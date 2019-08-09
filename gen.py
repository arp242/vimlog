#!/usr/bin/env python
#

# [title, [vim version(s)], extended description]
changes = [
    # 2019

    ["popup in 'completeopt'", ['8.1.1880', '8.1.1882'],
        '''Show extra completion info in popup window (as an alternative to the
        preview window).'''],

    [":spellrare", ['8.1.1838'],
        '''Mark words as rare in the spellfile.'''],

    ["-&gt; operator", ['8.1.1835', '8.1.1834', '8.1.1809', '8.1.1803', '8.1.1888'],
        '''<code>expr-&gt;fun(args)</code> is a shortcut for <code>fun(expr,
        args)</code> to improve readability:<br><code>[1, 2]-&gt;map({_, v -&gt;
        v + 1})</code>. See |method|.'''],

    ["Popup windows", ['8.1.1799', '8.1.1391', '8.1.1364'],
        '''Popup windows are like the completion window, but can be controlled
        in VimScript to a much greater degree. See |popup|, 'previewpopup'.
        This is still an experimental feature.'''],

    ["'completeslash'", '8.1.1769',
        '''Override 'shellslash' for completion.'''],

    ["#{} dict notation", ['8.1.1705', '8.1.1692', '8.1.1683'],
        '''The <code>#{}</code> notation is the same as the regular
        <code>{}</code> dict notation, except that the key values don't need
        quoting:<br><code>#{foo: "bar"}</code>.'''],

    ["Sound functions", ['8.1.1565','8.1.1502'],
        '''Ability to play sound; see sound_playevent().'''],

    ["|v:option_command|, |v:option_oldlocal|, |v:option_oldglobal|", ['8.1.1542'],
        '''Improvements for the |OptionSet| event.'''],

    [":const", ['8.1.1539'],
        '''Constants; same as <code>:let v = 1 | :lockvar v</code>'''],

    ["win_execute()", ['8.1.1418'],
        '''execute() in the context of a specific window.'''],

    ["'wincolor'", ['8.1.1391'],
        '''Highlight group to use instead of |hl-Normal| for this window.'''],

    ["|g:actual_curwin|, |g:statusline_winid|", ['8.1.1372'],
        '''Temporarily set when running expressions inside the 'statusline' (<code>%{expr}</code>).'''],

    ['|:let=<<|', ['8.1.1354'],
        '''Heredoc assignment:<pre>let text =<< trim END\n\ttext\nEND</pre>'''],

    ['Text properties', ['8.1.0579', '8.1.1341', '8.1.1340'],
        '''Assign metadata to text in a buffer, as an alternative to Vim's syntax highlighting.
            See |textprop|. This is still an experimental feature.'''],

    ["listener_add()", ['8.1.1320', '8.1.1321', '8.1.1332'],
        '''Add a callback that will be invoked when changed have been made to a buffer.'''],

    ["Default values for function arguments", ['8.1.1310'],
        '''e.g. <code>function Fun(value=10)</code>. See |optional-function-argument|.'''],

    [':xrestore', '8.1.1307',
        '''Reconnect to X server after restart.'''],

    ['environ(), getenv(), and setenv()', '8.1.1305',
        '''Deal with environment variables.'''],

    ["chdir()", ['8.1.1291'],
        '''Change directory with scope and ability to restore.'''],

    [":cbefore, :cafter", ['8.1.1275'],
        '''Navigate to errors before/after the cursor.'''],

    ["Show match position when searching", ['8.1.1270'],
        '''Show "3/44" when using |n| and "S" is not in 'shortmess'.'''],

    [":cabove, :cbelow, :labove, :lbelow", ['8.1.1256'],
        '''Navigate through errors relative to the cursor.'''],

    ["Control font weight on Windows'", ['8.1.1224'],
        '''Use "W" in 'guifont' to control font weight on Windows. See |gui-font|. '''],

    ["Tab-local directory", ['8.1.1218'],
        ''' See :tcd. Similar to the window-local directory with :lcd. '''],

    ["v: prefix is required", ['8.1.1188'],
        '''Previously e.g. <code>count</code> would also work. The
        <code>v:</code> prefix is mandatory when :scriptversion is 3 or
        higher.'''],

    ["Add more arguments to winnr()", ['8.1.1140'],
        '''To find out what neighbors a window has.'''],

    ["|CompleteChanged| event", ['8.1.1138'],
        '''After each time the Insert mode completion menu changed.'''],

    ["str2list() and list2str()", ['8.1.1122'],
        '''Convert a string to a list of byte, or the reverse.'''],

    ["readdir()", ['8.1.1120'],
        '''Get contents of a directory.'''],

    [":scriptversion", ['8.1.1116'],
        '''Specify VimScript compatibility level.'''],

    ["<code>..</code> operator", ['8.1.1114'],
        '''String concatenation operator, as <code>.</code> is ambiguous.
        <code>'a' .. 'b'</code> and <code>'a' . 'b'</code> are identical.
        Also adds <code>..=</code>.'''],

    ["<code>++once</code> argument for :autocmd", ['8.1.1113'],
        '''Run an autocommand just once, e.g. <code>au CursorMoved * ++once :echom 'ONCE'</code>.'''],

    ["Add window ID argument to matchdelete(), clearmatches(), getmatches(), setmatches()", ['8.1.1084'],
        ''' '''],

    ["complete_info()", ['8.1.1068'],
        '''Get information about current completion.'''],

    ["rubyeval() ", ['8.1.1056'],
        '''Evaluate a Ruby expression.'''],

    ["|CTRL-W_gt|, |CTRL-W_gT|", ['8.1.0972'],
        '''Switch tabs, like |gt| and |gT|. Mainly useful to switch from terminal window.'''],

    ["<code>*=</code>, <code>/=</code>, <code>%=</code> ", ['8.1.0902'],
        '''e.g. <code>let var *= 2</code>'''],

    ["<code>a:</code> variables are immutable", ['8.1.0888', '8.1.0897'],
        '''Previously it was possible to change <code>a:</code> variables in some cases.'''],

    ["|[:ident:]|, |[:keyword:]|, |[:fname:]|", ['8.1.0862'],
        ''''''],

    ["Allow for a third character for \"tab:\" in 'listchars'", ['8.1.0759'],
        '''Third character is set as the last one for a tab, e.g. <code>set listchars=tab:(_)</code> shows a tab as <code>(______)</code>.'''],

    ["Blob type", ['8.1.0735', '8.1.0757', '8.1.0756'],
        '''A blob stores binary data. Blob literals start with <code>0z</code>, e.g. <code>0zDEADBEEF</code>. See |blob|.'''],

    ["\"p\" flag in 'formatoptions'", ['8.1.0728'],
        '''Don't break lines at single spaces that follow periods.'''],

    [":redrawtabline", ['8.1.0706'],
        '''Redraw tabline after changing 'tabline' (mainly useful for plugins).'''],

    # 2018
    ["sign_place(), sign_unplace(), etc", ['8.1.0614', '8.1.0658'],
        '''Functions for defining and placing signs.'''],

    ["Allow functions and commands to redefine themselves", ['8.1.0515', '8.1.0573'],
        '''Previously a <code>!</code> always had to be added to <code>function</code>
        to overwrite a function with the same name. Now Vim is smarter and
        allows a function to overwrite itself. This means that using
        <code>function!</code> in your vimrc or plugin's autoload is almost
        never required any more.
    '''],

    [":filter support for more commands", ['8.0.1651', '8.1.0165', '8.1.0495'],
        ''' '''],

    [":tlmenu", ['8.1.0487'],
        '''Popup menu for terminal.'''],

    ['Include the xdiff library', ['8.1.0360', '8.1.0393'],
        '''Include diff library instead of relying on external tools to improve
        diff quality. Many new 'diffopt' settings (e.g. <code>set
        diffopt+=internal,algorithm:patience</code> would be a good setting for
        many).'''],

    [" \"\\ ", ['8.1.0369'],
            '''Comments in line continuations; see |line-continuation-comment|: <pre>
au FileType git
            "\ Go to commit.
            \  nnoremap &lt;Leader&gt;g :exe printf(":!cd ~/src/vim && git diff %s^\\!", split(getline('.'), ' ')[1])&lt;CR&gt;
            "\ Delete commit.
            \| nnoremap &lt;Leader&gt;d :call search('^commit ', 'bc') \| :exe 'd' . (search('^commit ', 'n') - line('.'))&lt;CR&gt;
</pre>
            '''],

    ["|cfilter-plugin|", ['8.1.0311'],
        '''Filter quickfix/location list'''],

    ["'vartabstop', 'varsofttabstop'", ['8.1.0105'],
        '''TODO'''],

    ["promp buffer", ['8.1.0027', '8.1.0035'],
        '''Mainly useful to feed user input to a job.'''],

    ["Allow :unlet $ENV", ['8.0.1832'],
        '''Previously there was no way to truly unset an environment variable
            (just set it to an empty string).'''],

    ["CTRL-R CTRL-L", ['8.0.1787'],
        '''Insert line from buffer in commandline'''],

    ["job_info() without argument lists all jobs", ['8.0.1742'],
        ''''''],

    ["mkdir('p') won't fail fail if the directory already exists", ['8.0.1708'],
        ''' '''],

    ["Add the terminal API.", ['8.0.1641'],
        '''See |terminal-api|.'''],

    ["trim()", ['8.0.1630'],
        '''Clean whitespace; had to use substitute() before.'''],

    ["Add \"!\" to 'guioptions'", ['8.0.1609', '8.0.1616'],
        '''Use a Vim terminal window for :! shell commands.'''],

    ['Menus in terminal', ['8.0.1558', '8.0.1570'],
        '''Make :popup and right-click work in terminal.'''],

    ["24 bit colors in Windows console", ['8.0.1531'],
        '''See 'termguicolors'.'''],

    ["'pumwidth'", '8.0.1491',
        '''Minimum width of completion menu.'''],

    ["|DirChanged| event", ['8.0.1459'],
        '''When directory changed (with :cd, :lcd, etc.)'''],

    ["|CmdlineChanged| event", ['8.0.1445'],
        '''After a change was made to the text in the command line.'''],

    # 2017
    ["|TextYankPost| event", ['8.0.1394'],
        '''After yanking or deleting text.'''],

    ["win_screenpos().", ['8.0.1364'],
        '''Get winow position.'''],

    ["|CmdlineEnter|, |CmdlineLeave|", ['8.0.1206'],
        '''When entering and leaving the commandline.'''],

    [":terminal ", ['8.0.0693', '8.0.0730', '8.0.0744', '8.0.0804', '8.0.0929', '8.0.1108'],
        '''Terminal buffer.'''],

    ["|--clean|, 'viminfofile'", ['8.0.0716'],
        '''Start Vim with the default settings and without plugins.'''],

    ["E flag in 'cinoptions'", ['8.0.0431'],
        '''Set indent for extern block.'''],

    ["'pyxversion', :pythonx", ['8.0.0251'],
        '''Make it easier to run Python code in both Python 2 and 3, depending
        on what is available.'''],

]


