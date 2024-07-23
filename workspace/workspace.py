import os
import sys


dir = os.environ.get('GPTSCRIPT_WORKSPACE_DIR', '')
if not os.path.isdir(dir):
    sys.exit(0)

cwd = os.getcwd()
print(f'The current working directory is: "{cwd}"')

print(f'The workspace directory is "{dir}". Use "{dir}" to create new files or directories.')

files = os.listdir(dir)
if not files:
    sys.exit(0)

files.sort()
if len(files) > 0:
    print(f'The workspace contains the following files and directories:')
    for file in files:
        if file.startswith('.'):
            continue
        if os.path.isdir(os.path.join(dir, file)):
            print(f'  {file}/')
        else:
            print(f'  {file}')
print("Always use absolute paths to interact with files in the workspace. The workspace path is not the same as the current working directory.")
print()
