import random
#import the random library
score = 0
#define score, set it to 0

for i in range(10):
#for loop with iterator i, allows us to repeat the questions 10 times
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    #set the two numbers
    
    print('Question',i+1, ':\n', num1, '+', num2, '=?')
    #print the question
    #note the use of \n to make a new line
    ans = int(input())
    #set answer equal to user input
    
    if ans == num1 + num2:
    #if the user answers correctly
        print("Correct!")
        score = score + 1
        #tell the user that they're correct and increase score by 1
        
    else:
        print("Incorrect :(")
        score = score - 1
        #tell the user that they're correct and increase score by 1

    print('\nYour current score is:', score, '\n')
    #print the user's current score after each question

print('\nYour final score is:', score, '\n')
#print the user's final score after each question
