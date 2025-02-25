Player=input("Do you want to play the game?")
if(Player=="Yes"):
    print("Let's start the game!!!!")
    print( "*********************")

questions = (
    "What is the chemical formula of water?",
    "What is the chemical formula of table salt?",
    "What is the pH of pure water?",
    "What type of chemical bond is formed by the sharing of electrons?",
    "Which gas is commonly used in balloons and airships because it is lighter than air?",
    "Which metal is liquid at room temperature?")

options = (
    ("A. H₂O", "B. CH₄", "C. CHO", "D. OH"),
    ("A. H₂O", "B. NaCl", "C. CHO", "D. OH"),  
    ("A. 5", "B. 9", "C. 7", "D. 12"),
    ("A. Ionic Bond", "B. Hydrogen Bond", "C. Metallic Bond", "D. Covalent Bond"),
    ("A. Hydrogen", "B. Nitrogen", "C. Helium", "D. Oxygen"),
    ("A. Lead", "B. Aluminium", "C. Silicone", "D. Mercury"))

answers = ("A", "B", "C", "D", "C", "D")  

score3 = 0
question_num = 0

for question in questions:
    print("----------------------------")
    print(question)
    
    for option in options[question_num]:
        print(option)
    
    select = input("Enter the option: ").strip().upper()  
    
    if select == answers[question_num]:
        print("The option is correct")
        score3 += 1
    else:
        print("The option is incorrect")
        print(f"The correct answer is {answers[question_num]}")  

    question_num += 1
print("_____________________________________________")
score=0
Question=input("Which organ is used for respiration?\n"
                 "A. Lungs\n"
                 "B. Intestine\n"
                 "C. Stomach\n"
                 "D. Liver\n").strip().capitalize() 
Z="Lungs" 
if (Question in Z or Z in Question or sum(a == b for a, b in zip(Question, Z)) >= 3):    
    print("The answer is correct")
    print("----------------------------------")
    score +=1

else:
    print("You answer is wrong")
    print("The correct answer is Lungs")
    print("----------------------------------")

Question=input("Which organ is used for Nutrient absorption?\n"
                 "A. Lungs\n"
                 "B. Intestine\n"
                 "C. Stomach\n"
                 "D. Liver\n").strip().capitalize()
Q="Intestine"
if (Question in Q or Q in Question or sum(a == b for a, b in zip(Question, Q)) >= 3):  
    print("The answer is correct")
    print("----------------------------------")
    score +=1
else:
    print("You answer is wrong")
    print("The correct answer is Intestine")
    print("----------------------------------")

Question=input("Which organ is used for thinking?\n"
                 "A. Lungs\n"
                 "B. Intestine\n"
                 "C. Brain\n"
                 "D. Liver\n").strip().capitalize()
G="Brain"
if (Question in G or G in Question or sum(a == b for a, b in zip(Question, G)) >= 3):  
    print("The answer is correct")
    print("----------------------------------")
    score +=1
else:
    print("The correct answer is Brain")
    print("----------------------------------")

Question=input("Which fluid circulate the oxygen to whole body?\n"
                 "A. Blood\n"
                 "B. Intestine\n"
                 "C. Stomach\n"
                 "D. Liver\n").strip().capitalize()
M="Blood" or "A" or "a"
if (Question in M or M in Question or 
    sum(a == b for a, b in zip(Question, M)) >= 3):  
    print("The answer is correct")
    print("----------------------------------")
    score +=1
else:
    print("You answer is wrong")
    print("The correct answer is Blood")
    print("----------------------------------")

Question=input("Which organ is used for digestion ?\n"
                 "A. Lungs\n"
                 "B. Intestine\n"
                 "C. Stomach\n"
                 "D. Liver\n").strip().capitalize()
N="Stomach"
if (Question in N or N in Question or sum(a == b for a, b in zip(Question, N)) >= 3):  
    print("The answer is correct")
    print("----------------------------------")
    score +=1
else:
    print("You answer is wrong")
    print("The correct answer is Stomach")
    print("----------------------------------")

Question=input("Which organ is used for storing vitamins?\n"
                 "A. Lungs\n"
                 "B. Intestine\n"
                 "C. Stomach\n"
                 "D. Liver\n").strip().capitalize()
