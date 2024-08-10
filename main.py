import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        COMMAND = str(input())

        match COMMAND:
            case 'exit 0':
                break

        if COMMAND.startswith('echo'):
            message = COMMAND.split("echo")[1]
            print(message)
        
        else:
            print(f'{COMMAND}: command not found')


if __name__ == "__main__":
    main()
