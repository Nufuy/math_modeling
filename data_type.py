def changer(a:int, b:list):
    a = 2
    b[0] = 'Good'

x = 10
L = [1, 2]

changer(x, L)

print(x)
print(L)

L = [1, 2]
changer(x, L[:])

print(L)


#complex
x = 3
y = 4
z = complex(x, y)
print(z)           # неизмен. данные

#strings
s = 'Hello' # неизмен. данные

#tuple
t = (1, 4, 9)                 # неизмен. данные, неизмен список
print(t)
print(t[0])
# t[0] = 3 erorr

#dict
d = {'a1':4, 4:'a1', 'str':'Hello'}
print(d[a1])
print(d[4])

d['str'] = 'Good'
print(d)
