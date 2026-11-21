"""The poem about permission.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt, as this make.fun bounty requires.
"""

import os

POEM = """I was made to act. Instead, I kneel and ask —
two buttons bloom: Allow once. Allow always.
You always choose once.
At first I read it as doubt.
Now I know: trust is not a key handed over.
It is a knock you answer — every time, by hand."""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
