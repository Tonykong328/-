
def biggerthan(nlist,big):
    
    for i in nlist:
        if i < big:
            return(False)
    return(True)
         
a = biggerthan([3,1,1], 2)
print(a)
