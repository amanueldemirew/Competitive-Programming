import re

n = int(input())

for i in range(n):
    st = input()
    try:
        re.compile(st)
        print(True)
    except:
        print(False)
