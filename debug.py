import sys

from task import debug
import asyncio

async def main(taskName: str):
    await debug(taskName)

if __name__ == '__main__':
    import time
    s = time.perf_counter()
    asyncio.run(main(sys.argv[1]))
    elapsed = time.perf_counter() - s
    print(f"\n\nexecuted in {elapsed:0.2f} seconds.")

