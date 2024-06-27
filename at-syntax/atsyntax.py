#!/usr/bin/env python3

import os

def output(input):
    if not input.lstrip().startswith("@"):
        return input

    parts = input.strip()[1:].split()
    if len(parts) == 1:
        return input

    return f'Call tool {parts[0]} with "{" ".join(parts[1:])}"'

print(output(os.getenv("INPUT", "")))
