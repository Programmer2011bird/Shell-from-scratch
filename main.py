import sys
import os


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        COMMAND = str(input())
        COMMANDS_LIST: list[str] = ["echo", "exit", "exit 0", "type", "PATH"]

        match COMMAND:
            case 'exit 0':
                break

            case 'PATH':
                PATH = os.environ.get("PATH").split(";")

                for index, path in enumerate(PATH):
                    print(f"{index} : {path}")

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
            print(f'{COMMAND}: command not found')

if __name__ == "__main__":
    main()
