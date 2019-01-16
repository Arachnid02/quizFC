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
run_quest(q0, ansU, q0CorAns, check)
run_quest(q1, ansU, q1CorAns, check)
run_quest(q2, ansU, q2CorAns, check)
run_quest(q3, ansU, q3CorAns, check)
run_quest(q4, ansU, q4CorAns, check)
run_quest(q5, ansU, q5CorAns, check)
run_quest(q6, ansU, q6CorAns, check)
run_quest(q7, ansU, q7CorAns, check)
run_quest(q8, ansU, q8CorAns, check)
run_quest(q9, ansU, q9CorAns, check)

#calls the function cal_score and provides an argument to fulfill the function's
#parameters
cal_score(grade)

#calls the function show_ans and provides an argument to fulfill the function's
#parameters
show_ans(showAnsCheck)
