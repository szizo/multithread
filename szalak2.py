from multiprocessing import Lock, Process, Queue, current_process
import time
import queue # imported for using queue.Empty exception
import math
import os
from datetime import datetime

def do_job(tasks_to_accomplish, tasks_that_are_done,primes,blocksize):
    while True:
        try:
            
            '''    try to get task from the queue. get_nowait() function will 
                raise queue.Empty exception if the queue is empty. 
                queue(False) function would do the same task also.
            '''
            task = tasks_to_accomplish.get_nowait()
        except queue.Empty:

            break
        else:
            '''
                if no exception has been raised, add the task completion 
                message to task_that_are_done queue
            '''
            def rosta(bs,kor):
                eredm=[]
                def IsPrime(n):
                    prime=True
                    if n>17 :
                        maximum=int(math.sqrt(n))+1
                    else:
                        maximum=n

                    for i in  primes:
                        if n>maximum : break
                        if n%i==0:
                            prime=False
                            break
                    return prime
                print((kor-1)*bs+1-kor*bs,__name__)
                for pr in  range((kor-1)*bs+1,kor*bs,2):
                    if IsPrime(pr):eredm.append(pr)   
                return eredm

            tmp=rosta(blocksize,task)
            tasks_that_are_done.put(tmp)
            time.sleep(.5)
    return True


def main():
    primes=[2,3,5,7,11,13,17]
    blocksize=1
    for i in primes:blocksize=blocksize*i
    number_of_task = 5
    number_of_processes = 5
    tasks_to_accomplish = Queue()
    tasks_that_are_done = Queue()
    processes = []
    def IsPrime(n):
        prime=True
        if n>17 :
            maximum=int(math.sqrt(n))+1
        else:
            maximum=n
        for i in  primes:
            if i>maximum :break
            if n%i==0:
                prime=False
                break
        return prime
    for pr in range(21,blocksize+1,2):
        if IsPrime(pr):primes.append(pr)
    #print(primes)

    
    for i in range(1,number_of_task+1):
        tasks_to_accomplish.put(i)

    # creating processes
    for w in range(number_of_processes):
        p = Process(target=do_job, args=(tasks_to_accomplish, tasks_that_are_done,primes,blocksize))
        processes.append(p)
        p.start()
    
    # completing process
    for p in processes:
        print("qwe")
        p.join()
    print('asd')
    # print the output
    while not tasks_that_are_done.empty():
        print(tasks_that_are_done.get()[0])

    return True


if __name__ == '__main__':
    main()