import os
import sys


dir = os.environ.get('GPTSCRIPT_WORKSPACE_DIR', '')
if not os.path.isdir(dir):
    sys.exit(0)

files = os.listdir(dir)
files.sort()
if len(files) > 0:
    print(f'The workspace directory is "{dir}" and contains the following files and directories:')
    for file in files:
        if file.startswith('.'):
            continue
        if os.path.isdir(os.path.join(dir, file)):
            print(f'- {file}/')
        else:
            print(f'- {file}')
else:
    print(f'The workspace directory is "{dir}" and contains no files.')

print("Always use absolute paths to interact with files in the workspace.")
print("Prefer creating new files in the workspace if the user does not imply a specific directory.")
print("If the user refers to '.' that is the current working directory and not the workspace directory.")
print()
