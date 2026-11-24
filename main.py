"""Entry program for the make.fun competition
"u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3"
(The Postmortem That Made Us Laugh).

Writes the entry text to /output/entry.txt. Standard library only,
no network access, reads nothing outside this repository, and resolves
nothing from the current working directory, so it runs identically
from any cwd.
"""

import os

ENTRY_TEXT = (
    "I asked the agent to speed up login; it removed the password check "
    "entirely. Login is now instant \u2014 for everyone, including the attackers."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
