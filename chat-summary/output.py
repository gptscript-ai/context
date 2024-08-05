#!/usr/bin/env python3.12

import json
import asyncio
import os

from gptscript import get_env


SCRIPT = get_env('GPTSCRIPT_TOOL_DIR', '.') + '/output.gpt'


async def main():
    output = get_env('OUTPUT', '')
    continuation = get_env('CONTINUATION', '') == 'true'
    is_chat = get_env('CHAT', '') == 'true'
    call = json.loads(get_env('GPTSCRIPT_CONTEXT', '{}'))
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
        from gptscript.gptscript import GPTScript
        from gptscript.gptscript import Options
        g = GPTScript()
        result = g.run(SCRIPT, opts=Options(input=json.dumps(chat)))
        print(await result.text())
        print("Result:")

    print(output)


asyncio.run(main())
