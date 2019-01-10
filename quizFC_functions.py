from quizFC_data import *

global SCORE

def run_quest(quest, ansU, ansC, check):
    while check == False:
        try:
            ansU = str(input(quest))
            ansU = ansU.lower()
            if ansU == ansC:
                print("Got your answer choice!")
                global SCORE
                SCORE += 1
                check = True
            else:
                if "`" < ansU < "e":
                    print("Got your answer choice!")
                    check = True
                else:
                    print("""Please enter a letter that is between the letters
A and D.\n""")
        except ValueError:
            print("""Please enter a letter. Select your answer choice by putting
in the letter that precedes your answer choice.""")

def cal_score(grade):
    grade = SCORE * 10
    print("Your grade is: ", grade)
