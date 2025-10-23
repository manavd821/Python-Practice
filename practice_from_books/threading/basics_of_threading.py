import threading
import time

start = time.perf_counter()

def do_something(name="",delay=2):
    print(f"Thread {threading.current_thread().name} is starting. {name}")
    time.sleep(delay)
    print(f"Thread {threading.current_thread().name} is finishing. {name}")
    
threads = [] 
for i in range(5):
    thread = threading.Thread(target=do_something, name=f"Worker-{i+1}", args=['Manav'], kwargs={'delay' : 2})
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
end = time.perf_counter()
print(round(end-start, 2))
