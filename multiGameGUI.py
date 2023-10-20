'''
Author: Temidayo Akinyemi
Date: September 27, 2023 - 
Program: multiGameGUI.py
Description: Create a multigame program where the user has an option to play 1. Number Guessing Game,
2. Rock, Paper, Scissors, or 3. Fun Fact Quiz Game. Each game will have a separate that the user will 
click in order to open a new window to play the game.
'''

# import tkinter
from tkinter import *
from tkinter.ttk import *
import sys, os
# import random
from random import randint

# the purpose of the self parameter is to be the instance to which the method belongs to be passed automatically
# but not received automatically.
# first parameter of methods is the instance the method is called on

# set the class for the main window
class mainWindow():

    def __init__(self, master, title, geometry):
        self.master = master
        self.title = title
        self.geometry = geometry
        # title for mainWindow GUI
        title = ("MultiGame")
        geometry = ("690x600")
        self.master.configure(bg = '#9966cc')
        
        self.titleLabel = Label(self.master, text = "Welcome to the Multigame!", font = ('courier', 20, 'bold'),
        bg = '#9966cc')
        self.titleLabel.place(relx = 0.5, rely = 0.1, anchor = 'center')
        
        # 'ask' the user to choose a game
        self.chooseLabel = Label(self.master, text = "Choose Your Game", font = ('courier', 15, 'bold'),
        bg = '#9966cc')
        self.chooseLabel.place(relx = 0.5, rely = 0.25, anchor = 'center')
        
        # button that allows user to choose game 1: Number Guessing Game
        self.game1PlayButton = Button(self.master, text = "Number Guessing Game", font = ('courier', 15, 'bold'),
        bg = '#FF99FF', fg = 'black', width = 23, height = 2, command = self.game1GoBackButtonClicked)
        self.game1PlayButton.place(relx = 0.5, rely = 0.38, anchor = 'center')
        
        # button that allows the user to choose game 2: Rock, Paper, Scissors
        self.game2PlayButton = Button(self.master, text = "Rock, Paper, Scissors", font = ('courier', 15, 'bold'),
        bg = '#FF99FF', fg = 'black', width = 23, height = 2, command = "")
        self.game2PlayButton.place(relx = 0.5, rely = 0.5, anchor = 'center')
        
        # button that allows the user to choose game 3: Fun Fact Game
        self.game3PlayButton = Button(self.master, text = "Fun Fact Game", font = ('courier', 15, 'bold'),
        bg = '#FF99FF', fg = 'black', width = 23, height = 2, command = "")
        self.game3PlayButton.place(relx = 0.5, rely = 0.62, anchor = 'center')
        
        # button that allows you to exit the window
        self.exitButton = Button(self.master, text = "Exit Game", font = ('courier', 15, 'bold'),
        bg = 'light blue', fg = 'black', width = 10, height = 2, command = self.game1WCancel)
        self.exitButton.place(relx = 0.5, rely = 0.85, anchor = 'center')
        
    # function that is called when the 'Back to Menu' button is clicked on the game1Window
    def game1GoBackButtonClicked(self):
        new = game1Window(self, 'Number Guessing Game', '690x600')
        
    # function called when the user clicks 'Back to Menu' on game1Window
    def game1WCancel(self):
        self.master.destroy() 
    
