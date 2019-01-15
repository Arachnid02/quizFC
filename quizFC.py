#imporrts all data from the data module and the functions module
from quizFC_data import *
from quizFC_functions import *

print("""This is a 10 question U.S. Government and Civics quiz. There will be
four possible answers and only one of the will be correct. When selecting
your answer, enter the letter that precedes your answer choice. The program
is case insensitive, meaning it doesn't matter if your selections are done
in upper or lower case.

Try your best and good luck!\n""")

#calls the function run_quest and provides arguments to fulfill the function's
#parameters
run_quest(q0, q0Ans, q0CorAns, check)
run_quest(q1, q1Ans, q1CorAns, check)
run_quest(q2, q2Ans, q2CorAns, check)
run_quest(q3, q3Ans, q3CorAns, check)
run_quest(q4, q4Ans, q4CorAns, check)
run_quest(q5, q5Ans, q5CorAns, check)
run_quest(q6, q6Ans, q6CorAns, check)
run_quest(q7, q7Ans, q7CorAns, check)
run_quest(q8, q8Ans, q8CorAns, check)
run_quest(q9, q9Ans, q9CorAns, check)

#calls the function cal_score and provides an argument to fulfill the function's
#parameters
cal_score(grade)
