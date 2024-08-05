#!/usr/bin/env python3.12

import json
from gptscript import get_env


histories = json.loads(get_env('GPTSCRIPT_CONTEXT', '{}'))
chat = []

for history in histories.get('history', []):
    completion = history.get('completion', {})
    messages = completion.get('messages', [])
    for message in messages:
        role = message.get('role', '')
        text = []
        parts = message.get('content', [])
        for part in parts:
            if 'text' in part:
                text.append(part['text'])
        
        if role == 'user' or role == 'assistant' and len(text) > 0:
            chat.append(f'{role}: {' '.join(text)}')

if len(chat) > 0:
    print(f'''
You are having a follow up conversation with a user. The previous conversation is as follows:
        
START CONVERSATION HISTORY (lines {len(chat)}):

{'\n'.join(chat)}

END CONVERSATION HISTORY:
''')