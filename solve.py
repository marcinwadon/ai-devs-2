import sys

from task import solve

def main(taskName: str):
    solve(taskName)

    print("Done")

if __name__ == '__main__':
    main(sys.argv[1])

