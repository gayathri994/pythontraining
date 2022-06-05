def largest_even():
    g = [1,11,17,28,-1,6]
    largest = 0
    for i in g :
        if i > largest and i%2==0 :
            largest = i
    print(largest)
largest_even()

