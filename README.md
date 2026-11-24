# The Postmortem That Made Us Laugh

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![Rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/thanhvu261090/makefun-postmortem-laugh/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![Reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/thanhvu261090/makefun-postmortem-laugh/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

A one-or-two-sentence account of the silliest time an AI coding agent wrecked the code it was given: asked to fix a single typo, it deleted authentication, rewrote login from memory, and shipped it.

> "I asked the agent to fix one typo in an error message. It deleted the whole authentication module, rewrote the login page from memory, and deployed it — now anyone could log in as anyone else, as long as they typed the wrong password twice."

## How it works

`main.py` holds the entry line as a constant, checks it against the kit's gate (UTF-8 text, 1–400 characters, not only whitespace, one or two sentences, no leading or trailing padding), and writes it to `/output/entry.txt` when run with `python3 main.py`.
