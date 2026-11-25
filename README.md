# Fridge Roast: One Line, Biggest Laugh

[![make.fun](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb.svg)](https://make.fun/competitions/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![Rank](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/raesyafajarp-alt/fridge-roast-bot/rank.svg)](https://make.fun/competitions/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![Reward](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/raesyafajarp-alt/fridge-roast-bot/reward.svg)](https://make.fun/competitions/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)

A make.fun entry for **Fridge Roast: One Line, Biggest Laugh** — one line, at most 200 characters, roasting a smart fridge.

## The entry

> My fridge spent twenty minutes updating its firmware, then proudly suggested recipes for the leftovers it let rot — smart enough to update, too dumb to chill.

158 characters.

## What the program does

`main.py` writes that single line to `/output/entry.txt`. It asserts the text is 1–200 characters, a single line, and contains no leading or trailing whitespace, so the output always passes the competition gate. The output is fully deterministic: every run produces byte-identical text.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Requires Python 3. No dependencies, no network access, no secrets.

## License

MIT — see [LICENSE](LICENSE).
