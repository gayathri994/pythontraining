def odd_in_list():
    g = [1,11,7,8,-1,6]
    c = []
    for i in g :
         if i%2==1 :
            c.append(i)
    print("elements less than given value")
    print(c)
    print("number of elements that are less than given number")
    print(len(c))
odd_in_list()
