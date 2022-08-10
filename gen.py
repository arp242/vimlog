#!/usr/bin/env python3

import html
import re
import subprocess
import sys
import urllib.parse

from changes import changes

# Location of Vim source, git checkout
vimsrc = '/home/martin/src/vim'

# Load helptags.
tags = {}
for line in open(vimsrc + '/runtime/doc/tags').readlines():
    tag, file, _ = line.split('\t')
    tag = tag.replace('&lt;', '<').replace('&gt;', '>')
    tags[tag] = file

help_url = '<a target="_blank" class="help-{}" href="https://vimhelp.org/{}.html#{}">{}</a>'


def opt(klass):
    def f(m):
        tag = m.group(0)
        file = tags.get(tag.strip(), None)
        if file is None:
            return tag
        return help_url.format(klass, file, urllib.parse.quote_plus(tag), tag)
    return f


def helptag(m):
    tag = m.group(1)
    file = tags.get(tag, None)
    if file is None:
        return m.group(0)
    return help_url.format('tag', file, urllib.parse.quote_plus(tag), tag)


def helpify(text):
    text = re.sub(r"('\w+')", opt('option'), text)               # 'option'
    text = re.sub(r'\b(\w+)\(\)', opt('tag'), text)              # function()
    text = re.sub(r':([\w]+)[^|.]', opt('tag'), text)            # :ex
    text = re.sub(r'\|([-\w/?:\\<>%=\[\].]+)\|', helptag, text)  # |tag|
    return text


# Load all commits.
commits = subprocess.run(['git', '-C', vimsrc, 'tag', '--list',
                         '--format', '%(refname:strip=2)|%(objectname)|%(authordate)'],
                         capture_output=True)
if commits.returncode > 0:
    print(commits.stderr.decode())
    sys.exit(commits.returncode)

commits = [l.split('|') for l in commits.stdout.decode().split('\n')[:-1]]
commits.reverse()


def find_commit(version):
    for c in commits:
        if c[0] == 'v' + version:
            return c
    print(f'no commit found for "{version}"', file=sys.stderr)
    sys.exit(1)


def in_neovim(patch):
    return True


def gen_html():
    html = '<h2>2022</h2>\n'
    last_year = '2022'
    for c in changes:
        if type(c[1]) == str:
            c[1] = [c[1]]
        version = []
        c[1] = sorted(c[1])
        for i, p in enumerate(c[1]):
            commit = find_commit(p)

            # ['v8.1.1833', '0c779e8e4831c538918ae835ce3365af028e36ea', 'Fri Aug 9 17:01:02 2019 +0200']
            if i == len(c[1]) - 1:
                year = commit[2][-10:-6]
                if year != last_year:
                    html += f'\n<h2>{year}</h2>\n'
                    last_year = year

            d = commit[2][4:10].strip()
            l = f'https://github.com/vim/vim/commit/{commit[1]}'
            # Only put the date on the last one.
            if i == len(c[1]) - 1:
                version.append(f'<a target="_blank" href="{l}">{p}</a> <sup>({d})</sup>')
            else:
                version.append(f'<a target="_blank" href="{l}">{p}</a>')
        #last_version = version.pop()
        html += f'''<section><div><h3>{helpify(c[0])}</h3><p>{', '.join(version)}</p></div><p>{helpify(c[2])}</p></section>\n'''

    lu = commits[0]
    lud = commits[0][2].split(' ')
    last_update = f'{lu[0][1:]} ({lud[1]} {lud[2]} {lud[4]})'

    with open('last_update', 'w') as fp:
        fp.write(f'v{last_update.split(" ")[0]}\n')

    with open('index.html', 'w') as fp:
        fp.write(open('tpl.html').read().
                 replace('%%CONTENT%%', html).
                 replace('%%LAST_UPDATE%%', last_update))


def gen_rss():
    escape = lambda t: html.escape(t.replace('<code>', '').replace('</code>', ''))

    xml = ''
    for c in changes:
        if type(c[1]) == str:
            c[1] = [c[1]]
        c[1] = sorted(c[1])

        title = '{} [{}]'.format(escape(c[0]), ', '.join(c[1]))
        link = "https://www.arp242.net/vimlog"
        desc = escape(c[2])
        xml += f'''<item><title>{title}</title><link>{link}</link><description>{desc}</description></item>\n'''

    with open('feed.xml', 'w') as fp:
        fp.write(open('tpl.xml').read().replace('%%CONTENT%%', xml))

if __name__ == '__main__':
    gen_html()
    gen_rss()
