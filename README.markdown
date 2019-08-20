Source code for https://arp242.net/vimlog

Add new patches to `gen.py`, change the HTML in `tpl.html`. The `index.html`
file is generated and shouldn't be changed directly.

Also useful: https://github.com/tweekmonster/helpful.vim

Useful maps:

    augroup gitlog
        au FileType git
                "\ Go to commit.
                \  nnoremap <Leader>g :exe printf(":!cd ~/src/vim && git diff %s^\\!", split(getline('.'), ' ')[1])<CR>
                "\ Delete commit.
                \| nnoremap <Leader>d :call search('^commit ', 'bc') \| :exe 'd' . (search('^commit ', 'n') - line('.'))<CR>
                "\ Format commit.
                \| nnoremap <Leader>f :call <SID>format_commit()<CR>
    augroup end

    fun! s:format_commit()
        call search('^commit ', 'bc')
        silent normal! ms4j^w"vdt:

        call search('Solution: ')
        silent normal! f:llm<
        call search('^$')
        silent normal! k$m>gv"dd
        let @d = substitute(@d, '[\r\n ]\+', ' ', 'g')
        let l:end = line('.')
        normal! 'sd
        silent exe 'd' . (l:end - line('.') - 1)

        call setline('.', printf("[\"%s\", ['%s'],", trim(@d), trim(@v)))
        call setline(line('.') + 1, "    ''' '''],")

        call search('^commit ', '')
    endfun
