import timeit

loops = 1000000

setup = "from utils.pagination import Paginator" 
res = timeit.repeat('Paginator(2147483647,147483647,3,3).paginate()', setup=setup, number=1, repeat=loops)

# timeit in microseconds
# convert it to milliseconds (10**-6)

print("{} loops, best result: {} milliseconds".format(loops, min(res)/(10**-6)))