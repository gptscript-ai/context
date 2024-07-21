#!/usr/bin/env python3.12

import json
import os
import asyncio


SCRIPT = os.getenv('GPTSCRIPT_TOOL_DIR', '.') + '/summarize.gpt'


async def main():
    histories = json.loads(os.environ.get('GPTSCRIPT_CONTEXT', '{}'))
    chat = []

    for history in histories.get('history', []):
        for message in history.get('completion', {}).get('messages', []):
            role = message.get('role', '')
            text = [part['text'] for part in message.get('content', []) if 'text' in part]
            if role == 'user' or role == 'assistant' and len(text) > 0 and not text[0].startswith("Call "):
                chat.append({
                    'role': role,
                    'message': ' '.join(text)
                })

    if len(chat) > 1:
        from gptscript.gptscript import GPTScript
        from gptscript.gptscript import Options
        g = GPTScript()
        result = g.run(SCRIPT, opts=Options(input=json.dumps(chat)))
        print(await result.text())


asyncio.run(main())
