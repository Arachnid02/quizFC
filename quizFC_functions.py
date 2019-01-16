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
                return ansU
                check = True
            #if the user input is not the correct answer...
            else:
                #check to see if it is an acceptable answer, and if it is then
                #give neutral feedback, and DON'T increment the SCORE variable,
                #and set the escape condition for the while loop to True
                if "`" < ansU < "e":
                    print("Got your answer choice!")
                    return ansU
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
    if grade < 70:
        print("Nice attempt, but you failed the quiz. :(")
    elif grade == 70:
        print("Good job! You barely passed the quiz :)")
    elif 80 < grade < 100:
        print("Great job!. You passed the quiz :)")
    else:
        print("Frantastic! You passed the quiz with flying colors! :)")

#delcaration of a programmer defined function. Will require a value for the
        #parameter (showAnsCheck)
def show_ans(showAnsCheck):
    while showAnsCheck == False:
        #stores the user input into the variable showAns as a string, and
        #convert the string into uppercase
        showAns = str(input("""\nDo you want to see the correct
answers? Type Y for Yes, or N for No.\n"""))
        showAns = showAns.upper()
        #if the user selected Y, to view the correct answers, print out the
        #correct answer for each question
        if showAns == "Y":
            showAnsCheck = True
            print("Question 1:\nCorrect Answer:", q0CorAns,
                  "\n\nQuestion 2:\nCorrect Answer:", q1CorAns,
                  "\n\nQuestion 3:\nCorrect Answer:", q2CorAns,
                  "\n\nQuestion 4:\nCorrect Answer:", q3CorAns,
                  "\n\nQuestion 5:\nCorrect Answer:", q4CorAns,
                  "\n\nQuestion 6:\nCorrect Answer:", q5CorAns,
                  "\n\nQuestion 7:\nCorrect Answer:", q6CorAns,
                  "\n\nQuestion 8:\nCorrect Answer:", q7CorAns,
                  "\n\nQuestion 9:\nCorrect Answer:", q8CorAns,
                  "\n\nQuestion 10:\nCorrect Answer:", q9CorAns)
        #if the user selected N, to skip the option to view the correct answers,
        #provide feedback that program understands input, and exit
        elif showAns == "N":
            print("Okay, the correct answer choices will not be shown.")
            showAnsCheck = True
        #if the user didn't enter either Y or N, prompt them for input again,
        #and provide instructions
        else:
            print("""Sorry, that input is invalid. Your input needs to be
either the letter Y for Yes or N for No.""")

