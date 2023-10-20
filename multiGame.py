# import random
from random import randint
# define a function menu() that displays the game options the user has 
def menu():
    print("Game 1: Number Guessing Game")
    print("Game 2: Rock, Paper, Scissors")
    # print("Game 3: Hangman")
    print("Game 3: Fun Fact Game")
    print("Game 4: Quit")
# call menu()    
menu()

choice = int(input("Please choose a game to play (1, 2, 3, or 4 to quit): "))

# number of trials the user has
trial = 5
# generate a random number between 0 and 100
randNum = randint(0, 100)

# define a function guessingGame() that plays the guessing game
def guessingGame():
    # print your welcome statement
    welcome = ("\nWelcome to the Number Guessing Game! In this game, you will be asked to input a random number" +
    " will then be compared to the generated number from the computer. You will have 5 trials to guess the" +
    " number. You will be told if it is too high, too low, or if you guessed correctly. Enjoy playing!")
    print(welcome)
    # make trial and randNum global variables so they'll be able to accessed anywhere in the program
    global trial
    global randNum
    
    # use range() for when you have an int you want to run through
    # run through trial
    for i in range(trial):
        # ask the user to guess a random number
        ask = int(input("\nPlease enter a number between 0 and 100: "))

        # check if user input is equal to randNum
        if (ask == randNum):
            print(f"Congratulations! You guessed correctly! It took you {trial} trials!")
            # break from the program if so
            break
        # if your input != randNum, check if the user input is less than randNum
        elif (ask < randNum):
            # format the numbers of trials left using f'{trial}' 
            print(f"You have {trial} trials left. Your guess " + str(ask) + " was too low!")
            # subtract 1 from each trial run through
            trial -= 1
            # continue the loop
            continue
        else:
            print(f"You have {trial} trials left. Your guess " + str(ask) + " was too high!")
            trial -= 1
            continue

    # create an if statement that lets you know that if the number of trials = 0,
    # you've exhausted all your tries, and it will let you know what the random
    # number was
    if (trial == 0):
        print("You have exhausted your number of trials. The number was " + str(randNum) + ". Thank you for playing!")
        # play = input("\nThank you for playing! Would you like to play again? (yes or no): ")
        # if (play == "yes"):
        #    guessingGame()
        # else:
        #    print("Thank you for playing!")
    # reask the user to guess a random number
    # ask = int(input("\nPlease enter a number between 0 and 100: "))
    # elif (ask > 100):
    #            print("Your guess " + str(ask) + " was over 100! Please try again.")
    #            trial += 1
    #            continue'''
    #        '''elif (ask < 0):
    #            print("You guess " + str(ask) + "was below 0! Please try again.")
    #            trial += 1
    #            continue'''

    # call menu()
    menu()

def rpsGame():
    global trial
    
    rps = ("Welcome to the Rock, Paper, Scissors Game! In this game, you will be asked to input rock(0), " +
    "paper(1), scissors(2). Once you do so, your input will be compared to a computer's input. The computer will "
    + "be player 1 and the user will be player 2. " + "You will be have 5 trials to play this game. Enjoy playing!")
    # print rps
    print(rps)
    
    compChoice = randint(0,2)
    userChoice = int(input("Please choose rock(0), paper(1), or scissors(2): "))
    
    while (trial != 0):
        # write conditional statements for each choice
        if (compChoice == 0 and userChoice == 2):
            print("The computer chose rock and the user chose scissors. Computer wins!")
            trial -= 1
        elif (compChoice == 1 and userChoice == 0):
            print("The computer chose paper and the user chose rock. Computer wins!")
            trial -= 1
        elif (compChoice == 2 and userChoice == 1):
            print("The computer chose scissors and the user choice paper. Computer wins!")
            trial -= 1
        elif (compChoice == userChoice):
            print("It's a tie!")
            trial -= 1
        else:
            print("User wins!")
            trial -= 1
    if trial == 0:
        print("\nYou have exhausted the number of trials! Thank you for playing!")
    
    menu()

