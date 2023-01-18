from collections import Counter
x = int(input())
a = list(map(int,input().split(" ")))
n = int(input())

ava = Counter(a)
res = 0

for i in range(n):
    x,y =  list(map(int,input().split(" ")))
    if ava[x]>0:
        res+=y
        ava[x]-=1
    else:
        res+=0
print(res)