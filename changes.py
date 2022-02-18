
# [title, [vim version(s)], extended description]
#
# ["", '',
#     """ """],

changes = [
    ["|ModeChanged| event", ["8.2.3430"],
        """Triggered when the mode changes."""],

    ["Add multispace to 'listchars'", ["8.2.3424"],
        """Show two or more spaces no matter where they appear."""],

    ["Add digraph_get(), digraph_getlist(), digraph_set(), digraph_setlist()", ["8.2.3184", "8.2.3226"],
        """List and define digraphs from functions."""],

    ["Add list to 'breakindentopt'", ["8.2.3160", "8.2.3198"],
        """Add additional indent for lines that match a numbered or bulleted
            list (using the 'formatlistpat' setting)."""],

    ["Add <code>\%.l</code>, <code>\%<.l</code>, and <code>\%>.l</code> patterns", "8.2.3110",
        """Match the line the cursor is currently on; see |/\%l|."""],

    ["Add 'cryptmethod'=xchaha20", ["8.2.3022"],
        """More secure encryption from libsodium."""],

    ["Add |zp|, |zP|, |zy|", ["8.2.2914", "8.2.2971"],
        """|zp| pastes in block mode without adding trailing whitespace, |zy| yanks
            without trailing whitespace."""],

    ["Add %{ to 'statusline'", "8.2.2854",
        """%{expr} reëvaluates the expression as a 'statusline' formatting string."""],

    ["Add f flag in :vimgrep", "8.2.2813",
        """"Fuzzy" match :vimgrep results."""],

    ["Add 'autoshelldir'", "8.2.2675",
        """Automatically change directory in Vim from terminal window."""],

    ["Add strcharlen()", "8.2.2606",
        """Get length of string counting combining characters separately."""],

    ["Loop over a string", "8.2.2658",
        """Loop over a string as `for char in "str"`; loops are by codepoint
        with any combining characters."""],

    ["Expand 'fillchars'", ["8.2.2508", "8.2.2518", "8.2.2542", "8.2.2518", "8.2.2569"],
        """New values: "eob" to change change the (~) to indicate non-existing
            lines, "foldopen", "foldclose", and "foldsep" to change 'foldcolumn'
            markers.

            'fillchars' can be set per-window (previously it was always global).

            Also allow multibyte characters in 'fillchars' and 'statusline'.
        """],

    ["Add followwrap to 'diffopt'", ["8.2.2490"],
        """Don't reset 'wrap' for diff windows."""],

    ["Add fullcommand()", ["8.2.2468"],
        """Get the full command name from abbreviated ones (e.g. :s → :substitute)"""],

    ["lead: in 'listchars'", ["8.2.2454"],
        """Highlight leading spaces when 'list' is set."""],

    ["Detect focus events in terminal", ["8.2.2345", "8.2.2348", "8.2.2352", "8.2.2383", "8.2.2428"],
        """The |FocusGained| and |FocusLost| autocmds can work inside a terminal. See |xterm-focus-event|."""],

    [":sleep!", ["8.2.2366"],
        """Sleep and hide cursor."""],

    ["Add charcol(), getcharpos(), setcharpos(), getcursorcharpos(), setcursorcharpos()", "8.2.2324",
        """Multibyte-aware versions of col(), getpos(), setpos(), getcurpos(), cursor()."""],

    # 2020

    ['Add charidx()', "8.2.2233",
        """Convert byte index to character index."""],

    ["Add |VimSuspend| and |VimResume|", "8.2.2128",
        """Triggered on suspend/resume; only for &lt;C-z&gt; and not SIGSTP/SIGCONT signals."""],

    ['Add &lt;Cmd&gt;', "8.2.1978",
        """Don't change modes in this key mapping so that insert or visual mode
        mappings will always work without having to use &lt;C-u&gt; or &lt;C-o&gt;.
        For example <code>noremap &lt;C-q&gt; &lt;Cmd&gt;:normal! K&lt;CR&gt;</code>"""],

    [':sort and sort() can do locale-aware sorting', ["8.2.1933"],
        """<code>:sort l</code> or <code>sort(..., 'l')</code>."""],

    ["matchfuzzy(), matchfuzzypos()", ["8.2.1665", "8.2.1726", "8.2.1893", "8.2.1921"],
        """"Fuzzy" matching."""],

    ["Add |InsertLeavePre|", "8.2.1874",
        """Triggered before leaving insert mode."""],

    ["|??| operator", ["8.2.1794"],
        """<code>echo value ?? 'used if value is empty'</code>"""],

    ["Add gettext()", ["8.2.1544"],
        """Can be used to translate plugins."""],

    ["Add setcellwidths(), charclass()", ["8.2.1535", "8.2.1536"],
        """Allow overriding the display width for characters whose width is ambiguous."""],

    ["Add g&lt;Tab&gt;; support :tabnext #, :tabclose #, etc.", ["8.2.1401", "8.2.1413"],
        """g&lt;Tab&gt; goes back to the last accessed tab, and <code>#</code> in
        <code>:tab*</code> commands refer to the last accessed tab."""],

    ["expand('&lt;SID&gt;')", ["8.2.1347"],
        """Useful for the *func and *expr settings, e.g.
        <code>let &includexpr = expand('&lt;SID&gt;') .. 'fun()'</code> to use <code>s:fun()</code>"""],

    ["Add 'quickfixtextfunc'", ["8.2.0869", "8.2.0933", "8.2.0959", "8.2.1255"],
        """Customize text contents of quickfix window; can also be passed as an argument to to setqflist()"""],

    ["Add sorting to readir(), readirex()", ["8.2.0988"],
        """Add optional argument to readdir() and readdirex() to control sorting."""],

    ['Add terminalprops()', ["8.2.0970"],
        """List which features are supported in this terminal."""],

    ["Add 'spelloptions'", ["8.2.0953"],
        """Only accepted value is <code>camel</code> to spell check CamelCase words."""],

    ["Add |SigUSR1| autocmd", ["8.2.0952"],
        """Event to detect SIG_USR1."""],

    ["Add flatten()", ["8.2.0935"],
        """Flatten a list"""],

    ["Add getreginfo()", "8.2.0924",
        """Returns detailed information for a register information; can be restored by passing to setreg()."""],

    ["Add searchcount()", "8.2.0877",
        """Get details about current search."""],

    ["Allow setting underline colour in terminal", ["8.2.0863"],
        """Can use <code>ctermul</code> in :highlight to set the underline
        colour, or <code>guisp</code> if 'termguicolors' is enabled.""" ],

    ["Add reduce()", ["8.2.0878"],
        """Reduce list to single value."""],

    ["Add readirex()", ["8.2.0875"],
        """Like readdir(), but return a dict with attributes (i.e. stat() on Unix)."""],

    ["Add getmarklist()", "8.2.0861",
        """Get list of marks, similar to :marks"""],

    ["Add unsigned to 'nrformats'", ["8.2.0860"],
        """Ignore <code>-</code> before numbers and always treat them as unsigned
        for &lt;C-a&gt; and &lt;C-x&gt; so that using it on e.g. <code>1985-06-18</code> works as expected."""],

    ["Add mapset()", ["8.2.0807", "8.2.0812", "8.2.0815"],
        """Set mappings from a script, and can restore mappings."""],

    ["Call Vim functions from Lua", ["8.2.0775"],
        """Call Vim functions from Lua with <code>vim.call('fun_name', 'arg')</code> and <code>vim.fn.fun_name('arg')</code>."""],

    # ["Add "nostop" to 'backspace'", ["8.2.0590"],
    # 	"""
    # 		aa0489e12 #5940
    # https://groups.google.com/g/vim_use/c/tGICgxJmdf8
    # 		TODO: I can't figure this out, as ^W and ^U don't behave as documented
    # 		and identical to nostop(?)
    # 	"""],

    ["IPv6 support in channels", ["8.2.0557", "8.2.0574"],
        """IPv6 support in channels"""],

    ["Add echoraw()", ["8.2.0258"],
        """Output string to terminal with no processing; can be used to send escape codes."""],

    ["Add optional error code to :cquit", ["8.2.0095"],
        """Exit with a specific code, instead of always 1. |v:exiting| was added in 8.2.2070 (Nov 2020)"""],

    # 2019
    ["rand() and srand()", ["8.1.2342", "8.1.2343"],
        """Generate random numbers."""],

    ["interrupt()", ["8.1.2341"],
        """Abort a running script."""],

    ["strptime()", ["8.1.2326"],
        """Parse a time string"""],

    [":terminal ++shell", ["8.1.2251", "8.1.2255"],
        """Run :terminal commands in the shell."""],

    ["v:argv", ["8.1.2233"],
        """Get commandline arguments Vim was invoked with."""],

    ["Add |gM|", ["8.1.2231"],
        """Move to middle of line."""],

    ["|hl-LineNrAbove|, |hl-LineNrBelow|", ["8.1.2229"],
        """Highlight line numbers above and below the cursor when
        'relativenumber' is set."""],

    ["Add 'cursorlineopt'", ["8.1.2019"],
        """More control on how to display 'cursorline'."""],

    ["border and align in 'completepopup'", ["8.1.1902", "8.1.1904"],
        """More option to control completion popup menu."""],

    ["popup in 'completeopt'", ["8.1.1880", "8.1.1882"],
        """Show extra completion info in popup window (as an alternative to the
        preview window)."""],

    [":spellrare", ["8.1.1838"],
        """Mark words as rare in the spellfile."""],

    ["-&gt; operator", ["8.1.1835", "8.1.1834", "8.1.1809", "8.1.1803", "8.1.1996"],
        """<code>expr-&gt;fun(args)</code> is a shortcut for <code>fun(expr,
        args)</code> to improve readability:<br><code>[1, 2]-&gt;map({_, v -&gt;
        v + 1})</code>. See |method|."""],

    ["Popup windows", ["8.1.1799", "8.1.1391", "8.1.1364", "8.1.1905", "8.1.1928"],
        """Popup windows are like the completion window, but can be controlled
        in VimScript to a much greater degree. See |popup|, 'previewpopup'.
        This is still an experimental feature."""],

    ["'completeslash'", "8.1.1769",
        """Override 'shellslash' for completion."""],

    ["#{} dict notation", ["8.1.1705", "8.1.1692", "8.1.1683"],
        """The <code>#{}</code> notation is the same as the regular
        <code>{}</code> dict notation, except that the key values don't need
        quoting:<br><code>#{foo: "bar"}</code>."""],

    ["Sound functions", ["8.1.1565","8.1.1502"],
        """Ability to play sound; see sound_playevent()."""],

    ["|v:option_command|, |v:option_oldlocal|, |v:option_oldglobal|", ["8.1.1542"],
        """Improvements for the |OptionSet| event."""],

    [":const", ["8.1.1539"],
        """Constants; same as <code>:let v = 1 | :lockvar v</code>"""],

    ["win_execute()", ["8.1.1418"],
        """execute() in the context of a specific window."""],

    ["'wincolor'", ["8.1.1391"],
        """Highlight group to use instead of |hl-Normal| for this window."""],

    ["|g:actual_curwin|, |g:statusline_winid|", ["8.1.1372"],
        """Temporarily set when running expressions inside the 'statusline' (<code>%{expr}</code>)."""],

    ['|:let=<<|', ["8.1.1354"],
        """Heredoc assignment:<pre>let text =<< trim END\n\ttext\nEND</pre>"""],

    ['Text properties', ["8.1.0579", "8.1.1341", "8.1.1340"],
        """Assign metadata to text in a buffer, as an alternative to Vim's syntax highlighting.
            See |textprop|. This is still an experimental feature."""],

    ["listener_add()", ["8.1.1320", "8.1.1321", "8.1.1332"],
        """Add a callback that will be invoked when changed have been made to a buffer."""],

    ["Default values for function arguments", ["8.1.1310"],
        """e.g. <code>function Fun(value=10)</code>. See |optional-function-argument|."""],

    [':xrestore', "8.1.1307",
        """Reconnect to X server after restart."""],

    ['environ(), getenv(), and setenv()', "8.1.1305",
        """Deal with environment variables."""],

    ["chdir()", ["8.1.1291"],
        """Change directory with scope and ability to restore."""],

    [":cbefore, :cafter", ["8.1.1275"],
        """Navigate to errors before/after the cursor."""],

    ["Show match position when searching", ["8.1.1270"],
        """Show "3/44" when using |n| and "S" is not in 'shortmess'."""],

    [":cabove, :cbelow, :labove, :lbelow", ["8.1.1256"],
        """Navigate through errors relative to the cursor."""],

    ["Control font weight on Windows'", ["8.1.1224"],
        """Use "W" in 'guifont' to control font weight on Windows. See |gui-font|. """],

    ["Tab-local directory", ["8.1.1218"],
        """ See :tcd. Similar to the window-local directory with :lcd. """],

    ["v: prefix is required", ["8.1.1188"],
        """Previously e.g. <code>count</code> would also work. The
        <code>v:</code> prefix is mandatory when :scriptversion is 3 or
        higher."""],

    ["Add more arguments to winnr()", ["8.1.1140"],
        """To find out what neighbors a window has."""],

    ["|CompleteChanged| event", ["8.1.1138"],
        """After each time the Insert mode completion menu changed."""],

    ["str2list() and list2str()", ["8.1.1122"],
        """Convert a string to a list of byte, or the reverse."""],

    ["readdir()", ["8.1.1120"],
        """Get contents of a directory."""],

    [":scriptversion", ["8.1.1116"],
        """Specify VimScript compatibility level."""],

    ["<code>..</code> operator", ["8.1.1114"],
        """String concatenation operator, as <code>.</code> is ambiguous.
        <code>'a' .. 'b'</code> and <code>'a' . 'b'</code> are identical.
        Also adds <code>..=</code>."""],

    ["<code>++once</code> argument for :autocmd", ["8.1.1113"],
        """Run an autocommand just once, e.g. <code>au CursorMoved * ++once :echom 'ONCE'</code>."""],

    ["Add window ID argument to matchdelete(), clearmatches(), getmatches(), setmatches()", ["8.1.1084"],
        """ """],

    ["complete_info()", ["8.1.1068"],
        """Get information about current completion."""],

    ["rubyeval() ", ["8.1.1056"],
        """Evaluate a Ruby expression."""],

    ["|CTRL-W_gt|, |CTRL-W_gT|", ["8.1.0972"],
        """Switch tabs, like |gt| and |gT|. Mainly useful to switch from terminal window."""],

    ["<code>*=</code>, <code>/=</code>, <code>%=</code> ", ["8.1.0902"],
        """e.g. <code>let var *= 2</code>"""],

    ["<code>a:</code> variables are immutable", ["8.1.0888", "8.1.0897"],
        """Previously it was possible to change <code>a:</code> variables in some cases."""],

    ["|[:ident:]|, |[:keyword:]|, |[:fname:]|", ["8.1.0862"],
        """"""],

    ["Allow for a third character for \"tab:\" in 'listchars'", ["8.1.0759"],
        """Third character is set as the last one for a tab, e.g. <code>set listchars=tab:(_)</code> shows a tab as <code>(______)</code>."""],

    ["Blob type", ["8.1.0735", "8.1.0757", "8.1.0756"],
        """A blob stores binary data. Blob literals start with <code>0z</code>, e.g. <code>0zDEADBEEF</code>. See |blob|."""],

    ["\"p\" flag in 'formatoptions'", ["8.1.0728"],
        """Don't break lines at single spaces that follow periods."""],

    [":redrawtabline", ["8.1.0706"],
        """Redraw tabline after changing 'tabline' (mainly useful for plugins)."""],

    # 2018
    ["sign_place(), sign_unplace(), etc", ["8.1.0614", "8.1.0658"],
        """Functions for defining and placing signs."""],

    ["Allow functions and commands to redefine themselves", ["8.1.0515", "8.1.0573"],
        """Previously a <code>!</code> always had to be added to <code>function</code>
        to overwrite a function with the same name. Now Vim is smarter and
        allows a function to overwrite itself. This means that using
        <code>function!</code> in your vimrc or plugin's autoload is almost
        never required any more.
    """],

    [":filter support for more commands", ["8.0.1651", "8.1.0165", "8.1.0495"],
        """ """],

    [":tlmenu", ["8.1.0487"],
        """Popup menu for terminal."""],

    ['Include the xdiff library', ["8.1.0360", "8.1.0393"],
        """Include diff library instead of relying on external tools to improve
        diff quality. Many new 'diffopt' settings (e.g. <code>set
        diffopt+=internal,algorithm:patience</code> would be a good setting for
        many)."""],

    [" \"\\ ", ["8.1.0369"],
            """Comments in line continuations; see |line-continuation-comment|: <pre>
au FileType git
            "\ Go to commit.
            \  nnoremap &lt;Leader&gt;g :exe printf(":!cd ~/src/vim && git diff %s^\\!", split(getline("."), ' ')[1])&lt;CR&gt;
            "\ Delete commit.
            \| nnoremap &lt;Leader&gt;d :call search('^commit ', 'bc') \| :exe 'd' . (search('^commit ', 'n') - line("."))&lt;CR&gt;
</pre>
            """],

    ["|cfilter-plugin|", ["8.1.0311"],
        """Filter quickfix/location list"""],

    ["'vartabstop', 'varsofttabstop'", ["8.1.0105"],
        """Variable tabstop widths, e.g. <code>set vartabstop=4,8</code> makes
            the first tab 4 spaces, and the rest 8."""],

    ["|OptionSet| autocmd", ["8.1.0081", "8.1.0414"],
        """Triggered whenever an option is set."""],

    ["prompt buffer", ["8.1.0027", "8.1.0035"],
        """Mainly useful to feed user input to a job."""],

    ["Allow :unlet $ENV", ["8.0.1832"],
        """Previously there was no way to truly unset an environment variable
            (just set it to an empty string)."""],

    ["CTRL-R CTRL-L", ["8.0.1787"],
        """Insert line from buffer in commandline"""],

    ["job_info() without argument lists all jobs", ["8.0.1742"],
        """"""],

    ["mkdir('p') won't fail fail if the directory already exists", ["8.0.1708"],
        """ """],

    ["Add the terminal API.", ["8.0.1641"],
        """See |terminal-api|."""],

    ["trim()", ["8.0.1630"],
        """Clean whitespace; had to use substitute() before."""],

    ["Add \"!\" to 'guioptions'", ["8.0.1609", "8.0.1616"],
        """Use a Vim terminal window for :! shell commands."""],

    ['Menus in terminal', ["8.0.1558", "8.0.1570"],
        """Make :popup and right-click work in terminal."""],

    ["24 bit colors in Windows console", ["8.0.1531"],
        """See 'termguicolors'."""],

    ["'pumwidth'", "8.0.1491",
        """Minimum width of completion menu."""],

    ["|DirChanged| event", ["8.0.1459"],
        """When directory changed (with :cd, :lcd, etc.)"""],

    ["|CmdlineChanged| event", ["8.0.1445"],
        """After a change was made to the text in the command line."""],

    # 2017
    ["|TextYankPost| event", ["8.0.1394"],
        """After yanking or deleting text."""],

    ["win_screenpos().", ["8.0.1364"],
        """Get winow position."""],

    ["|CmdlineEnter|, |CmdlineLeave|", ["8.0.1206"],
        """When entering and leaving the commandline."""],

    [":terminal ", ["8.0.0693", "8.0.0730", "8.0.0744", "8.0.0804", "8.0.0929", "8.0.1108"],
        """Terminal buffer."""],

    ["|--clean|, 'viminfofile'", ["8.0.0716"],
        """Start Vim with the default settings and without plugins."""],

    ["E flag in 'cinoptions'", ["8.0.0431"],
        """Set indent for extern block."""],

    ["'pyxversion', :pythonx", ["8.0.0251"],
        """Make it easier to run Python code in both Python 2 and 3, depending
        on what is available."""],
]
