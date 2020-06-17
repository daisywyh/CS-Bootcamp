import turtle
s = turtle.getscreen()
t = turtle.Turtle()
#import turtle and initialise the screen and the turtle

shape_list = ["triangle", "square", "Triangle", "Square"]
#create a list of shapes that we want to draw

def custom_triangle(length):
    for x in range(3):
        t.forward(length)
        t.right(120)
#create the function to create a triangle with custom dimensions

def custom_square(length):
    for x in range(4):
        t.forward(length)
        t.right(90)
#create the function to create a square with custom dimensions

shape_choice = input("What would you like to draw? " +  str(shape_list[0:2]))
#ask the user what shape they would like to draw

x = True
#set x as true so the while loop runs
while x:
    if shape_choice in shape_list:
    #check their shape choice is in the list
        thickness = input("What thickness would you like your lines to be?")
        '''
        ask users about line thickness and set thickness to that
        note: i have not turned thickness into an integer because i want to make sure that
        people entered actual numbers, which i check in the next while loop
        if people enter string and I try to convert to integer, the program will crash
        '''
        x = False
        #break the loop by setting x as false
        
    else:
        print("Please input a valid answer.")
        shape_choice = input("What would you like to draw? " +  str(shape_list[0:2]))
        #tell users to make sure their input is valid, and redo input

x = True
#set x as true so the while loop runs
while x:
    if thickness.isdigit():
        #if the thickness is a digit
        thickness = int(thickness)
        #turn thickness into integer
        if thickness < 11 and thickness > 0:
            t.pensize(thickness)
            #set line thickness as specified
            size = input("How long should the sides be?")
            #ask user how long sides should be
            x = False
            #break loop by setting x as false
        else:
            print("Make sure pen thickness is between 1-10")
            #prompt user on why their input is unvalid
            thickness = input("What thickness would you like your lines to be?")
            #prompt user to redo input
    else:
        print("Make sure pen thickness is an integer")
        #prompt user on why their input is unvalid
        thickness = input("What thickness would you like your lines to be?")
        #prompt user to redo input

x = True
#set x to true to run while loop
while x:
    size = str(size)
    if size.isdigit():
    #check if size is an actual integer
    #change to string so i can use .isdigit method
        size = int(size)
        #change size back to integer
        x = False
        #if size is integer, just carry on with program
    else:
        print("Make sure length is a positive integer")
        #prompt user on why their input is wrong
        size = input("How long should the sides be?")
        #prompt user to redo input

'''
note the use of conditional statements to check whether not user input is valid
before converting data types. doing so ensures that the program does not crash due to
invalid feedback from the user.
'''

if shape_choice == "Triangle" or shape_choice == "triangle":
    custom_triangle(size)
    #if the user chooses triangle, draw a triangle with the specified side lengths

elif shape_choice == "Square" or shape_choice == "square":
    custom_square(size)
    #if the user chooses square, draw a triangle with the specified side lengths
