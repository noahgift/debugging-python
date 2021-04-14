# var=1
# var=var


def add(x, y):
    #import pdb;pdb.set_trace()
    result = x + y
    print(f"This is the x: {x}, y: {y} and this is the result: {result}")
    return result

def double():
    xx = add(1,1)
    yy = add(2,2)
    return xx+yy

print(add(1, 1))
print(double())
