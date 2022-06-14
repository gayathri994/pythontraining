def less_than_or_equal(g,b):
    c = []
    for i in g :
        if i<=b :
            c.append(i)
    return len(c)
if less_than_or_equal([1,11,7,8,-1,6],(11))==6:
    print("test passed")
else:
    print("test failed")
if less_than_or_equal([1,11,7,8,-1,6],(10))==5:
    print("test1 passed")
else:
    print("test1 failed")
if less_than_or_equal([1,11,7,8,-1,6],(-1))==1:
    print("test2 passed")
else:
    print("test2 failed")
if less_than_or_equal([1,11,7,8,-1,6],(-2))==0:
    print("test3 passed")
else:
    print("test3 failed")

