import random
N = random.randrange(1,1000)
print('N = ', N)
K = 1
while K*K <= N:
K += 1
K -= 1
print("K = {0}, K^2 = {1}, (K+1)^2 = {2}".format(K,K**2,(K+1)**2))
