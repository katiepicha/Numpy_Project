import time
import numpy as np
import random

start_time_list = time.time()

list1 = [random.randrange(1,7) for i in range(0, 10_000_000)]

print(f"Process finished --- {(time.time() - start_time_list)} seconds ---")


start_time_array = time.time()

array1 = np.random.randint(1, 7, 10_000_000)

print(f"Process finished --- {(time.time() - start_time_array)} seconds ---")