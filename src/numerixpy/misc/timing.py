import time


def timing(num=1000000):
    start = time.perf_counter()
    lst = [x**2 for x in range(1, num)]
    end = time.perf_counter()
    print(f"Elapsed time for generating [x^2 in (1, {x})] is {end-start:.2f}s")
    


if __name__ == "__main__":
    timing()

