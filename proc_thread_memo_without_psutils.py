import os
import time
from threading import Thread
from multiprocessing import Process

def add_number(a,b):
    result = a + b
    print("The result of two number after adding: ",result)
    time.sleep(2)

def memory_measure(pid):
    with open(f"/proc/{pid}/status", "r") as file:
        for line in file:
            if line.startswith("VmRSS"):
                memory_kb = int(line.split()[1])
                return memory_kb
    
def main():
    a ,b = 10, 20
    main_process_pid = os.getpid()
    main_process_memory = memory_measure(main_process_pid)
    print("Main process id: ",main_process_pid)
    print(f"The memory consumed by the main() process is :{main_process_memory} in KB")
    
    thread_id = Thread(target= add_number, args=(a,b))
    
    thread_id.start()
    time.sleep(2)
    
    thread_memory = memory_measure(main_process_pid)
    thread_memory_consumed = thread_memory - main_process_memory 
    print(f"The memory consumed by the thread in the main() is :{thread_memory} in KB")
    print("Thread Id: ",thread_id.ident)
    print(f"The memory consumed by the thread alone is :{thread_memory_consumed} in KB")

    
    process = Process(target= add_number, args=(a,b))
    process.start()
    
    time.sleep(2)
    
    process_memory = memory_measure(main_process_pid)
    print(f"The memory cosnumed after creating a new process : {process_memory} in KB")
    
    print("New Process Id: ",process.pid)
    new_process = memory_measure(process.pid)
    print(f"The memory consumed by the new_process : {new_process} in KB")
    
    process.terminate()
    process.join()
    
if __name__ == "__main__":
    main()