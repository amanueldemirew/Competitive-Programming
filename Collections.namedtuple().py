from collections import namedtuple
n = int(input())
data = namedtuple("date", input().split())
s = 0
for i in range(n):
    mark = (data(*input().split()))
    s += int(mark.MARKS)
print(s / n)
