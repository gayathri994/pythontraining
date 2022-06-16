
def largest(g):
    c = 0
    for i in g :
        if i > c :
            c = i
    return c
if largest([1,11,17,28,-1,6])==28:
    print("test passed")
else:
    print("test failed")
if largest([1,11,8,-1,6,7])==11:
    print("test1 passed")
else:
    print("test1 failed")
