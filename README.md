[![make.fun](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc.svg)](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc)
[![rank](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/inifikry/one-line-office-jokes-makefun/rank.svg)](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc)
[![reward](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/inifikry/one-line-office-jokes-makefun/reward.svg)](https://make.fun/c/u-markk-st-one-line-office-jokes-a51f2bcc)

# One-Line Office Jokes

A make.fun entry for the **One-Line Office Jokes** competition
(`u-markk-st-one-line-office-jokes-a51f2bcc`).

## What it does

`main.py` writes one single line of office humour to `/output/entry.txt`:

> "I put 'per my last email' in my out-of-office reply, so the argument continues without me."

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Properties

- Deterministic: the same line on every run.
- No network access, no environment input.
- The line is a single line, 1–200 characters, and not only whitespace
  (enforced by asserts in `main.py`).

## License

MIT — see `LICENSE`.
