'''
Author: Temidayo Akinyemi
Date: September 27, 2023 - 
Program: MultiGameGUI.py
Description: Create a python program where the user has an 3 options for game buttons:
1. Number Guessing Game, 2. Rock, Paper, Scissors, or 3. Fun Fact Game. Each game will have a 
separate button that the user will click in order to open a new window that will play the game.
'''
# import all widgets and modules that are available in tkinter and ttk module
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
# import random
from random import randint

class mainWindow(tk.Tk):
    
    def __init__(self):
        
        super().__init__()
        
        self.geometry('690x600')
        self.title('MultiGame')
        self.config(background = '#F2D4CC')

        titleLabel = ttk.Label(self, text = "Welcome to the Multigame!", style = 'Main.TLabel')
        titleLabel.place(relx = 0.5, rely = 0.1, anchor = 'center')

        chooseLabel = ttk.Label(self, text = "Choose Your Game", style = 'Main.TLabel')
        chooseLabel.place(relx = 0.5, rely = 0.21, anchor = 'center')

        # button that allows user to choose game 1: Number Guessing Game
        game1PlayButton = ttk.Button(self, text = "Number Guessing Game", width = 23, style = 'Main.TButton',
        command = self.game1ButtonClicked)
        # game1PlayButton.bind("<Button>", lambda e: game1Window(master))
        game1PlayButton.place(relx = 0.5, rely = 0.35, anchor = 'center')

        # button that allows the user to choose game 2: Rock, Paper, Scissors
        game2PlayButton = ttk.Button(self, text = "Rock, Paper, Scissors", width = 23, style = 'Main.TButton', command = "")
        # , height = 2
        # , font = ('courier', 15, 'bold'),
        # bg = '#FF99FF', fg = 'black', width = 23, height = 2, command = "")
        game2PlayButton.place(relx = 0.5, rely = 0.45, anchor = 'center')

        # button that allows the user to choose game 3: Fun Fact Game
        game3PlayButton = ttk.Button(self, text = "Fun Fact Game", width = 23, style = 'Main.TButton', command = "")
        # , height = 2
        # font = ('courier', 15, 'bold'),
        # bg = '#FF99FF', fg = 'black', width = 23, height = 2, command = "")
        game3PlayButton.place(relx = 0.5, rely = 0.55, anchor = 'center')

        # button that allows the user to choose game 4: Create Shapes
        game4PlayButton = ttk.Button(self, text = "Create a Shape", width = 23, style = 'Main.TButton', command = "")
        game4PlayButton.place(relx = 0.5, rely = 0.65, anchor = 'center')

        # button that allows the user to choose game 5: Tic-Tac-Toe
        game5PlayButton = ttk.Button(self, text = "Tic-Tac-Toe", width = 23, style = 'Main.TButton', command = "")
        game5PlayButton.place(relx = 0.5, rely = 0.75, anchor = 'center')

        # button that allows you to exit the window
        exitButton = ttk.Button(self, text = "Exit Game", width = 10, style = 'Main.TButton', command = exit)
        # , height = 2
        # font = ('courier', 15, 'bold'),
        # bg = 'light blue', fg = 'black', width = 10, height = 2, command = exit)
        exitButton.place(relx = 0.5, rely = 0.9, anchor = 'center')

        # create a style object
        self.style = ttk.Style(self)
        # how to add color to a ttk button
        self.style.theme_use('alt')
        # this adds style for the the Labels and will be named 'TLabel' as that's the name for common ttk widget
        # classes
        self.style.configure('Main.TLabel', font = ('courier', 20, 'bold'), background = '#F2D4CC')
        # style for the buttons
        self.style.configure('Main.TButton', height = 3, font = ('courier', 15, 'bold'), background = '#FF99FF',
        foreground = 'black')
        # used for if the buttons are active 
        self.style.map('Main.TButton', background = [('active', '#d3d3d3')])
        
    # function that is called when the 'Back to Menu' button is clicked on game1Window
    def game1ButtonClicked(self):
        self.new = game1Window()
        
    # def game2ButtonClicked(self):
    #     self.new = game2Window()

