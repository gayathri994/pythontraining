def less_than_and_odd():
    g = [1,11,7,8,-1,6]
    b = 10
    print("value that u need to check less than",b)
    c = []
    for i in g :
        if i<=b and i%2==1 :
            c.append(i)
    print("elements less than and odd for given value")
    print(c)
    print("no.of elements that are less than and odd")
    print(len(c))
less_than_and_odd()