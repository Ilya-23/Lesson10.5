import multiprocessing
import time
from multiprocessing import Pool
def read_info(name):
    all_data = []
    with open(name, encoding='utf-8') as file:
        str1 = file.readlines()
        all_data.append(str1)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

"""time_start = time.time()
for i in filenames:
    read_info(i)
time_end = time.time()
print(time_end - time_start)"""


if __name__ == '__main__':
    time_start1 = time.time()
    with Pool(processes=4) as pool:
        process1 = pool.map(read_info, filenames)
    time_end1 = time.time()
    print(time_end1 - time_start1)