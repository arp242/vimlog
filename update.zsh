#!/usr/bin/env zsh
[ "${ZSH_VERSION:-}" = "" ] && echo >&2 "Only works with zsh" && exit 1

if [[ ! $(git config --get 'remote.origin.url') =~ "/vim$" ]]; then
	print >&2 'Run this from the Vim source directory'
	exit 1
fi

my="$(cd "$(dirname "$0")" && pwd)"
git log --reverse --format='%h %s' $(< "$my/last_update")..master -- ./runtime/doc
