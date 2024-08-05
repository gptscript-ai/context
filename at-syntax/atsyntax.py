#!/usr/bin/env python3

from gptscript import get_env


def output(input):
    if not input.lstrip().startswith("@"):
        return input

    parts = input.strip()[1:].split()
    if len(parts) == 1:
        return f'Call the tool "{parts[0]}" with defaultPromptParameter as empty'

    return f'Call the tool "{parts[0]}" with defaultPromptParameter as exactly "{" ".join(parts[1:])}"'


print(output(get_env("INPUT")))