import subprocess
import sys
import re

# Load helptags.
tags = {}
for line in open('/home/martin/src/vim/runtime/doc/tags').readlines():
    tag, file, _ = line.split('\t')
    tag = tag.replace('&lt;', '<').replace('&gt;', '>')
    tags[tag] = file

help_url = '<a target="_blank" class="help-{}" href="https://vimhelp.org/{}.html#{}">{}</a>'
def opt(klass):
    def f(m):
        tag = m.group(0)
        file = tags.get(tag, None)
        if file is None:
            return tag
        return help_url.format(klass, file, tag, tag)
    return f

def helptag(m):
    tag = m.group(1)
    file = tags.get(tag, None)
    if file is None:
        return m.group(0)
    return help_url.format('tag', file, tag, tag)

def helpify(text):
    text = re.sub(r"('\w+')", opt('option'), text)             # 'option'
    text = re.sub(r'\b(\w+)\(\)', opt('tag'), text)            # function()
    text = re.sub(r':([\w]+)[^|]', opt('tag'), text)           # :ex
    text = re.sub(r'\|([-\w/:\\<>%=\[\]]+)\|', helptag, text)  # |tag|
    return text

# Load all commits.
commits = subprocess.run(['git', '-C', '/home/martin/src/vim', 'tag', '--list',
                      '--format', '%(refname:strip=2)|%(objectname)|%(authordate)'],
                      capture_output=True)
if commits.returncode > 0:
    print(commits.stderr.decode())
    sys.exit(commits.returncode)

commits = [l.split('|') for l in commits.stdout.decode().split('\n')[:-1]]
commits.reverse()

html = '<h2>2019</h2>\n'
last_year = '2019'
for c in changes:
    if type(c[1]) == str:
        c[1] = [c[1]]
    version = []
    c[1] = sorted(c[1])
    for i, p in enumerate(c[1]):
        for co in commits:
            if co[0] == 'v' + p:
                commit = co
                break

        # ['v8.1.1833', '0c779e8e4831c538918ae835ce3365af028e36ea', 'Fri Aug 9 17:01:02 2019 +0200']^J
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

with open('index.html', 'w') as fp:
    fp.write(open('tpl.html').read().replace('%%CONTENT%%', html))
