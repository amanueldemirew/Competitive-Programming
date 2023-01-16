nums = [4,6,5,9,3,7]
l = [0,0,2]
r = [2,3,5]
n = len(l)
num = []
bol = []
out = []
n = len(l)
for i in range(n):
    s = list((nums[l[i]:r[i]+1]))
    s.sort()
    b = len(s)
    for j in range(1,b):
        if s[j] - s[j-1] == s[1] - s[0]:
            bol.append("true")
        else:
            bol.append("false")
o = 
print(bol)