class game1Window(Toplevel):
    
    def __init__(self):
        
        super().__init__() # master = master
        self.title("Number Guessing Game")
        self.geometry("720x600")
        self.config(background = '#99FFCC')
        
        # create variable sVar that holds your StringVar() which holds string data 
        # that is able to be retrieved
        self.sVar = StringVar()
        
        # create variable iVar that holds your IntVar() which holds int data
        # that is able to be retrieved
        self.iVar = IntVar()
        
        # create variable trial and set equal to 1
        self.trial = 1
        
        # create variable total and set it equal to 5
        self.total = 5
        
        # create variable randNum and set equal to the range of 0 to 100
        self.randNum = randint(0, 100)
        
        # labels, entries, and buttons for game1Window
        
        # title label
        self.nLabel = ttk.Label(self, text = 'Number Guessing Game', style = 'g1.TLabel')
        self.nLabel.place(relx = 0.5, rely = 0.1, anchor = 'center')
        
        # startLabel that is constantly updated based on the entry of the number guessed after the user 
        # clicks 'Guess Number'
        self.startLabel = ttk.Label(self, text = "Click on Start Game", style = 'start.TLabel') # font size 15
        self.startLabel.place(relx = 0.5, rely = 0.65, anchor = 'center')
        
        # startButton allows you to start the guessing game
        self.startButton = ttk.Button(self, text = 'Start Game', style = 'g1.TButton', command = self.guessNum)
        self.startButton.place(relx = 0.35, rely = 0.9, anchor = 'center')
        
        # backButton allows you to exit the game1Window and return to the mainWindow
        self.backButton = ttk.Button(self, text = 'Back to Menu', style = 'g1.TButton', command = self.destroy)
        self.backButton.place(relx = 0.65, rely = 0.9, anchor = 'center')
        
        # guessNumButton allows you to guess a number a get a result on whether it was too high,
        # too low, or if you got it correct
        # set the state of guessNumButton back to 'diabled' so the user won't be able to get headstart before 
        # they press 'Start Game'
        self.guessNumButton = ttk.Button(self, text = 'Guess Number', style = 'guess.TButton', state = 'disabled', command = self.guessingGame)
        self.guessNumButton.place(relx = 0.35, rely = 0.5, anchor = 'center')
        
        # entry that allows user to input number guess
        self.guessEntry = ttk.Entry(self, style = 'g1.TEntry', textvariable = self.sVar)
        self.guessEntry.place(relx = 0.65, rely = 0.5, anchor = 'center')
        
        # label that lisst the directions of the game
        self.welcomeLabel = ttk.Label(self, text = "Welcome to the Number Guessing Game! " +
        "\nIn this game, you will be asked to input a random number" +
        "\nwhich will then be compared to the generated number from " +
        "\nthe computer. You will have 5 trials to guess the number. " +
        "\nYou will be told if it is too high, too low, \nor if you guessed correctly. " +
        "\nEnjoy playing!", style = 'welcomeLabel.TLabel') # in order to put a border around a label, have height, width, borderwidth, and
        # relif = 'solid' attributes set
        self.welcomeLabel.place(relx = 0.5, rely = 0.3, anchor = 'center')
        
        # create a style object 
        self.style = ttk.Style(self)
        
        # style for labels
        self.style.configure('g1.TLabel', font = ('courier', 25, 'bold'), background = '#99FFCC')
        # style for buttons 
        self.style.configure('start.TLabel', font = ('courier', 15, 'bold'), background = '#99FFCC')
        self.style.configure('g1.TButton', font = ('courier', 15, 'bold'), background = '#006600', foreground = 'black',
        width = 12)
        self.style.configure('guess.TButton', font = ('courier', 13, 'bold'), background = '#006600', foreground = 'black',
        width = 12)
        # style for entry(ies)
        self.style.configure('g1.TEntry', font = ('courier', 15), width = 15)
        # welcomeLabel style
        self.style.configure('welcomeLabel.TLabel', font = ('courier', 13, 'bold'), background = '#99FFCC',
        borderwidth = 2, width = 60, height = 5, relief = 'solid')
        
    # function that updates the start label by telling the user the game directions
    def updateResult(self, text):
        self.startLabel.configure(text = text)
        
    # function that's able to enable the Guess Number button and allow the user to begin guessing
    def guessNum(self):
        # set the button back to 'normal' once the user clicks 'Start Game'
        self.guessNumButton.config(state = 'normal')
        
        self.iVar = IntVar()
        self.sVar = StringVar()
        
        self.trial = 1
        self.total = 5
        self.randNum = randint(0, 100)
        
        # set the text of updateResult
        self.updateResult(text = "Guess a random number between 0 and 100")
        
        # use the delete function to delete the entry after the user guessed the number correctly
        # or after the trials are finished
        # set it to start at 0 (index of the first number or letter), 'end' (function decides where
        # the entry ends)
        self.guessEntry.delete(0, END)
        # self.guessEntry.insert(0, self.result)
        
    # make trial and randNum global variables inside of setting them to a value inside of the function because those values will
    # reset everytime the function gets called
    # trial = 1
    # randNum = randint(0, 100)
    # total = 5
    
    # function that plays the guessing game
    def guessingGame(self):
        self.iVar = IntVar()
        self.sVar = StringVar()
        
        # global trial
        # global randNum
        # global total
        
        # call trial from the previous function guessNum() because when the game runs in this function, it won't reset to
        # its original value
        
        print(self.trial)
        
        self.trialRun = self.total - self.trial
        
        # since self.guessEntry textvariable is equal to the StringVar(), get the value of the input in the entry and
        # convert to an int
        self.ask = int(self.guessEntry.get()) 
        # print("TESTING POINT")
        # print(self.ask)
        # print("AFTER THE TESTING POINT")
        
        # set the outer statement to run as long as trial doesn't equal 5
        if (self.trial != 5):
            # if your input doesn't equal randNum, check if the user input is less than randNum
            if (self.ask < self.randNum):
                # self.askN = str(self.ask)
                # format the numbers of trials left using f'{trial}'
                # try to formay using .format() instead
                self.result = (f"Trial {self.trial}. " + f"\nYour guess {self.ask} was too low!" +
                f"\nYou have {self.trialRun} trials left.")
                # (f"You have {self.trial} trials left. " +
                # "\nYour guess " + self.ask + " was too low!")
                # subtract 1 from each trial run
                # print("TESTING POINT 1")
                self.trial += 1
                print(self.trial)
                print("TRIALS LEFT")
                print(self.trialRun)
                # print("AFTER TESTING POINT 1")
                # print("RANDOM NUMBER")
                # print(self.randNum)
                
            # if user input is greater than randNum
            elif (self.ask > self.randNum):
                self.result = (f"Trial {self.trial}. \nYour guess {self.ask} was too high!" +
                f"\nYou have {self.trialRun} trials left.")
                # (f"You have {self.trial} trials left. " + 
                # "\nYour guess " + self.ask + " was too high!")
                # print("TESTING POINT 2")
                self.trial += 1
                print(self.trial)
                print("TRIALS LEFT")
                print(self.trialRun)
                # print("AFTER TESTING POINT 2")
                # print("RANDOM NUMBER")
                # print(self.randNum)
                
                # if user input is equal to randNum
            else:
                # self.trialRun = self.total - self.trial
                self.result = ("Congratulations! You guessed " + str(self.randNum) + " correctly!" + 
                f"\nYou only used {self.trialRun} trials! \nClick on 'Start Game' to play again or " + 
                "\n'Back to Menu' to return to the main menu.")
                # (f"Congratulations! You guessed {self.randNum} correctly! " +
                # f"\nIt took you {self.trial} trials! Click on 'Start Game' " + 
                # "\nto play again or 'Back to Menu' to return to the main menu.")
                # if you guessed correctly, set the state of the guessNumButton back to 'disbaled'
                self.guessNumButton.configure(state = 'disabled')
                
        # if the trial reaches zero and you haven't correctly guessed randNum
        else:
            self.result = ("Sorry! You have exhausted the number of trials! " + f"\nThe number was {self.randNum}. "
            + "\nThank you for playing!" + "\nClick on 'Start Game to play again or 'Back to Menu' " + 
            "\nto return to the menu.")
            # print("RANDOM NUMBER" + self.randNum)
            # if you exhaust all your trials, set the state of guessNumButton back to 'disabled'
            self.guessNumButton.configure(state = 'disabled')
            
        # update the result with the text of the condition that gets looped through
        self.updateResult(self.result)
            
        # btn = Button(self, text = "Click to Return to the Main Window", command = self.destroy)
        # btn.pack(pady = 10)
        
# class game2Window(Toplevel):
        
# runs the mainWindow
if __name__ == "__main__":
    master = mainWindow()
    master.mainloop()