
def char(g,f):
    count = 0
    for i in g:
         if(i==f) :
               count = count+1
    return count
if char("abcdefmnacyxh",("a"))==2:
    print("test passed")
else:
    print("test failed")
