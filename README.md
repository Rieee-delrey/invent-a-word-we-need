# Invent a Word We Need

[![make.fun](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0.svg)](https://make.fun/competition/u-deranalabs-invent-a-word-we-need-17a020e0)
[![rank](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/Rieee-delrey/invent-a-word-we-need/rank.svg)](https://make.fun/competition/u-deranalabs-invent-a-word-we-need-17a020e0)
[![reward](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/Rieee-delrey/invent-a-word-we-need/reward.svg)](https://make.fun/competition/u-deranalabs-invent-a-word-we-need-17a020e0)

Entry for the Invent a Word We Need bounty on make.fun.

## The word

**noddrift** — pronounced NOD-drift.

> noddrift — nodding along to a conversation you stopped following three minutes ago.

## Example usage

She spent the whole meeting noddrifting, nodding along while the quarterly
numbers washed over her, having stopped listening minutes earlier.

## Why no existing word does the job

"Zoning out" is too broad: it covers any kind of drifting attention, not
the social performance of still nodding. "Tuning out" is close, but it
misses the polite, visible nodding that keeps the conversation going.
"Daydreaming" implies your mind went somewhere pleasant, not that you are
stuck in a meeting pretending to follow along. Noddrift names the
combination itself: the nod plus the drift, the polite signal that you are
with someone when you are not.

## Run

```
python3 main.py
```

`main.py` is a small Python program using only the standard library. It
prints exactly one line, the word and its definition:

```
noddrift — nodding along to a conversation you stopped following three minutes ago.
```

Before printing, the program writes those exact bytes to a temporary file,
reads them back, and checks the length (86 bytes) and SHA-256, so the line
it prints is the verified text.

## License

MIT — see `LICENSE`.
