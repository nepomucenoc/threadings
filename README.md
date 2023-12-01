# threadings
This is an example of how to use Threading.
In Python, threading is a way to run multiple threads (smaller units of a program) concurrently within a single process. A thread is the smallest unit of execution, and it consists of a sequence of instructions, a program counter, and a stack. Threads within the same process share the same data space, which means they can communicate with each other more easily than processes that run in separate memory spaces.

Python provides a built-in module called threading that allows you to create and manage threads. The threading module provides a convenient way to create and start threads, synchronize access to shared resources, and perform other threading-related tasks.

## Example de Threading em Python

```python
import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

def print_letters():
    for letter in 'ABCDE':
        time.sleep(1)
        print(letter)

# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Init threads
thread1.start()
thread2.start()

# Wait finish threads
thread1.join()
thread2.join()

print("threads finished.")


In this example, two threads (thread1 and thread2) are created, and each thread executes a different function (print_numbers and print_letters). The start() method is called on each thread to initiate their execution, and the join() method is used to wait for the threads to complete before moving on.

It's important to note that Python's Global Interpreter Lock (GIL) can limit the effectiveness of threading for CPU-bound tasks. In such cases, the multiprocessing module, which uses separate processes rather than threads, maybe a better choice. However, threading can be effective for I/O-bound tasks or tasks that involve waiting for external resources.
