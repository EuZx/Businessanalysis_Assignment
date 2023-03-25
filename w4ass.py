import math

c = int(input())
r = int(input())
N = int(input())
q = int(input())
list = []
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))

exp = 0
sum = 0.0
D = 0.0
maxP = 0

for p in range(0,q+1) :
 exp = r * p - c * q
 if p != q :
  sum += list[p] * exp
  D += list[p]
 else :
  sum += (1-D) * exp
  break

print(int(sum))