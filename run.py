print("Hello Player!")

name = input("What is your name? ")

print(f"Welcome to the Irish quiz, {name.capitalize()}! The quiz is made of two parts. First part are 5 YES or NO questions. Please answer them by writing 'YES' or 'NO'. Second part of the quiz are 5 questions with 3 possible answers. Write the letter in front of the answer you want to choose. For example: 'A'. The game is NOT case sensitive. :) When you are ready, please write yes. Good luck {name.capitalize()}!")

ready = input(f"Are you ready to play {name.capitalize()}? (YES/NO) ")
if ready.upper() != "YES":
    quit()
else:
    print(f"Let's start, {name.capitalize()}!")

answer1 = input("Dublin is the capital of the Republic of Ireland. (YES/NO) ")
answer2 = input("Republic of Ireland has one official language. (YES/NO) ")
answer3 = input("The official currency of Republic of Ireland is pound. (YES/NO) ")
answer4 = input("Ireland is island made of two countries. (YES/NO) ")
answer5 = input("The Irish name for Ireland is Eire. (YES/NO) ")
correct_answers = [answer1, answer4, answer5]
incorrect_answers = [answer2, answer3]

for answer in correct_answers:
    if answer1.upper() == "YES":
        print("Correct! :) ")
    else:
        print("Incorrect! :( ")

for answer in incorrect_answers:
    if answer2.upper == "NO":
         print("Correct! :) ")
    else:
        print("Incorrect! :( ")
        
