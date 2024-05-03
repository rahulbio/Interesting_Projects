import random
print("Welcome to The Number guessing game!🤔🤔🤔")
print("Im thinking of a number between 1 and 100")
guessed_num=random.randint(1,100)
choice=input("Choose a difficulty. Type 'easy' or 'hard': ")
if choice.lower()=="easy":
    no_of_choices=10
    print(f"You have {no_of_choices} chances to guess the number! ")
    while(no_of_choices>0):
        guess=int(input("Make a guess: "))
        if(guess==guessed_num):
            print("Congrats! You have guessed the number!🎉🎉🍾")
            break
        elif(guess>guessed_num):
            print("Too high⬆️")
            print("Guess again!")
            no_of_choices-=1
            print(f"You have {no_of_choices} left! ")
        elif(guess<guessed_num):
            print("Too low⬇️")
            print("Guess again!")
            no_of_choices-=1
            print(f"You have {no_of_choices} left! ")
            if(no_of_choices==0):
                print(f"Gameover! The number was {guessed_num}😓")
elif choice.lower()=="hard":
    no_of_choices=5

    print(f"You have {no_of_choices} chances to guess the number! ")
    while(no_of_choices>0):
        guess=int(input("Make a guess: "))
        if(guess==guessed_num):
            print("Congrats! You have guessed the number!🎉🎉🍾")
            break
        elif(guess>guessed_num):
            print("Too high⬆️")
            print("Guess again!")
            no_of_choices-=1
            print(f"You have {no_of_choices} left! ")
        elif(guess<guessed_num):
            print("Too low⬇️")
            print("Guess again!")
            no_of_choices-=1
            print(f"You have {no_of_choices} left! ")
            if(no_of_choices==0):
                print(f"Gameover! The number was {guessed_num}😓")