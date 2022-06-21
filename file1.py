def lil(string):
    string1 =" welcome "
    file1 = open("apg.txt", "w")
    file1.write(string1)
    file1 = open("apg.txt", "a")
    G = file1.write(string)
    file1 = open("apg.txt", "r")
    L = file1.read()
    print(L)
    if string in L :
        print('Found In File')
    else:
	    print('Not Found')
    file1.close()
lil("gud mrng")
