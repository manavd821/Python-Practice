import concurrent.futures
import time

start = time.perf_counter()

def do_something(name="", delay=2):
    print(f"Process is starting. {name}")
    time.sleep(delay)
    print(f"Process is finishing. {name}")
    return f"Ha - {name}"

if __name__ == '__main__':
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=15) as executor:
        # f1 = executor.submit(do_something, "1", 1)
        # print(f1.result())
        
        secs = [5,4,3,2,1]
        # results = [executor.submit(do_something, i, i) for i in secs]
        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())
    
        results = executor.map(do_something, secs, secs)
        for r in results:
            print(r)
            
        end = time.perf_counter()
        print(f"Finished in {round(end - start, 2)} seconds")