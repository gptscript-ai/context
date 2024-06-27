#!/usr/bin/env python3

import json
import sys
import os

context = json.loads(os.environ.get('GPTSCRIPT_CONTEXT', '{}'))
chat = []

call = context.get('call', {})
agents = call.get('agentGroup', [])
currentAgent = call.get('currentAgent', {}).get('toolID','')

if len(agents) == 0:
    sys.exit(0)

print(f"You have the following ({len(agents)}) agents available to you:")

for agent in agents:
    if agent.get('toolID', '') == currentAgent:
        continue
    named = agent.get('named', '')
    tool = context.get('program').get('toolSet').get(agent.get('toolID'))
    print(f'\t@{named} - {tool.get("description","")}\n')
