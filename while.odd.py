def odd_in_list():
    g = [1,11,7,8,-1,6]
    p = len(g)
    c = []
    i = 0
    while i < p :
        if g[i]%2==1 :
            c.append (g[i])
        i= i+1
    print("odd elements in a given value")
    print(c)
    print("number of odd elements in a given number")
    print(len(c))
odd_in_list()
