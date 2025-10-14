from contextlib import contextmanager
import time
# 1st task
import os
class UploadSaver: # it does write operation
    def __init__(
        self,
        filename : str,
        overwrite : bool = True,
        ):
        self.filename = filename
        self.overwrite = overwrite
    def __enter__(self):
        if not self.overwrite and os.path.exists(self.filename):
            raise FileExistsError(f"File {self.filename} already exists.")
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self,exc_type, exc_val, exc_tb):
        if exc_tb:
            print("Exception type:", exc_type)
            print("Exception value:", exc_val)
            print("Traceback:", exc_tb)
        if self.file:
            self.file.close()

    
# 2nd task:
class MeasureExecutionTime:
    def __init__(self):
        self.start = 0.0
        self.end = 0.0
    
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, exe_type, exe_val, exe_tb):
        self.end = time.perf_counter()
        print('Execution time:', self.end - self.start)
        
# with MeasureExecutionTime():
#     with UploadSaver(filename='abc.txt') as file:
#         file.write("Manav")
        
@contextmanager
def measure_execution_time():
    start = time.perf_counter()
    try:
        yield None
    finally:
        end = time.perf_counter()
        print('Execution time:', end - start)

with measure_execution_time():
    time.sleep(1)