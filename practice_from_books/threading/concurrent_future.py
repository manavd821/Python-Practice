import concurrent.futures
import time
start = time.perf_counter()

def do_something(name="",delay=2):
    print(f"Thread is starting. {name}")
    time.sleep(delay)
    print(f"Thread is finishing. {name}")
    return f"Ha - {name}"
    
with concurrent.futures.ThreadPoolExecutor(max_workers=100, thread_name_prefix='thread-') as executor :
    # f1 = executor.submit(do_something, "1", 2)
    secs = [5,4,3,2,1]
    
    # results = [executor.submit(do_something, i, i) for i in secs]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    
    results = executor.map(do_something, secs, secs)
    for r in results:
        print(r)

end = time.perf_counter()
print(round(end-start, 2))
