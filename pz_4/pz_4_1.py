import random
N = random.randrange(1,11)
K = random.randrange(1,11)
print("N = ",N)
print("K = ",K)
print()
s = 0
for i in range(1,N+1):
p = 1.0
for j in range(1,K+1):
p *= i
s += p
print("i = ",i)
print("p = ",p)
print("s = ",s)
print()
print("Sum = ",s)
