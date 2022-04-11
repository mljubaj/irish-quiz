print("Hello Player!")

name = input("What is your name? ")

print(f"Welcome to the Irish quiz, {name.capitalize()}! The quiz is made of two parts. First part are YES or NO questions. You will see the correct answers after you finish all questions.\n Second part of the quiz are questions with 3 possible answers. (A, B or C)\n The game is NOT case sensitive. :) When you are ready, please write 'yes'.\n Good luck {name.capitalize()}!")

ready = input(f"Are you ready to play {name.capitalize()}? (YES/NO) ")
if ready.upper() != "YES":
    quit()
else:
    print(f"Let's start, {name.capitalize()}!")

answer1 = input("Dublin is the capital of the Republic of Ireland. (YES/NO) ")
answer2 = input("Ireland is island made of two countries. (YES/NO) ")
answer3 = input("The Irish name for Ireland is Eire. (YES/NO) ")
answer4 = input("Republic of Ireland has one official language. (YES/NO) ")
answer5 = input("The official currency of Republic of Ireland is pound. (YES/NO) ")
correct_answers = [answer1, answer2, answer3]
incorrect_answers = [answer4, answer5]

score = 0

for answer in correct_answers:
    if answer.upper() == "YES":
        print("Correct! :) ")
        score += 1
    else:
        print("Incorrect! :( ")

for answer in incorrect_answers:
    if answer.upper() == "NO":
         print("Correct! :) ")
         score += 1
    else:
        print("Incorrect! :( ")

print(f"{name.capitalize()} scored {score} out of 5 points.")

go_ahead = input("Do you want to continue? (YES/NO) ")

if go_ahead.upper() == "NO":
    print(f"{name.capitalize()} solved {(score/10)*100} % of the quiz. ")
    print(f"Goodbye {name.capitalize()}!")
    quit()
else:
    print(f"Great {name.capitalize()}! Let's continue!")


        
