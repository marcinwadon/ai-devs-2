import sys

from task import solve
import asyncio

async def main(taskName: str):
    await solve(taskName)

if __name__ == '__main__':
    import time
    s = time.perf_counter()
    asyncio.run(main(sys.argv[1]))
    elapsed = time.perf_counter() - s
    print(f"\n\nexecuted in {elapsed:0.2f} seconds.")

