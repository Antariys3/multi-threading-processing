import threading

data = list(range(1, 100001))
global_sum = 0


# A function that calculates the sum of the squares of the elements in an array
def compute_sum(start, end):
    global global_sum
    local_sum = sum(x * x for x in data[start:end])

    with sum_lock:
        global_sum += local_sum


sum_lock = threading.Lock()

if __name__ == "__main__":
    # number of threads
    num_threads = 4
    chunk_size = len(data) // num_threads

    threads = []
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else len(data)
        thread = threading.Thread(target=compute_sum, args=(start, end))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print(f"Total sum of squares: {global_sum}")
