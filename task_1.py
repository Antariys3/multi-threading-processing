import threading


def even_numbers():
    for i in range(1, 21):
        if not i % 2:
            print(f"Even: {i}")


def odd_numbers():
    for i in range(1, 21):
        if i % 2:
            print(f"Odd: {i}")


if __name__ == "__main__":
    even_thread = threading.Thread(target=even_numbers)
    odd_thread = threading.Thread(target=odd_numbers)

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()
