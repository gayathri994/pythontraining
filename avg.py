def avg_of_three(x,y,z):
     g = x+y+z
     avg=g/3
     print("avg of three elements:",avg)
     return round(avg,2)
c = avg_of_three(4,5,6)
if c == 5:
     print("test passed")
else:
     print("test failed")
c = avg_of_three(9,5,11)
if c == 8.33:
     print("test1 passed")
else:
     print("test1 failed")
c = avg_of_three(11,-3,5.5)
if c == 4.5:
     print("test2 passed")
else:
     print("test2 failed")