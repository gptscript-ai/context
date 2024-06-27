#!/usr/bin/env python3.12

import json
import os
import asyncio
from gptscript.gptscript import GPTScript
from gptscript.gptscript import Options


SCRIPT = os.getenv('GPTSCRIPT_TOOL_DIR', '.') + '/output.gpt'


async def main():
    output = os.environ.get('OUTPUT', '')
    continuation = os.environ.get('CONTINUATION', '') == 'true'
    is_chat = os.environ.get('CHAT', '') == 'true'
    call = json.loads(os.environ.get('GPTSCRIPT_CONTEXT', '{}'))
    chat = []

    for message in call.get('completion', {}).get('messages', []):
        role = message.get('role', '')
        text = [part['text'] for part in message.get('content', []) if 'text' in part]
        if role == 'user' or role == 'assistant' and len(text) > 0:
            chat.append({
                'role': role,
                'message': ' '.join(text)
            })

    if is_chat and not continuation and len(chat) > 1:
        g = GPTScript()
        result = g.run(SCRIPT, opts=Options(input=json.dumps(chat)))
        print(await result.text())
        print("Result:")

    print(output)


asyncio.run(main())
