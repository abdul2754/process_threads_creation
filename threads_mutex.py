from threading import Thread, Event, Lock
import threading
import time  

def Led_Blinking(val, i, stop,lock):
    print(f"The Thread{i} is created")
    while not stop.is_set():
        with lock:
            print(f"Led of Thread{i} is blinking")
            time.sleep(val)  
            print(f"Led of Thread{i} is not blinking")
    print(f"Thread{i} is now terminated")    

def main():
    val = float(input("Enter the time for Blinking: "))
    stop_event = []
    threads = []
    lock = Lock()
    for i in range(1, 4):
        stop = Event()
        t = Thread(target=Led_Blinking, args=(val, i, stop,lock))
        t.start()
        threads.append(t)
        stop_event.append(stop)
        time.sleep(3)  
    for s in stop_event:
        s.set() 
    
    for i in threads:
        i.join()  
    
    print("All threads are terminated!!!")

if __name__ == "__main__":
    main()
