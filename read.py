import sys

from task import read

def main(taskName: str):
    read(taskName)

    print("Done")

if __name__ == '__main__':
    main(sys.argv[1])

