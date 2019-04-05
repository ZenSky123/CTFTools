from pyfiglet import Figlet
import re
import os
from collections import defaultdict

print(Figlet(font='slant').renderText('CTF_Scripts'))

script_path_hook = {}
help_hook = defaultdict(list)
dictionaries = ('coding', 'crypto', 'misc')

for dictionary in dictionaries:
    for *_, filenames in os.walk(dictionary):
        for filename in filenames:
            if filename.endswith('.py'):
                script_name = '.'.join(filename.split('.')[:-1])
                script_path = os.path.join(dictionary, filename)

                help_hook[dictionary].append(script_name)
                script_path_hook[script_name] = script_path


def help():
    for dictionary, scripts in help_hook.items():
        print(dictionary)
        [print('\t', script) for script in scripts]


command_pattern = re.compile(r'(\S*) (.*)')

while 1:
    command = input('>>> ').strip()
    if command.startswith('help'):
        help()
    elif any([command.startswith(exit_initial) for exit_initial in ('quit', 'q', 'exit')]):
        break
    else:
        try:
            script_name, args = command_pattern.match(command).groups()
            if script_name in script_path_hook:
                script_path = script_path_hook[script_name]
                os.system(' '.join(('python3', script_path, args)))
        except:
            pass
