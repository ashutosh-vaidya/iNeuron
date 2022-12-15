from multiprocessing import Process as pr
from datetime import datetime as dt
import time
import random

def process_one():
    print(f"Starting process one... {dt.now()}")
    time.sleep(random.randint(1,5))
    print(f"Stopping process one... {dt.now()}")
    
def process_two():
    print(f"Starting process two... {dt.now()}")
    time.sleep(random.randint(1,5))
    print(f"Stopping process two... {dt.now()}")
    
def process_three():
    print(f"Starting process three... {dt.now()}")
    time.sleep(random.randint(1,5))
    print(f"Stopping process three... {dt.now()}")

if __name__ == "__main__":
    p1 = pr(target = process_one)
    p2 = pr(target = process_two)
    p3 = pr(target = process_three)
    
    p1.start()
    p2.start()
    p3.start()
    
    p1.join()
    p2.join()
    p3.join()  