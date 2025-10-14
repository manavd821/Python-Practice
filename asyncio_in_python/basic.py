import asyncio
from datetime import datetime
import time
from concurrent.futures import ProcessPoolExecutor

def fetch_data(param):
    print(f"Start something with {param}",flush=True)
    time.sleep(param)
    print(f"End with {param}", flush=True)
    return f"Result of {param}"

async def main():
    start = datetime.now()
    task1 = asyncio.create_task(asyncio.to_thread(fetch_data, 1))
    task2 = asyncio.create_task(asyncio.to_thread(fetch_data, 2))
    result1 = await task1
    print("Thread 1 fully completed")
    result2 = await task2
    print("Thread 2 fully completed")

    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as executor:
        task1  = loop.run_in_executor(executor, fetch_data, 1)
        task2  = loop.run_in_executor(executor, fetch_data, 2)
        
        result1 = await task1
        print("Process 1 fully completed")
        result2 = await task2
        print("Process 2 fully completed")
        
    end = datetime.now()
    return [result1, result2, (end-start).seconds]

if __name__ == "__main__":
    t1 = time.perf_counter()
    results = asyncio.run(main())
    print(results)
    t2 = time.perf_counter()
    print(f"finished in {t2-t1:.2f} seconds")