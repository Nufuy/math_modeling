def my_func(a, b):
    x1 = 3*a - 2*b
    x2 = 5*b - 4*a
    return x1, x2
    	
tmp = my_func(3, 2)

print(tmp)
print(tmp[0])
print(tmp[1])

print(my_func(3, 2)[1])

def crutoi_chuvak(a=1, b=1, c=1):
    a = 'Pofig'
    b = 'Pofig'
    print('Куртой чувак')
    
crutoi_chuvak()
 
help(crutoi_chuvak)
