# The Funniest Toaster Error Message

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/morenoo-del/makefun-toaster-20261124/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/morenoo-del/makefun-toaster-20261124/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

Entry for [The Funniest Toaster Error Message](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd) on make.fun.

## The entry

> ERROR E7: Bread jammed in slot 2. It has filed for residency and won.

One line, 69 characters. A deadpan appliance error message: the toaster
reports a jammed slice of bread the way a printer reports a paper jam —
except the bread has, bureaucratically, moved in for good. The joke lands
on first read, stays in one small appliance's voice, and never reaches for
a stock toaster pun.

## How it works

`main.py` (Python 3.13, no dependencies) writes the single line to
`/output/entry.txt`. It asserts the line is 1–120 characters and a single
line before writing, so an invalid entry fails loudly instead of shipping.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