J="Liver"
if (Question in J or J in Question or sum(a == b for a, b in zip(Question, J)) >= 3):  
    print("The answer is correct")
    print("----------------------------------")
    score +=1
else:
    print("You answer is wrong")
    print("The correct answer is Liver")
    print("----------------------------------")



score2=0
Question=int(input("Solve for x:2X+5=17 ?\n"
                 "A. 9\n"
                 "B. 5\n"
                 "C. 6\n"
                 "D. 7\n"))
if (Question==7):  
    print("The answer is correct")
    print("----------------------------------")
    score2 +=1
else:
    print("You answer is wrong")
    print("The correct answer is 7")
    print("----------------------------------")

Question=int(input("A train travels 240 km in 4 hours. What is its average speed?\n"
                 "A. 60 km/h\n"
                 "B. 35 km/h\n"
                 "C. 90 km/h\n"
                 "D. 88 km/h\n"))
if (Question==60):  
    print("The answer is correct")
    print("----------------------------------")
    score2 +=1
else:
    print("You answer is wrong")
    print("The correct answer is 60")
    print("----------------------------------")

Question=int(input("What is the value of 8!/6!?\n"
                 "A. 60 \n"
                 "B. 35 \n"
                 "C. 90 \n"
                 "D. 56\n"))
if (Question==56):  
    print("The answer is correct")
    print("----------------------------------")
    score2 +=1
else:
    print("You answer is wrong")
    print("The correct answer is 56")
    print("----------------------------------")

Question=int(input("If a triangle has angles 50° and 60°, what is the third angle?\n"
                 "A. 60°  \n"
                 "B. 30°  \n"
                 "C. 90°  \n"
                 "D. 70° \n"))
if (Question==70):  
    print("The answer is correct")
    print("----------------------------------")
    score2 +=1
else:
    print("You answer is wrong")
    print("The correct answer is 70°")
    print("----------------------------------")

Question=int(input("Find the area of a rectangle with length 12 cm and width 8 cm.\n"
                 "A. 96 cm² \n"
                 "B. 86 cm² \n"
                 "C. 85 cm² \n"
                 "D. 45 cm²\n"))
if (Question==96):  
    print("The answer is correct")
    print("----------------------------------")
    score2 +=1
else:
    print("You answer is wrong")
    print("The correct answer is 96 cm² ")
    print("----------------------------------")

Question=input("Who discovered the Pythagorean Theorem ?\n"
                 "A. Pythagoras\n"
                 "B. Euclid\n"
                 "C. Archimedes\n"
                 "D. Srinivasa Ramanujan\n").strip().capitalize()
C="Pythagoras"
if (Question in C or C in Question or sum(a == b for a, b in zip(Question, C)) >= 3):  
    print("The answer is correct")
    print("----------------------------------")
    score2 +=1
else:
    print("You answer is wrong")
    print("The correct answer is Pythagores")
    print("----------------------------------")
print("__________________________________")
print(f"Your Score for Biology is {score} out of 6")
a=(score/6)*100
c=int(a)
print(f"The percentage of your performmance for Biology is {c}%")
print("___________________________________")
print(f"Your Score for Mathematics is {score2} out of 6")
a=(score2/6)*100
c=int(a)
print(f"The percentage of your performmance for Mathematics is {c}%")
print("____________________________________")
print(f"Your Score for Chemistry is {score3} out of 6")
a=(score3/6)*100
c=int(a)
print(f"The percentage of your performmance for Chemistry is {c}%")
print("__________________________________________")

d=score+score2+score3
print("Your overall score is",d)
e=(d/18)*100
f=int(e)
print(f"The overall percentage for your performmance is {f}%")

print("___________________________")
if (score>=4):
    print("Good luck")
    print("You have high score in biology")
else:
    print("You need to concentrate on Biology")
    print("Try again")
print("___________________________")
if(score2>=4):
    print("Good luck")
    print("You have high score in Mathematics")
else:
    print("You need to concentrate on Mathematics")
    print("Try again")
print("___________________________")
if (score3>=4):
    print("Good luck")
    print("You have high score in Chemistry")
else:
    print("Try again")
    print("You need to concentrate on Chemistry")
print("_________________________________________")











