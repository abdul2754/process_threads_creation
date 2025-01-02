import os
import time
from threading import Thread
from multiprocessing import Process
import psutil

def add_number(a,b):
    result = a + b
    print("The result of two number after adding: ",result)
    time.sleep(2)

def memory_measure(pid):
    proc = psutil.Process(pid) 
    return proc.memory_info().rss
    
def main():
    a ,b = 10, 20
    main_process_pid = os.getpid()
    main_process_memory = memory_measure(main_process_pid)
    
    print(f"The memory consumed by the main() process is :{main_process_memory / 1024:.2f} in KB")
    
    thread_id = Thread(target= add_number, args=(a,b))
    
    thread_id.start()
    time.sleep(2)
    
    thread_memory = memory_measure(main_process_pid)
    thread_memory_consumed = thread_memory - main_process_memory 
    print(f"The memory consumed by the thread in the main() is :{thread_memory / 1024 :.2f} in KB")
    print(f"The memory consumed by the thread alone is :{thread_memory_consumed / 1024 :.2f} in KB")

    
    process = Process(target= add_number, args=(a,b))
    process.start()
    
    time.sleep(2)
    
    process_memory = memory_measure(main_process_pid)
    print(f"The memory cosnumed after creating a new process : {process_memory / 1024 :.2f} in KB")
    
    new_process = memory_measure(process.pid)
    print(f"The memory consumed by the new_process : {new_process / 1024 :.2f} in KB")
    
    process.terminate()
    process.join()
    
if __name__ == "__main__":
    main()