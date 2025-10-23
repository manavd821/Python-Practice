import multiprocessing
import time

start = time.perf_counter()

def do_something(name="",delay=2):
    print(f"{multiprocessing.current_process().name} is starting. {name}")
    time.sleep(delay)
    print(f"{multiprocessing.current_process().name} is finishing. {name}")

if __name__ == '__main__':   
    processes = [] 
    for i in range(10):
        process = multiprocessing.Process(target=do_something, name=f"Worker-{i+1}", args=['Manav'], kwargs={'delay' : 2})
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
        
    end = time.perf_counter()
    print(round(end-start, 2))
