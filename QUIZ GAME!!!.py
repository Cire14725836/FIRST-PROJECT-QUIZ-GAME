import random

RED = '\033[31m'
BLUE = '\033[34m'

print(RED + "Hello Player lets play a game")

name = input("But first Player what is your name?: ")
print("")

print("Hello " + name + " nice to meet you")
print("You will be playing 3 different games that test your luck, knowledge, and skill")
print("I wish you the best of luck " + name)
print(" ")

print(BLUE + "ROUND 1 GUESS THE NUMBER")

print(RED + "You must guess the number I am thinking of!")
print("You must figure out the number in 3 attempts or less to score a point")

score = 0

attempt = int(1)

random_number = random.randint(1,10)

guess = int(input("Im thinking of a number between 1-10. Can you guess it? "))

while random_number != guess:
    if guess > random_number:
        print("To high. Try again: ")
        guess = (int(input("")))
        attempt += 1

    elif guess < random_number:
        print("To low. Try again: ")
        guess = (int(input("")))
        attempt += 1

if attempt <4:
    score += 1
    print("You did it good job!")
else:
    print(f"You got it but it took you {attempt} attempts....YOU FAIL")

print(f"Your current score is {score}")
print("")

print(BLUE + "ROUND 2 ROCK,PAPER,SCISSORS")
print(RED + "In this game we will play Rock,Paper,Scissors in a best of 3")
print("Lets see if you can beat my perfect strategy")

player_score = 0
computer_score = 0

while player_score != 2:
    user_guess = input("OK " + name +" Rock,Paper,or Scissors?: ")

    print("Computer played rock!")

    if user_guess == "paper" or user_guess == "Paper":
        print(name + " Won!")
        player_score += 1
    elif user_guess == "scissors" or user_guess == "Scissors":
        print("Computer Won!")
        computer_score += 1
    else:
        print("It was a draw!")
    if computer_score == 2:
        break

if player_score == 2:
    print("Looks like you beat my perfect strategy....")
    print("YOU WIN!")
    score += 1
else:
    print("HAHA my rock strategy always wins!")
    print("YOU LOSE")

print(f"Your current score is {score}")
print("")

print(BLUE + "FINAL ROUND KNOWLEDGE CHECK")
print(RED + "This time I will give you a topic choice between History or Science.")

choice = "_"

while choice not in ["History","history","Science","science"]:
    choice = input("So choose History or Science? ")

if choice == "History" or choice == "history":
    print("In what year did World War 2 start")
    
    print("A: 1923")
    print("B: 1975")
    print("C: 1939")
    print("D: 1948")

    hist_answer = input("Please sumbit your letter choice from the asnwers above: ")

    if hist_answer == "C" or hist_answer == "c":
        print("That is the correct answer! World War 2 started in 1939 when Hitler invaded Poland")
        print("GOOD JOB!")
        score += 1
    else:
        print("That is the wrong answer! World War 2 started in 1939 when Hitler invaded Poland")
        print("So the correct answer was C")

if choice == "Science" or choice == "science":
    print("What land animal currently has the longest tongue?")

    print("A: Giraffe")
    print("B: Chameleon")
    print("C: Ant Eater")
    print("D: Bat")

    sci_answer = input("Please sumbit your letter choice from the asnwers above: ")

    if sci_answer =="B" or sci_answer == "b":
        print("That is the correct answer! A Chameleons tongue can be up to 47 inches!")
        print("GOOD JOB!")
        score += 1
    else:
        print("That is the wrong answer! A Chameleons tongue can be up to 47 inches!")
        print("So the correct answer was B")


print("")

print(BLUE + "THE RESULTS ARE IN!")
print(RED + "Lets see how you did")

if score == 3:
    print("YOU GOT A PERFECT SCORE!!")
    print("I guess your just to smart for my game " + name)
elif score == 2:
    print("You got 2 out of 3 correct so you win!")
    print("Not bad! Not just anyone can win my game!")
elif score == 1:
    print("You got 1 out of 3 correct so you lose!")
    print("My game is pretty hard! at least you got a point tho.....")
else:
    print("YOU GOT NOTHING RIGHT!!!")
    print("Where you even trying or.....")

print(BLUE + "THANKS FOR PLAYING!!!")

leave = "_"

while leave not in ["Exit","exit"]:
    leave = input("Please type exit to leave: ")
