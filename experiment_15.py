
import gc
import tracemalloc

tracemalloc.start()

def show_memory():
    current, peak = tracemalloc.get_traced_memory()
    print("Current Memory:", current, "bytes")
    print("Peak Memory:", peak, "bytes")

print("Initial Memory:")
show_memory()

data = []

for i in range(1000):
    x = []
    x.append(x)
    data.append(x)

print("\nMemory After Creating Objects:")
show_memory()

del data

gc.set_debug(gc.DEBUG_STATS)

print("\nGarbage Collection:")
collected = gc.collect()
print("Objects Collected:", collected)

print("\nMemory After Garbage Collection:")
show_memory()

gc.set_debug(0)

tracemalloc.stop()
