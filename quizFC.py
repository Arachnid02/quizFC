q1Check = bool(False)
q1Answer = str("")
q1 = str("""1. What is the technique called by which the genome of an organism can be
split up into different sized molecules?
    a. Electrolysis
    b. Electrophrosis
    c. Chromatography
    d. None of the above\n""")

print("""This is a one question science quiz. There will be four possible answers,
and only one of them is correct. When selecting answers, enter the letter that
precedes it.\n""")

while q1Check == False:
        try:
                q1Answer = str(input(q1))
                q1Answer = q1Answer.lower()
                if q1Answer == "b":
                        print("Got your answer choice!")
                        q1Check = True
                else:
                        if "`" < q1Answer < "e":
                                print("Got your answer choice!")
                                q1Check = True
                        else:
                                print("""Please enter a letter that is between the
letters A and D.\n""")
        except ValueError:
                print("""Please enter a letter. Select your answer choice by putting in
the letter that precedes your answer choice.""")
