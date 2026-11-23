#!/usr/bin/env python3
"""Dad joke entry for make.fun's "Dad Joke Showdown" bounty.

Writes a single original dad joke to /output/entry.txt (or to the path
in ENTRY_OUTPUT when set, for local testing). Pure standard library only.

The joke was chosen after drafting several candidates against the judge's
five criteria (a dad joke a father would tell, a pun that lands cleanly on
first read, freshness, tight wording with the punchline at the end, and a
rhythm that reads naturally aloud):

- Pencil / draw the line: "My daughter asked why I always carry a pencil.
  I said, 'In case I need to draw the line somewhere.'" THE WINNER. A
  real question-and-answer dad joke: the setup is a child's innocent
  question, and the punchline turns the idiom "draw the line" into a
  literal reason to carry a pencil. The pun is understood instantly,
  the joke is tight (99 characters), the punchline lands last, and it
  reads aloud exactly like a father answering across the dinner table.
- Bakery / doughnut holes: "I asked the bank for a loan to open a bakery.
  They said my plan had too many holes in it -- I told them that's the
  whole point of a doughnut." Clean pun, but the bakery-loan setup is
  long for its payoff and the doughnut-holes turn is a familiar pairing.
- Wi-Fi / Martin Router King: "I renamed our Wi-Fi 'Martin Router King'
  -- now the whole family has to say his name before they can get
  online." Cute, but the pun is a known Wi-Fi-name gag rather than a
  fresh joke, and the setup does more work than the punchline.
- Elevator / pushing my buttons: "I told my son the elevator is just a
  room that can't decide which floor it wants to be on. He's been pushing
  my buttons ever since." Two half-puns competing with each other; the
  ending is a shrug, not a punchline.

Set aside without drafting: "Hi hungry, I'm dad", the scarecrow award,
the tomato blushing, the two-tired bicycle, the fog ("I mist"), the
broken pencil ("pointless"), the calendar's numbered days, and the
moon going through a phase -- all classics the judge has heard a
thousand times, all failing the freshness criterion before the first word.
"""

import os
from pathlib import Path

ENTRY = (
    "My daughter asked why I always carry a pencil. "
    "I said, 'In case I need to draw the line somewhere.'"
)


def validate(entry: str) -> None:
    """Raise ValueError unless entry is 1-200 non-blank characters."""
    if not (1 <= len(entry) <= 200) or not entry.strip():
        raise ValueError("entry must be 1-200 non-blank characters")


def main() -> None:
    entry = ENTRY.rstrip("\n")
    validate(entry)
    output_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
