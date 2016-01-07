#!/usr/bin/env bash
{ set +x; } 2>/dev/null

! [ -x "${BASH_SOURCE[0]}" ] && ( set -x; chmod +x "${BASH_SOURCE[0]}" )

if [ -t 1 ] && [ -e ~/.command/config.sh ]; then
	{ set -x;  . ~/.command/config.sh; { set +x; } 2>/dev/null; }
fi

{ set -x;  cd "${BASH_SOURCE[0]%/*/*}"; { set +x; } 2>/dev/null; }
find="$(find . -type f -name "test_*.sh" -o -name "test.sh" -o -name "tests.sh")"
[[ -z $find ]] && exit
while IFS= read sh; do
	( set -x; . "$sh" ) && echo || exit
done <<< "$find";:
