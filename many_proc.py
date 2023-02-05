from time import time
from multiprocessing import Pool
import os

def enumerate(number):
    index = 1
    result = []
    while index <= number:
        if number % index == 0:
            result.append(index)
        index +=1
    return(result)

if __name__ == '__main__':
    A = (128, 255, 99999, 10651060)
    res = []
    print('Number of processors ' + str(os.cpu_count()))
    start = time()
    with Pool(os.cpu_count()) as pool:
        res = pool.map(enumerate, A)
    end = time() - start
    print(end)
    for i in res:
        print(i)

