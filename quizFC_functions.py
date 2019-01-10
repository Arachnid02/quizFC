#imports all data from data module
from quizFC_data import *

#announces that the variable SCORE is a global variable, meaning it can be
#accessed within all modules
global SCORE

#declaration of a programmer defined function. Will require values for each of
#the four parameters (quest, ansU, andC, check)
def run_quest(quest, ansU, ansC, check):
    while check == False:
        #first try to get a string input from the user, if the program doesn't
        #receive a string, then skip directly to the execpt ValueError
        try:
            #stores the user input into the variable ansU as a string, and
            #convert the string into lowercase
            ansU = str(input(quest))
            ansU = ansU.lower()
            #checks to see if the user input is the correct answer, and if it is
            #then give neutral feedback and increment the SCORE variable, and
            #set the escape condition for the while loop to True
            if ansU == ansC:
                print("Got your answer choice!")
                global SCORE
                SCORE += 1
                check = True
            #if the user input is not the correct answer...
            else:
                #check to see if it is an acceptable answer, and if it is then
                #give neutral feedback, and DON'T increment the SCORE variable,
                #and set the escape condition for the while loop to True
                if "`" < ansU < "e":
                    print("Got your answer choice!")
                    check = True
                #if it isn't an acceptable answer, then give appropriate
                #feedback to the user, and providing instructions on how to
                #enter an acceptable answer
                else:
                    print("""Please enter a letter that is between the letters
A and D.\n""")
        #if the user didn't enter a string, then give them appropriate feedback,
        #and provide instructions on how to enter an acceptable answer
        except ValueError:
            print("""Please enter a letter. Select your answer choice by putting
in the letter that precedes your answer choice.""")

#declaration of a programmer defined function. Will require a value for the
#parameter (grade)
def cal_score(grade):
    #user's grade for the quiz will be their score multiplied by 10
    grade = SCORE * 10
    #print out the user's grade to them
    print("Your grade is: ", grade)
