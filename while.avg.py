def avg_ele():
    g = [1,11,17,28,-1,6]
    p = len(g)
    i = 0
    s = 0
    while i < p :
        s = s+g[i]
        i = i+1
    print("sum of elements in a list:",s)
    print("average of g:",s/p)
avg_ele()