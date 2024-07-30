import os

cwd = os.getcwd()
files = os.listdir(cwd)
if len(files) == 0:
    print(f'The current working directory is "{cwd}" and contains no following files.')
else:
    files.sort()
    print(f'The current working directory is "{cwd}" and contains the following files:')
    for file in files:
        if os.path.isdir(os.path.join(cwd, file)):
            print(f'- {file}/')
        else:
            print(f'- {file}')
print()
