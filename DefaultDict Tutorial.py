from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    inp = input().rstrip()
    d[inp].append(i+1)
for i in range(m):
    inp = input().rstrip()
    if inp in d:
        print(*d[inp])
    else:
        print("-1")





