from collections import deque
n = int(input())
d = deque()
for i in range(n):
    func = input()
    if func == "pop":
        d.pop()
    elif func == "popleft":
        d.popleft()
    else:
        met, val = func.split(" ")
        if met == "append":
            d.append(val)
        else:
            d.appendleft(val)


print(*d)
