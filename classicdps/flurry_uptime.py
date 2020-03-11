import random
import time

chance = 0.01
r = 0.5
flurry_hits = 0
total_hits = 2_000_000
flurry = 0
start = time.time()
for i in range(total_hits):
    if random.random() < r:
        flurry = 3
    if random.random() < chance:
        flurry = 3
    else:
        if flurry:
            flurry -= 1

    flurry_hits += bool(flurry)

uptime = 100 * flurry_hits / total_hits
print(uptime)
# print("time: ", time.time() - start)

q = chance
p = 1 - chance
# print(-(p-1)*100*(p**2+p+1))
# print((1-p**3)*100)


x= (1 - p + r) *  (p ** 2 / (1 + r) ** 2 + p/(1 + r) + 1)/(r+1)
y = (p**3/(1+r)**3)
print(x*100)
print((1-y)*100)
print(x+y)
