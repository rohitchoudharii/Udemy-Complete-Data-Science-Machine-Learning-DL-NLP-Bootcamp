"""
Definitions:
1. Program: A program is a set of instructions written in a programming language to perform a specific task.
2. Process: A process is an instance of a program that is being executed. It contains the program code and its current activity.
3. Thread: A thread is the smallest unit of a process that can be scheduled for execution. It is a lightweight process that shares resources with other threads in the same process.

Examples:
1. Program:
    A Python script that prints "Hello, World!" is a program.
    ```python
    print("Hello, World!")
    ```

2. Process:
    Running the above Python script creates a process that executes the code.

3. Thread:
    A thread in Python can be created using the `threading` module.
    ```python
    def print_hello():
        print("Hello from thread")

    thread = threading.Thread(target=print_hello)
    thread.start()
    thread.join()
    ```

Process Block Diagram:
+-------+-------+------+
| Code  | Data  | Heap |
+-------+-------+------+
| Stack | Register     |
+-------+--------------+
| Single Thread        |
+----------------------+

Multi-threading Block Diagram:
+-----------------------+
| Code  | Data  |  Heap |
+-----------------------+
| Stack | Stack | Stack |
| Reg.  | Reg.  | Reg.  |
+-------+-------+-------+
| Thread| Thread| Thread|
|   1   |   2   |   3   |
+-------+-------+-------+
"""
