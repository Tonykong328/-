a = [1,2,3,4,8,13,21,34,55,89]
b = [1,2,3,4,55,6,7,8,9,10,11,12]
def common(a,b):
    c = []
    
    for i in a:
        if i in b:
            c.append(i)
    newc = set(c)
    return c
    
print(common([1,2,3,4,8,13,21,34,55,89],[1,2,3,4,55,6,7,8,9,10,11,12]))