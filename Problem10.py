from UsefulFunctions import allPrimesBelow
import time


start = time.time()
print(sum(allPrimesBelow(2000000)))
end = time.time()
print(end - start)
