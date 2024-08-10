import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        COMMAND = str(input())

        print(f'{COMMAND}: command not found')


if __name__ == "__main__":
    main()
