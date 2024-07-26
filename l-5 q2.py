def allocate_memory():
    try:
        memory_hog = []
        size = 10**7  

        while True:
            memory_hog.append([0] * size)
            allocated_mb = len(memory_hog) * size * 8 / 1024 / 1024
            print(f"Allocated {allocated_mb:.2f} MB of memory.")

    except MemoryError:
        print("Memory exhausted!")

if __name__ == "__main__":
    allocate_memory()
