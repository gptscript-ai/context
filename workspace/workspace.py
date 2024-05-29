import os
import sys


cwd = os.getcwd()
print(f'The current working directory is: "{cwd}"')

dir = os.environ.get('GPTSCRIPT_WORKSPACE_DIR', '')
if not os.path.isdir(dir):
    sys.exit(0)

print(f'The workspace directory is "{dir}". Use "{dir}" to create new files or directories.')

files = os.listdir(dir)
if not files:
    sys.exit(0)

print(f'The workspace contains the following files and directories:')
files.sort()
for file in files:
    if file.startswith('.'):
        continue
    if os.path.isdir(os.path.join(dir, file)):
        print(f'  {file}/')
    else:
        print(f'  {file}')
print()