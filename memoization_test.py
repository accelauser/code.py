from functools import wraps
import sys
from time import perf_counter

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):    
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args,**kwargs )
        return cache[key]
    return wrapper

@memoize
def fibonacci(n):
    list = [0,1]
    for x in range (2,n):
        list.append(list[x-1] + list[x-2]) 
    return list


if __name__ == '__main__':
    start = perf_counter()
    f = fibonacci(1000)
    end = perf_counter()

    print(len(f))
    print(f'Time: {end-start} seconds')

'''
1000
Time: 0.00041405899992241757 seconds

1000
Time: 0.00019042499934585067 seconds


'''