class game1Window(Toplevel):
    
    def __init__(self, parent, title, geometry):
        super().__init__(name = "game1_main_menu")
        
        self.parent = parent
        self.title(title)
        self.geometry(geometry)
        
        # game1 title
        title = ('Number Guessing Game')
        geometry = ('690x600')
        self.configure(background = '#99FFCC')

        # create a variable guess that holds your StringVar() which holds string data
        # that is able to be retrieved
        # set iVar equal to IntVar() which holds integer data that will be able
        # to be retrieved
        self.iVar = iVar
        self.sVar = sVar
        
        self.trial = trial
        self.randNum = randNum
        
        iVar = IntVar()
        sVar = StringVar()

        # number of trials the user has
        trial = 5

        # generate a random number between 0 and 100
        randNum = randint(0, 100)
        
        # labels, entries, and buttons for game1Window
        
        # title label
        self.nLabel = Label(self, text = 'Number Guessing Game', font = ('courier', 25, 'bold'),
        bg = '#99FFCC')
        self.nLabel.place(relx = 0.5, rely = 0.1, anchor = 'center')
        
        # startLabel that is constantly updated based on the entry of the number guessed after the user 
        # clicks 'Guess Number'
        self.startLabel = Label(self, text = "Click on Start Game", font = ('courier', 15, 'bold'),
        bg = '#99FFCC')
        self.startLabel.place(relx = 0.5, rely = 0.65, anchor = 'center')
        
        # startButton allows you to start the guessing game
        self.startButton = Button(self, text = 'Start Game', font = ('courier', 15, 'bold'),
        bg = '#006600', fg = 'black', width = 10, command = self.guessNum)
        self.startButton.place(relx = 0.35, rely = 0.9, anchor = 'center')
        
        # backButton allows you to exit the game1Window and return to the mainWindow
        self.backButton = Button(self, text = 'Back to Menu', font = ('courier', 15, 'bold'),
        bg = '#006600', fg = 'black', width = 12, command = self.onCancel)
        self.backButton.place(relx = 0.65, rely = 0.9, anchor = 'center')
        
        # guessNumButton allows you to guess a number a get a result on whether it was too high,
        # too low, or if you got it correct
        # set the state of guessNumButton back to 'diabled' so the user won't be able to get headstart before 
        # they press 'Start Game'
        self.guessNumButton = Button(self, text = 'Guess Number', font = ('courier', 15, 'bold'),
        bg = '#006600', fg = 'black', state = 'disabled', command = self.guessingGame)
        self.guessNumButton.place(relx = 0.35, rely = 0.5, anchor = 'center')
        
        # entry that allows user to input number guess
        self.guessEntry = Entry(self, font = ('courier', 15, 'bold'), textvariable = sVar, width = 15)
        self.guessEntry.place(relx = 0.65, rely = 0.5, anchor = 'center')
        
        # label that lisst the directions of the game
        self.welcomeLabel = Label(self, text = "Welcome to the Number Guessing Game! " +
        "\nIn this game, you will be asked to input a random number" +
        "\nwhich will then be compared to the generated number from " +
        "\nthe computer. You will have 5 trials to guess the number. " +
        "\nYou will be told if it is too high, too low, \nor if you guessed correctly. " +
        "\nEnjoy playing!",
        font = ('courier', 13, 'bold'), bg = '#99FFCC', borderwidth = 2,
        width = 60, height = 5, relief = 'solid') # in order to put a border around a label, have height, width, borderwidth, and
        # relif = 'solid' attributes set
        self.welcomeLabel.place(relx = 0.5, rely = 0.3, anchor = 'center')
        
        # create global variables
        # trial
        # randNum
        
    # function that updates the start label by telling the user the game directions
    def updateResult(self, text):
        self.startLabel.configure(text = text)
        
    # function guessNum() that's able to enable the Guess Number button and allow
    # the user to begin guessing
    def guessNum(self):
        # set the button back to 'normal' once the user clicks 'Start Game'
        self.guessNumButton.config(state = 'normal')
        
        self.iVar = iVar
        self.sVar = sVar
        
        self.trial = trial
        self.randNum = randNum
        
        iVar = IntVar()
        sVar = StringVar()

        # number of trials the user has
        trial = 5

        # generate a random number between 0 and 100
        randNum = randint(0, 100)
        # set the text of updateResult
        self.updateResult(text = "Guess a random number between 0 and 100")
        
        # use the delete function to delete the entry after guessing the number correctly
        # or after the trials are finished
        # set it to start at 0 (index of the first number or letter), 'end' (function decides
        # where the entry ends)
        self.guessEntry.delete(0, 'end')
        
    # function guessingGmae() that plays the guessing game
    def guessingGame(self):
        # global variables
        self.iVar = iVar
        self.sVar = sVar
        
        self.trial = trial
        self.randNum = randNum
        
        iVar = IntVar()
        sVar = StringVar()

        # number of trials the user has
        trial = 5

        # generate a random number between 0 and 100
        randNum = randint(0, 100)
        
        # set ask to retrieve the string input from sVar, but convert to an int
        # variable to an integer variable becasue that it what you'll be inputting
        self.ask = ask
        ask = int(sVar.get())
        
        self.result = result
        
        # set the outer loop to run as long as trial doesn't equal 0
        if (trial != 0):
            # if your input doesn't equal randNum, check if the user input is less than randNum
            if (ask < randNum):
                # format the numbers of trials left using f'{trial}'
                result = (f"You have {trial} trials left. Your guess " +
                str(ask) + " was too low!")
                # subtract 1 from each trial run
                trial -= 1
                
            # if user input is greater than randNum
            elif (ask > randNum):
                result = (f"You have {trial} trials left. Your guess " +
                str(ask) + " was too high!")
                trial -= 1
                
                # if user input is equal to randNum
            else:
                result = (f"Congratulations! You guessed {randNum} correctly! " +
                f"\nIt took you {trial} trials! Click on 'Start Game' " + 
                "\nto play again or 'Back to Menu' to return to the main menu.")
                # if you guessed correctly, set the state of the guessNumButton back to 'disbaled'
                self.guessNumButton.configure(state = 'disabled')
                
        # if the trial reaches zero and you haven't correctly guessed randNum
        else:
            result = ("Sorry! You have exhausted the number of trials! " + "\nThe number was " + str(randNum) + ". "
            + "\nThank you for playing!" + "\nClick on 'Start Game to play again or 'Back to Menu' " + 
            "\nto return to the menu.")
            # if you exhaust all your trials, set the state of guessNumButton back to 'disabled'
            self.guessNumButton.configure(state = 'disabled')
            
        # update the result with the text of the condition that gets looped through
        self.updateResult(result)
            
    # function that goes back to the mainWindow
    def onCancel(self):
        self.destroy()
        
if (__name__ == "__main__"):
    window = Tk()
    MainWindow = mainWindow(window, "root/main/first window", "690x600")
    window.mainloop()
