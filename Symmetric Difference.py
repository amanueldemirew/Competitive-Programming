a, b = (int(input()), (input().split()))
c, d = (int(input()), (input().split()))
x = set(b)
y = set(d)
z = x ^ y
out = []
for r in z:
    out.append(int(r))
n = len(out)
for i in range(n):

    min = i

    for j in range(i+1, n):
        if out[min] > out[j]:
            min =j
    out[i], out[min] = out[min], out[i]
for t in out:

    print(t)