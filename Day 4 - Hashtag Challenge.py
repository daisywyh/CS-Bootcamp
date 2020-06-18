# More complex version
size = int(input("how large?\n"))
    for x in range(size):
	for y in range(size):
	    print("#", end=" ")
	print("\n", end = "")

# More simple version
size = int(input("how large?\n"))
    for x in range(size):
	print("")
	#as the print version automatically prints a new line
	#we can just use the 
	for y in range(size):
	    print("#", end=" ")
