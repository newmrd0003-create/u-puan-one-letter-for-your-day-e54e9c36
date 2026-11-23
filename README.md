# One Letter for Your Day

[![One Letter for Your Day](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![Rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/newmrd0003-create/u-puan-one-letter-for-your-day-e54e9c36/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![Reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/newmrd0003-create/u-puan-one-letter-for-your-day-e54e9c36/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

## Entry

One letter: **J**.

J stands for **jinxed** — a day where everything that could go wrong did, as if cursed. One thing after another breaking, not a vague mood: the kind of day you can only describe as cursed.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes exactly one character — `J`, a single byte, no trailing newline — to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It then reads the file back and asserts the output is exactly one A–Z letter, so the gate (UTF-8 text of exactly 1 character) always passes.

## Run

```sh
python3 main.py
```

Check the output:

```sh
wc -c /output/entry.txt   # 1
cat /output/entry.txt      # J
```
