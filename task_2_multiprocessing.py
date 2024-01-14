import multiprocessing


# A function that calculates the sum of the squares of the elements in an array
def compute_sum(start, end, result):
    local_sum = sum(x * x for x in data[start:end])
    with sum_lock:
        result.value += local_sum


if __name__ == "__main__":
    data = list(range(1, 100001))
    num_processes = 4

    global_sum = multiprocessing.Manager().Value("i", 0)
    sum_lock = multiprocessing.Lock()

    chunk_size = len(data) // num_processes

    processes = []
    for i in range(num_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_processes - 1 else len(data)
        process = multiprocessing.Process(
            target=compute_sum, args=(start, end, global_sum)
        )
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"Total sum of squares: {global_sum.value}")
