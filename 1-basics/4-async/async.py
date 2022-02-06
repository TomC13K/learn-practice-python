import asyncio
import time


async def await_coroutine():
    print(f"started - {time.strftime('%X')}")
    print("Hello")
    await asyncio.sleep(2)  # time in SECONDS !!!!
    print("World")
    print(f"finished - {time.strftime('%X')}")


# TASKS - runs/schedule coroutines concurrently
async def say_after(delay, text):
    await asyncio.sleep(delay)
    print(text)

async def tasks():
    task1 = asyncio.create_task(
        say_after(2, "concurrent Hello")
    )
    task2 = asyncio.create_task(
        say_after(3, "concurrent World")
    )


    print(f"started - {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished - {time.strftime('%X')}")


asyncio.run(await_coroutine())
asyncio.run(tasks())
