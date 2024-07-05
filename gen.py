#!/usr/bin/env python3

import copy, html, re, subprocess, sys, urllib.parse
from changes import changes

# Location of Vim source, git checkout
vimsrc = '/home/martin/src/vim'
if len(sys.argv) > 1:
    vimsrc = sys.argv[1]

# Load helptags.
tags = {}
try:
    for line in open(vimsrc + '/runtime/doc/tags').readlines():
        tag, file, _ = line.split('\t')
        tag = tag.replace('&lt;', '<').replace('&gt;', '>')
        tags[tag] = file
except FileNotFoundError as e:
    print(e, file=sys.stderr)
    print('set the first argument to a git checkout of the Vim source directory', file=sys.stderr)
    sys.exit(1)

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
    text = re.sub(r':([\w]+)[^|.,]', opt('tag'), text)           # :ex
    text = re.sub(r'\|([-\w/?:\\<>%=\[\].]+)\|', helptag, text)  # |tag|
    return text


# Load all commits.
commits = subprocess.run(['git', '-C', vimsrc, 'tag', '--list',
                         '--format', '%(refname:strip=2)|%(objectname)|%(creatordate)'],
                         capture_output=True)
if commits.returncode > 0:
    print(commits.stderr.decode())
    sys.exit(commits.returncode)

commits = [l.split('|') for l in commits.stdout.decode().split('\n')[:-1]]
commits.reverse()


def find_commit(version):
    if version == '…many…':
        return version

    for c in commits:
        if c[0] == 'v' + version:
            return c
    print(f'no commit found for "{version}"', file=sys.stderr)
    sys.exit(1)


# neosrc = '/home/martin/src/neovim'
# neo_commits = subprocess.run(['git', '-C', neosrc, 'log', '--format=%H|%s'],
#                              capture_output=True)
# if neo_commits.returncode > 0:
#     print(neo_commits.stderr.decode())
#     sys.exit(neo_commits.returncode)
# 
# neo_commits = [l.split('|') for l in neo_commits.stdout.decode().split('\n')[:-1] if l.find('vim-patch') > -1]
# neo_map = {}
# for c in neo_commits:
#     h = c[0]
#     sub = c[1]
#     
#     text = re.find(r'vim-patch:[0-9a-f.{}]+', sub)


def in_neovim(patch):
    # We can get this from the Neovim commit log, but the format isn't 100%
    # consistent:
    #
    # c65b1f3e1 vim-patch:9.0.0342: ":wincmd =" equalizes in two directions
    # 95b8e2c55 vim-patch:partial:8.1.0822: peeking and flushing output slows down execution
    # 6a13b8fa5 vim-patch:7dd543246a4c (#19960)
    # f3c8f3e5d vim-patch:partial:8a3b805c6c9c (#19104)
    # eea6a4f2a vim-patch:8.2.{0212,0250}
    # 1b5f53ca9 vim-patch:7.4.212
    # e9e16655a [RFC] vim-patch:8.1.1378: delete() can not handle a file name that looks li… (#16268)
    # 65b823226 vim-patch:8.2.{210,424,436,...} #15976
    # 55d1e630b Merge #15731 vim-patch:7.4.725,8.2.{0597,0598,0924,1035}
    #
    # Check which tags apply for a commit:
    #
    #   git tag --contains 65b823226
    #
    #   nightly
    #   stable
    #   v0.6.0
    #   v0.6.1
    #   v0.7.0
    #   v0.7.1
    #   v0.7.2
    #
    # Or list all commits for a tag:
    #
    #   git rev-list v0.7.2
    return True


def has_elip(version_list):
    try:
        version_list.remove('…')
        return True
    except ValueError:
        return False


def gen_html():
    html = '<h2>2023</h2>\n'
    last_year = '2023'

    for c in changes:
        c = copy.deepcopy(c)
        if type(c[1]) == str:
            c[1] = [c[1]]

        elip = has_elip(c[1])
        c[1] = sorted(c[1])
        version = []
        for i, p in enumerate(c[1]):
            commit = find_commit(p)

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

        if elip:
            version.insert(len(version) - 1, '…many…')

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

        elip = has_elip(c[1])
        c[1] = sorted(c[1])

        if elip:
            c[1].insert(len(c[1]) - 1, '…many…')

        title = '{} [{}]'.format(escape(c[0]), ', '.join(c[1]))
        link = "https://www.arp242.net/vimlog"
        desc = escape(c[2])
        xml += f'''<item><title>{title}</title><link>{link}</link><description>{desc}</description></item>\n'''

    with open('feed.xml', 'w') as fp:
        fp.write(open('tpl.xml').read().replace('%%CONTENT%%', xml))

if __name__ == '__main__':
    gen_html()
    gen_rss()
