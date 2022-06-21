def lil(string):
    file1 = open("gpa.txt", "w")
    file1.write(string)
    file1 = open("gpa.txt", "r")
    G = file1.read()
    if string in G:
        print( 'Found In File')
    else:
	    print( 'Not Found')

    file1.close()
lil("Gud mrng")