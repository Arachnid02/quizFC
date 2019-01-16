#initialize variables q0-q9 with questions
q0 = str("""1. What are the two parts of the U.S. Congress?
    a. Senate, House of Representatives
    b. FBI, CIA
    c. President, Supreme Court
    d. Department of Justice, Department of Education
Your answer: """)
q1 = str("""\n2. The House of Representatives has how many voting members?
    a. 12
    b. 100
    c. 9
    d. 435
Your answer: """)
q2 = str("""\n3. What does the judicial branch do?
    a. Federal law enforcement
    b. Write and pass new legislation
    c. Authorize military action
    d. Decide the Constitutionality of laws
Your answer: """)
q3 = str("""\n4. When must all men register for the Selective Service?
    a. At age 18
    b. At age 21
    c. At age 16
    d. At age 55
Your answer: """)
q4 = str("""\n5. What territory did the United States buy from France in 1803?
    a. The Northwest Territory
    b. The Louisiana Territory
    c. Canada
    d. Alaska
Your answer: """)
q5 = str("""\n6. Name the U.S. war between the North and the South.
    a. World War I
    b. The American Revolution
    c. The French and Indian War
    d. The Civil War
Your answer: """)
q6 = str("""\n7. Who did the United States fight in World War II?
    a. England, Germany, and Russia
    b. Japan, Germany, and Canada
    c. Japan, Germany, and Italy
    d. China, Japan, and Turkey
Your answer: """)
q7 = str("""\n8. Before he was President, Eisenhower was a general. What war did he
fight in?
    a. World War II
    b. The American Revolution
    c. The Korean War
    d. World War I
Your answer: """)
q8 = str("""\n9. During the Cold War, what was the main concern of the United States?
    a. Capitalism
    b. Energy Shortage
    c. Climate Change
    d. Communism
Your answer: """)
q9 = str("""\n10. Which is the state that borders Mexico?
    a. Oklahoma
    b. Louisiana
    c. Mississippi
    d. Arizona
Your answer: """)
#initialize q0CorAns-q9CorAns with the correct answers for the associated
#questions
q0CorAns = str("a")
q1CorAns = str("d")
q2CorAns = str("d")
q3CorAns = str("a")
q4CorAns = str("b")
q5CorAns = str("d")
q6CorAns = str("c")
q7CorAns = str("a")
q8CorAns = str("d")
q9CorAns = str("d")
#declares SCORE a global variable, meaning it can be accessed and have it's
#value changed within every module
global SCORE
SCORE = int()
grade = int ()
#initialize q0Ans-Q9Ans to hold the user's answer to each question
ansU = str("")
#initialize the check variables for run_quest and show_ans as False
check = bool(False)
showAnsCheck = bool(False)
