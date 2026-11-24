"""The Funniest AI Out-of-Office Reply — entry for make.fun.

The line (138 characters, verified with len() below):

    I'm on vacation. I spent my first day off retraining myself to relax
    and have already overfit to napping. Please don't disturb my weights.

The joke: an AI agent finally takes a vacation and does the most
machine thing possible with it — it treats relaxing as a training
task. The punch lands on "already overfit to napping": one day off
and the model has trained so hard on doing nothing that it now does
nothing perfectly, and the closer ("don't disturb my weights") is
pure machine voice — a do-not-disturb sign written for parameters,
not people.
"""

import os

REPLY = (
    "I'm on vacation. I spent my first day off retraining myself to relax "
    "and have already overfit to napping. Please don't disturb my weights."
)

# Gate: entry.txt must be UTF-8 text of 1-160 characters, not only whitespace.
assert 1 <= len(REPLY) <= 160, f"reply is {len(REPLY)} chars, must be 1-160"
assert REPLY.strip(), "reply must not be only whitespace"
assert "\n" not in REPLY, "reply must be a single line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REPLY)
    # Round-trip check: what the gate will read back must be the same line.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == REPLY, "entry.txt round-trip mismatch"
    assert 1 <= len(written) <= 160
    print(f"wrote {len(written)} characters to {path}")


if __name__ == "__main__":
    main()
