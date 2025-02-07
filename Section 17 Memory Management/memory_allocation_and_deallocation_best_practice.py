import sys

a = []
print(sys.getrefcount(a))
b = a
print(sys.getrefcount(b))

## Garbage Collection
import gc

gc.enable()
# gc.disable()
print(gc.collect())

print(gc.get_stats())

## Get unreachable objects
print(gc.garbage)

"""
Memory management best practice:
1. Use local variable inside a method or class. They have shorter lifespan than global variables.
2. Avoid Circular References: This can lead to memory leaks. A->B->C->A
3. User generators: This helps keeping one item in memory.
4. Explicitly delete objects: use del to delete variable and objects explicitly
5. Profile Memory Usage: User memory profiling tools like tracemalloc and memory_profiler to identify memory leaks and optimize memory usage.
"""

# Handling circular dependency


class MyObject:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Object {self.name} deleted")


obj1 = MyObject("Obj1")
obj2 = MyObject("Obj2")

obj1.ref = obj2
obj2.ref = obj1

del obj1
del obj2

gc.collect()


# Generators for memory Efficiency
def generate_numbers(n):
    for i in range(n):
        yield i


for num in generate_numbers(10000000):
    print(num)
    if num > 10:
        break

# Profiling Memory usage with tracemalloc
import tracemalloc


def create_list():
    return [i for i in range(10000)]


def main():
    tracemalloc.start()

    create_list()

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics("lineno")

    print("[Top 10]")
    for stat in top_stats[:10]:
        print(stat)


main()
