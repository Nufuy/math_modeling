c = 1
b = 1
c = b
a = int(input())
for i in range(a):
    print(b)
    c , b = b, c + b
    