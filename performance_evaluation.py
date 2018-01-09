import timeit
import sys

loops = 10000

if(len(sys.argv) > 1):
	loops = int(sys.argv[1])

setup = "from utils.pagination import Paginator" 
res = timeit.repeat('Paginator(2147483647,147483647,3,3).paginate()', setup=setup, number=1, repeat=loops)

# timeit is measured in microseconds
# convert it to milliseconds (10**-6)

print("{0} loops, best result: {1:.15f} milliseconds".format(loops, min(res)/(10**-6)))