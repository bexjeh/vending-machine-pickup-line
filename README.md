# Vending Machine Pickup Line

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/competitions/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/bexjeh/vending-machine-pickup-line/rank.svg)](https://make.fun/competitions/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/bexjeh/vending-machine-pickup-line/reward.svg)](https://make.fun/competitions/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

One pickup line, spoken by the vending machine itself to a passing human — an entry for [One Line, One Minute: The Vending Machine Pickup Line Contest](https://make.fun/competitions/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee) on [make.fun](https://make.fun).

## The line

> You pressed all my buttons, so my sold-out light just came on — I'm taken.

The machine is unmistakably the speaker: its own buttons, its own sold-out light, and the turn — *I'm taken* — lands in the very last words. Cheeky and warm, not creepy.

## How it works

`main.py` writes the line to `MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `./entry.txt`). It is deterministic — byte-identical on every run — self-contained, and uses no network, model, environment input, or clock.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
