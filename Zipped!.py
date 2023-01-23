n, x = map(int, input().split(" "))
d = []
for i in range(x):
    d.append(list(map(float, input().split())))

z = zip(*d)
print(list(z))
for j in z:
    print(j)
    print(sum(j)/x)

