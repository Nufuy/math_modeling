def my_func(a=1, b=0):    #a=1 and b = 0 eto znacheniya po ymolchaniyu
    x = 3 * a - b
    return x

def my_func(*args):
    x = 3 * args[0] - args[1]
    return x

print(my_func(3, 4))



def my_func(**kwrgs):  #**kwrgs - clovar
    x = 3 * kwrgs['obj_1'] - kwrgs['obj_2']
    return x

print(my_func(obj_1=3, obj_2=4))
print(my_func(obj_1=3, obj_2=4, obj_3=8))