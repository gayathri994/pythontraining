#Write a function which return max even element in a given list
def largest_even(g):
    largest = 0
    for i in g:
        if i > largest and i%2==0 :
            largest = i
    return largest
if largest_even ([1,11,7,8,-1,6])==8:
    print("pass")
else:
    print("fail")
if largest_even ([1,11,17,28,-1,6])==28:
    print("pass")
else:
    print("fail")
