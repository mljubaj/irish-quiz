print("Hello Player!")

name = input("What is your name? ")

print(f"Welcome to the Irish quiz, {name.capitalize()}! The quiz is made of YES or NO questions. You will see the correct answers after you finish all questions.\n The game is NOT case sensitive. :) When you are ready, please write 'yes'.\n Good luck {name.capitalize()}!")

def end():
    print(f"Thank you for playing, {name.capitalize()}! Goodbye!")
    quit()

ready = input(f"Are you ready to play {name.capitalize()}? (YES/NO) ")
if ready.upper() != "YES":
    end()
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
print(f"{name.capitalize()} scored {score}/5 points.")

end()

