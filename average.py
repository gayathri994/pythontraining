def avg_ele():
    g = [1,11,17,28,-1,6]
    p = len(g)
    print("length of elements:",p)
    s = 0
    for i in g :
        s = s+i
    print("sum of elements in a list:",s)
    print("average of g:",s/p)
avg_ele()