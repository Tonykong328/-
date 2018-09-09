def hhhhcount(a, b):
    result = 0
    for i in a:
        if i==b:
            result=result+1
    return result

result = hhhhcount([1,4,6,7,4],4)
print (result)