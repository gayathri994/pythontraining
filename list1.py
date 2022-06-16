
def element_position(g,x):
    if x in g :
        return g.index(x)
    else:
        return((-1))
if element_position([1,11,7,8,-1,6],(12))==(-1):
    print("test passed")
else:
    print("test failed")
if element_position([1,11,7,8,-1,6],(-1))==4:
    print("test1 passed")
else:
    print("test1 failed")
if element_position([1,11,7,8,-1,6],(8))==3:
    print("test2 passed")
else:
    print("test2 failed")
