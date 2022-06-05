def less_than_or_equal():
    g = [1,11,7,8,-1,6]
    b = -2
    print("value that u need to check less than",b)
    c = []
    for i in g :
        if i<=b :
            c.append(i)
    print("elements less than given value")
    print(c)
    print("number of elements that are less than given number")
    print(len(c))
less_than_or_equal()