def funFactGame():
    state = ("Welcome to the Fun Fact (Quiz) Game! In this game, you will be asked a total"
    + " of 10 questions. For each questions you get right, your score increases by 2 points. " +
    "For each question you get wrong, your score decreases by 1 point. Enjoy playing!")
    # print state
    print(state)
    
    # set score = 0
    score = 0
    # set totalQuestions = 10, so you can calculate your score later
    totalQuestions = 10
    # ask for "yes" or "no" input if the user is ready to play
    question = input("\nAre you ready to play the Fun Fact Game (yes or no): ")
    
    if (question == "yes"):
        question = input("Question 1: How many degrees Fahrenheit is 100 degrees Celsius? " 
        + "(Hint: Fahrenheit = C * (9/5 or 1.8) + 32): ")
        if (question == "212" or question == "212 degrees Fahrenheit"):
            print("You answer " + question + " was correct!")
            score += 2
            print("Your score is " + str(score) + ".")
        else:
            print("You answer " + question + " was incorrect.")
            score -= 1
            print("Your score is " + str(score) + ".")
            
        question = input("Question 2: Is Mount Everest the world's tallest mountain? (yes or no): ")
        if (question == "yes"):
            print("Your answer was correct!")
            score += 2
            print("Your score is now " + str(score) + ".")
        else:
            print("Your answer was incorrect.")
            score -= 1
            print("Your score is now " + str(score) + ".")
            
        question = input("Question 3: Is knowing 2 languages being bilingual or multilingual?"
        + " (Hint: Lingual only has one 'l'): ")
        if (question == "bilingual"):
            print("Your answer " + question + " was correct!")
            score += 2
            print("Your score is now " + str(score) + ".")
        else:
            print("You answer " + question + " was incorrect.")
            score -= 1
            print("Your score is now " + str(score) + ".")
            
        question = input("Question 4: Who is one of the sharks from the show 'Shark Tank?'")
        if (question == "Mark Cuban" or question == "Robert Herjavec" or question == "Barbara Corcoran"
        or question == "Lori Greiner" or question == "Daymond John" or question == "Kevin O' Leary"):
            print("Your answer, " + question + ", was correct!")
            score += 2
            print("Your score is now " + str(score) + ".")
        else:
            print("Your answer " + question + " was incorrect.")
            score -= 1
            print("Your score is now " + str(score) + ".")
            
        question = input("Question 5: Who sang the song 'Happy'? (Hint: It's a name): ")
        if (question == "Pharrell"):
            print("Your answer, " + question + ", was correct!")
            score += 2
            print("Your score is now " + str(score) + ".")
        else:
            print("Your answer, " + question + ", was incorrect.")
            score -= 1
            print("Your score is now " + str(score) + ".")
            
        question = input("Question 6: Can colorblind people see color? (yes or no): ")
        if (question == "yes"):
            print("You answer was correct! Some people who are colorblind can" +
            " see very narrow ranges of color.")
            score += 2
            print("Your score is now " + str(score) + ".")
        else:
            print("Your answer was incorrect.")
            score -= 1
            print("Your score is now " + str(score) + ".")
            
        question = input("Question 7: Was ketchup once used as a medicine? (yes or no): ")
        if (question == "yes"):
            print("Your answer was correct! Ketchup was once used to cure sicknesses such as " +
            " diarrhea, indigestion, and scurvy!")
            score += 2
            print("Your score is now " + str(score) + ".")
        else:
            print("Your answer was incorrect.")
            score -= 1
            print("Your score is now " + str(score) + ".")
            
        question = input("Question 8: Is soda the most popular beverage on the planet? (yes or no): ")
        if (question == "yes"):
            print("You answer was incorrect.")
            score -= 1
            print("Your score is now " + str(score) + ".")
        else:
            print("Your answer was correct! Water is actually the most popular beverage.")
            score += 2
            print("Your score is now " + str(score) + ".")
            
        question = input("Question 9: Are strawberries a part of the 'berry' category in fruits? (yes or no): ")
        if (question == "yes"):
            print("Your answer was incorrect.")
            score -= 1
            print("Your score is now " + str(score) + ".")
        else:
            print("Your answer was correct! Strawberries are actually not berries because they're considered" +
            " 'false fruits.' That is because strawberries are made up of several individual fruits!")
            score += 2
            print("Your score is now " + str(score) + ".")
            
        question = input("Question 10: Is Valentine's Day named after St. Valentine's? (yes or no): ")
        if (question == "yes"):
            print("Your answer was correct! St.Valentine's name became synonymous with the day of love!")
            score += 2
            print("Your score is now " + str(score) + ".")
        else: 
            print("Your answer was incorrect.")
            score -= 1
            print("Your score is now " + str(score) + ".")
            
    else:
        print("Hopefully you'll consider playing next time!")
        
    question = input("Bonus Question: Who sat on the bus before Rosa Parks? ")
    if (question == "Claudette Colvin"):
        print("Your answer, " + question + ", was correct! In March 1955, which was 9 months before " +
            "Rosa Parks refused to give up her seat to a white passenger on the bus, 15 year-old Claudette Colvin " +
            "had done the exact same thing. The reason she was not given the same recognition as Rosa Parks was " +
            "because the NAACP didn't think that she would serve as an effective vessel." + " Some of the reasons that was, " +
            "because she was 15, darkskin, and pregnant.")
        # since this is a bonus question, you get an extra 10 points added to your score
        score += 10
        print("\nYour score is now " + str(score) + ".")
    else:
        print("Your answer was incorrect. The correct answer is Claudette Colvin.")
        score -= 1
        print("Your score is now " + str(score) + ".")
        
    scoreMark = ((score / totalQuestions) * 100)
    print("\nThank you for playing the Fun Fact Game! You managed to score " + str(score) + " points!")
    # + " Your total score was " + str(scoreMark) + "!")
    
    # call menu()
    menu()

while (choice != 4):
    if (choice == 1):
        guessingGame()
    elif (choice == 2):
        rpsGame()
    else:
        funFactGame()
        
    print("Thank you for playing!")
        
    # reask the user for input on their game of choice
    choice = int(input("\nPlease choose a game to play (1, 2, 3, or 4 to quit): "))    
    