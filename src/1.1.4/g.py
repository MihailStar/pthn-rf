# Задача G

import re as regexp

input_g = input()

per_chan = r"(?:100|[1-9][0-9]?|0)%"
hex_chan = r"(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])"
alf_chan = r"(?:1|0\.[1-9][0-9]?|0\.0[1-9]|0)"

per_pattern = r"^rgb\(" + r",".join([per_chan, per_chan, per_chan]) + r"\)$"
hex_pattern = r"^rgb\(" + r",".join([hex_chan, hex_chan, hex_chan]) + r"\)$"
alf_pattern = r"^rgba\(" + r",".join([hex_chan, hex_chan, hex_chan, alf_chan]) + r"\)$"

pattern = r"(?:" + "|".join([per_pattern, hex_pattern, alf_pattern]) + r")"


def is_valid(color: str) -> bool:
    if regexp.match(pattern, color):
        return True

    return False


print(is_valid(input_g))
