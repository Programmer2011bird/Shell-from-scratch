import sys
import os


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        COMMAND = str(input())
        COMMANDS_LIST: list[str] = ["echo", "exit", "exit 0", "type"]

        match COMMAND:
            case 'exit 0':
                break

        if COMMAND.startswith('echo'):
            message = COMMAND.split("echo")[1]
            print(message)
        
        if COMMAND.startswith('type'):
            function = COMMAND.split("type ")[1]

            if (function in COMMANDS_LIST) == False:
                print(f'{COMMAND}: command not found')
            
            else:
                message = f'{function} is a shell builtin'

                print(message)

        if (COMMAND.split(" ")[0] in COMMANDS_LIST) == False:
            print(os.environ.get("PATH"))
            print(f'{COMMAND}: command not found')

if __name__ == "__main__":
    main()
