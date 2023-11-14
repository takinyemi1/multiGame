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
from tkinter import messagebox
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
        titleLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)

        chooseLabel = ttk.Label(self, text = "Choose Your Game", style = 'Main.TLabel')
        chooseLabel.place(relx = 0.5, rely = 0.21, anchor = CENTER)

        # button that allows user to choose game 1: Number Guessing Game
        game1PlayButton = ttk.Button(self, text = "Number Guessing Game", width = 23, style = 'Main.TButton',
        command = self.game1ButtonClicked)
        # game1PlayButton.bind("<Button>", lambda e: game1Window(master))
        game1PlayButton.place(relx = 0.5, rely = 0.35, anchor = CENTER)

        # button that allows the user to choose game 2: Rock, Paper, Scissors
        
        # create a photoimage object to use an image for rock, paper, scissors
        # photo = PhotoImage(file = r'C:\Users\akiny\New folder\Code Files\Python Files\rps_img.jpg')
        
        game2PlayButton = ttk.Button(self, text = "Rock, Paper, Scissors", width = 23, style = 'Main.TButton', command = self.game2ButtonClicked)
        # , height = 2
        # , font = ('courier', 15, 'bold'),
        # bg = '#FF99FF', fg = 'black', width = 23, height = 2, command = "")
        game2PlayButton.place(relx = 0.5, rely = 0.45, anchor = CENTER)

        # button that allows the user to choose game 3: Fun Fact Game
        game3PlayButton = ttk.Button(self, text = "Fun Fact Game", width = 23, style = 'Main.TButton', command = self.game3ButtonClicked)
        # , height = 2
        # font = ('courier', 15, 'bold'),
        # bg = '#FF99FF', fg = 'black', width = 23, height = 2, command = "")
        game3PlayButton.place(relx = 0.5, rely = 0.55, anchor = CENTER)

        # button that allows the user to choose game 4: Create Shapes
        game4PlayButton = ttk.Button(self, text = "Create a Shape", width = 23, style = 'Main.TButton', command = "")
        game4PlayButton.place(relx = 0.5, rely = 0.65, anchor = CENTER)

        # button that allows the user to choose game 5: Tic-Tac-Toe
        game5PlayButton = ttk.Button(self, text = "Tic-Tac-Toe", width = 23, style = 'Main.TButton', command = "")
        game5PlayButton.place(relx = 0.5, rely = 0.75, anchor = CENTER)

        # button that allows you to exit the window
        exitButton = ttk.Button(self, text = "Exit Game", width = 10, style = 'Main.TButton', command = exit)
        # , height = 2
        # font = ('courier', 15, 'bold'),
        # bg = 'light blue', fg = 'black', width = 10, height = 2, command = exit)
        exitButton.place(relx = 0.5, rely = 0.9, anchor = CENTER)

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
        
    def game2ButtonClicked(self):
        self.new = game2Window()
        
    def game3ButtonClicked(self):
        self.new = game3Window()

class game1Window(Toplevel):
    
    def __init__(self):
        
        super().__init__() # master = master
        self.title("Number Guessing Game")
        self.geometry("800x600")
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
        self.nLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        
        # startLabel that is constantly updated based on the entry of the number guessed after the user 
        # clicks 'Guess Number'
        self.startLabel = ttk.Label(self, text = "Click on Start Game", style = 'start.TLabel') # font size 15
        self.startLabel.place(relx = 0.5, rely = 0.63, anchor = CENTER)
        
        # hintLabel is constantly updated based on the state of the game. So if your guess was below the random number,
        # it would tell you: "Hint: Your number is between {guess} and 100"
        # self.hintLabel = ttk.Label(self, text = '-', style = 'start.TLabel')
        # self.hintLabel.place(relx = 0.49, rely = 0.77, anchor = CENTER)
        
        # startButton allows you to start the guessing game
        self.startButton = ttk.Button(self, text = 'Start Game', style = 'g1.TButton', command = self.guessNum)
        self.startButton.place(relx = 0.35, rely = 0.9, anchor = CENTER)
        
        # hintButton allows you to receive a hint if the game is getting too difficult
        # lambda allows you to pass self.hint into the button to generarte a hint whenever it is clicked
        # self.hintButton = ttk.Button(self, text = 'Hint', style = 'g1.TButton', command = lambda: self.updateHint(self.hint))
        # self.hintButton.place(relx = 0.5, rely = 0.9, anchor = CENTER)
        
        # backButton allows you to exit the game1Window and return to the mainWindow
        self.backButton = ttk.Button(self, text = 'Back to Menu', style = 'g1.TButton', command = self.destroy)
        self.backButton.place(relx = 0.65, rely = 0.9, anchor = CENTER)
        
        # guessNumButton allows you to guess a number a get a result on whether it was too high,
        # too low, or if you got it correct
        # set the state of guessNumButton back to 'diabled' so the user won't be able to get headstart before 
        # they press 'Start Game'
        self.guessNumButton = ttk.Button(self, text = 'Guess Number', style = 'guess.TButton', state = DISABLED, command = self.guessingGame)
        self.guessNumButton.place(relx = 0.35, rely = 0.5, anchor = CENTER)
        
        # entry that allows user to input number guess
        self.guessEntry = ttk.Entry(self, style = 'g1.TEntry', textvariable = self.sVar)
        self.guessEntry.place(relx = 0.65, rely = 0.5, anchor = CENTER)
        
        # label that lisst the directions of the game
        self.welcomeLabel = ttk.Label(self, text = "Welcome to the Number Guessing Game! " +
        "\nIn this game, you will be asked to input a random number" +
        "\nwhich will then be compared to the generated number from " +
        "\nthe computer. You will have 5 trials to guess the number. " +
        "\nYou will be told if it is too high, too low, \nor if you guessed correctly. " +
        "\nEnjoy playing!", style = 'welcomeLabel.TLabel') # in order to put a border around a label, have height, width, borderwidth, and
        # relif = 'solid' attributes set
        self.welcomeLabel.place(relx = 0.5, rely = 0.3, anchor = CENTER)
        
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
        # self.hintLabel.configure(text = hints)
    
    # # function that updates the hint label by giving the user a hint
    # def updateHint(self, text):
    #     self.hintLabel.configure(text = text)
        
    # function that's able to enable the Guess Number button and allow the user to begin guessing
    def guessNum(self):
        # set the button back to NORMAL once the user clicks 'Start Game'
        self.guessNumButton.config(state = NORMAL)
        
        self.iVar = IntVar()
        self.sVar = StringVar()
        
        self.trial = 1
        self.total = 5
        self.randNum = randint(0, 100)
        # self.hint = '-'
        
        # set the text of updateResult
        self.updateResult(text = "Guess a random number between 0 and 100")
        # self.updateHint(text = "-")
        # self.updateResult(hints = "-")
        
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
        # self.hint = '-'
        
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
                self.result = (f"Trial {self.trial}. Your guess {self.ask} was too low!" +
                f"\nYou have {self.trialRun} trials left.")
                # self.hint = (f"Hint: Your next guess should be between {self.ask} and 100.")
                # (f"You have {self.trial} trials left. " +
                # "\nYour guess " + self.ask + " was too low!")
                # subtract 1 from each trial run
                # print("TESTING POINT 1")
                self.trial += 1
                
                # if (self.trialRun < 3):
                #     self.hint = (f"Hint: Your next guess should be between {self.ask} and 100.")
                    
            # if user input is greater than randNum
            elif (self.ask > self.randNum):
                self.result = (f"Trial {self.trial}. Your guess {self.ask} was too high!" +
                f"\nYou have {self.trialRun} trials left.")
                # self.hint = (f"Hint: Your next guess should be between 0 and {self.ask}.")
                # (f"You have {self.trial} trials left. " + 
                # "\nYour guess " + self.ask + " was too high!")
                # print("TESTING POINT 2")
                self.trial += 1
                
                # print(self.randNum)
                
                # if (self.trialRun < 3):
                #     self.hint = (f"Hint: Your next guess should be between 0 and {self.ask}.")
             
        # problem: the program kept printing "sorry..." even if the player guessed the random number correctly.
        # solution: put the elif statement for if the number is guessed correctly outside of the inside if statement  
        # if user input is equal to randNum
        elif (self.ask == self.randNum):
            # self.trialRun = self.total - self.trial
            self.result = ("Congratulations! You guessed " + str(self.randNum) + " correctly!" + 
            f"\nYou used {self.trial} trials! \nClick on 'Start Game' to play again or " + 
            "\n'Back to Menu' to return to the main menu.")
            # (f"Congratulations! You guessed {self.randNum} correctly! " +
            # f"\nIt took you {self.trial} trials! Click on 'Start Game' " + 
            # "\nto play again or 'Back to Menu' to return to the main menu.")
            # if you guessed correctly, set the state of the guessNumButton back to 'disbaled'
            self.guessNumButton.configure(state = DISABLED)        
        
        # if the trial reaches zero and you haven't correctly guessed randNum
        else:
            self.result = ("Sorry! You have exhausted the number of trials! " + f"\nThe number was {self.randNum}. "
            + "Thank you for playing!" + "\nClick on 'Start Game to play again or 'Back to Menu' " + 
            "\nto return to the menu.")
            # print("RANDOM NUMBER" + self.randNum)
            # if you exhaust all your trials, set the state of guessNumButton back to DISABLED, command = ""
            self.guessNumButton.configure(state = DISABLED)
            
        # update the result with the text of the condition that gets looped through
        self.updateResult(self.result)
        
        # update the hint with each condition that passes
        # self.updateResult(self.hint)
        # self.onHintClick(self.hint)
        
class game2Window(Toplevel):
    
    def __init__(self):
        
        super().__init__()
        self.title("Rock, Paper, Scissors")
        self.geometry("800x670")
        self.config(background = '#FFFF66')
        
        # create variables userCount, compCount, and tieCount that will hold the scores for each win
        self.userCount = 0
        self.compCount = 0
        self.tieCount = 0
        
        # variable sVar that is set equal to StringVar() which will receive the entry of the user's input
        self.sVar = StringVar()
        
        # same with iVar
        self.iVar = IntVar()
        
        # labels, entries, and buttons for game2Window
        
        # title label
        self.rpsLabel = ttk.Label(self, text = 'Rock, Paper, Scissors Game', style = 'title.TLabel')
        self.rpsLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        
        # label that gets updated with a new text based on your input of rock, paper, or scissors
        self.playLabel = ttk.Label(self, text = 'Click on Start Game', style = 'gameLabels.TLabel')
        self.playLabel.place(relx = 0.52, rely = 0.59, anchor = CENTER)
        
        # represents the user's score
        self.uLabel = ttk.Label(self, text = '   User    ', style = 'count.TLabel')
        self.uLabel.place(relx = 0.3, rely = 0.67, anchor = CENTER)
        
        # temporary label for user
        self.uTempLabel = ttk.Label(self, text = '0', style = 'gameLabels.TLabel')
        self.uTempLabel.place(relx = 0.3, rely = 0.77, anchor = CENTER)
        
        # represents the tie score
        self.tLabel = ttk.Label(self, text = '   Tie    ', style = 'count.TLabel')
        self.tLabel.place(relx = 0.5, rely = 0.67, anchor = CENTER)
        
        # temporary label for the tie
        self.tTempLabel = ttk.Label(self, text = '0', style = 'gameLabels.TLabel')
        self.tTempLabel.place(relx = 0.5, rely = 0.77, anchor = CENTER)
        
        # represents the computer score
        self.cLabel = ttk.Label(self, text = ' Computer  ', style = 'count.TLabel')
        self.cLabel.place(relx = 0.72, rely = 0.67, anchor = CENTER)
        
        # temporary label for computer
        self.cTempLabel = ttk.Label(self, text = '0', style = 'gameLabels.TLabel')
        self.cTempLabel.place(relx = 0.72, rely = 0.77, anchor = CENTER)
        
        # button that allows you to begin the game
        self.playButton = ttk.Button(self, text = 'Start Game', command = self.rpsStart)
        self.playButton.place(relx = 0.35, rely = 0.9, anchor = CENTER)
        
        # button that allows you to exit the game2Window and return to the main menu
        self.backMenuButton = ttk.Button(self, text = 'Back to Menu', command = self.destroy)
        self.backMenuButton.place(relx = 0.65, rely = 0.9, anchor = CENTER)
        
        # button that allows your to submit your input of rock, paper, or scissors, and lets you know if you won,
        # the computer won, or if there was a tie
        # state of the button will be set to disabled until the user clicks 'Start Game'
        self.rpsPlayButton = ttk.Button(self, text = 'Play', style = 'useButtons.TButton', state = DISABLED, command = self.rpsGame)
        self.rpsPlayButton.place(relx = 0.35, rely = 0.5, anchor = CENTER)
        
        # entry that allows you to input rock, paper, or scissors
        self.rpsEntry = ttk.Entry(self, style = 'gameEntry.TEntry', textvariable = self.sVar)
        self.rpsEntry.place(relx = 0.65, rely = 0.5, anchor = CENTER)
        
        # welcomeLabel that lists the directions for the game
        self.welcomeRPSLabel = ttk.Label(self, text = "Welcome to the 'Rock, Paper, Scissors Game'! " +
                "\nIn this game, you will be asked to input 'rock', 'paper', or " + 
                "\n'scissors. Once you do, your input will be compared to a " +
                "\ncomputer's input. For every computer win, user win, or tie, " +
                "\nyour points will be recorded. If either player gets 10 points, " +
                "\n the game will end, and the user will be congratulated." 
                "\nEnjoy playing!", style = 'welcomeLabel.TLabel')
        self.welcomeRPSLabel.place(relx = 0.5, rely = 0.3, anchor = CENTER)
        
        # create style object
        self.style = ttk.Style(self)
        
        # style for labels, buttons, and entries
        self.style.configure('title.TLabel', font = ('courier', 25, 'bold'), background = '#FFFF66')
        self.style.configure('count.TLabel', font = ('courier', 13, 'bold'), background = '#FFFF66', foreground = 'black',
        borderwidth = 2, width = 10, height = 2, relief = 'solid')
        self.style.configure('gameLabels.TLabel', font = ('courier', 13, 'bold'), background = '#FFFF66')
        self.style.configure('useButtons.TButton', font = ('courier', 15, 'bold'), background = '#FF666', foreground = 'black',
        width = 12)
        self.style.configure('gameEntry.TEntry', font = ('courier', 15), width = 15)
        self.style.configure('welcomeLabel.TLabel', font = ('courier', 13, 'bold'), background = '#FFFF66', borderwidth = 2, width = 66,
        height = 7, relief = 'solid')
        
    # function that updates the play label
    def playUpdate(self, text, u, t, c):
        self.playLabel.configure(text = text)
        self.uTempLabel.configure(text = u)
        self.tTempLabel.configure(text = t)
        self.cTempLabel.configure(text = c)
        
    # function that enables the 'Play' button and allows the user to begin inputting their response
    def rpsStart(self):
        # set the state of playButton back to NORMAL
        self.rpsPlayButton.configure(state = NORMAL)
        
        # set trial to 1
        # set compChoice equal to randint(0, 2) so that you can have 0 = rock, 1 = paper, 2 = scissors
        self.compChoice = randint(0, 2)
        self.c = '0'
        self.u = '0'
        self.t = '0'
        self.trial = 1
        
        # set the text that will continue to be updated depending on the entry
        self.playUpdate(text = "Enter 'rock', 'paper', or 'scissors'", u = '0', c = '0', t = '0')
        # self.playUpdate(u = '0')
        # self.playUpdate(c = '0')
        # self.playUpdate(t = '0')
        
        # delete the entry after either the user or the computer wins 10 times/points
        self.rpsEntry.delete(0, END)
        self.uTempLabel.deletecommand
        self.tTempLabel.deletecommand
        self.cTempLabel.deletecommand
        
    # main function that runs the rpsGame
    def rpsGame(self):
        # set your sVar and iVar variables
        self.iVar = IntVar()
        self.sVar = StringVar()
        
        print(self.trial)
        
        # get the value from rpsEntry
        self.userChoice = self.rpsEntry.get()
        print("Testing Point 1")
        print(self.userChoice)
        print("After Testing Point")
        
        # create if-elif-else statement that set the int values as their concurring strings
        if (self.compChoice == 0):
            self.compChoice = 'rock'
        elif (self.compChoice == 1):
            self.compChoice = 'paper'
        else:
            self.compChoice = 'scissors'
            
        # set the outer if statement to run for as long as userCount and compCount != 10
        if (str(self.compCount) != '10' or str(self.userCount) != '10'):
            # conditional statements for each choice
            if (self.compChoice == 'rock' and self.userChoice == 'scissors'):
                self.win = (f"Trial {self.trial}. The computer chose rock and the user chose scissors." +
                "\nComputer Wins!")
                
                # call temporary text of cTempLabel and set it equal to the update of compCount
                self.compCount += 1
                self.cTempLabel['text'] = str(self.compCount)
                self.trial += 1
                
                print("CompCount Score")
                print(self.compCount)
                print('-')
                
            elif (self.compChoice == 'paper' and self.userChoice == 'rock'):
                self.win = (f"Trial {self.trial}. The computer chose paper and the user chose rock." +
                "\nComputer Wins!")
                
                # call temporary text of cTempLabel and set it equal to the update of compCount
                self.compCount += 1
                self.cTempLabel['text'] = str(self.compCount)
                self.trial += 1
                
                print("CompCount Score")
                print(self.compCount)
                print('-')
            
            elif (self.compChoice == 'scissors' and self.userChoice == 'paper'):
                self.win = (f"Trial {self.trial}. The computer chose scissors and the user chose paper." +
                "\nComputer Wins!")
                
                # call the temporary text of cTempLabel and set it equal to the update of compCount
                self.compCount += 1
                self.cTempLabel['text'] = str(self.compCount)
                self.trial += 1
                
                print("CompCount Score")
                print(self.compCount)
                print('-')
                
            # if it ends in a tie
            elif (self.compChoice == self.userChoice):
                self.win = (f"Trial {self.trial}. It's a tie!")
                
                # call the temporary text of tTempLavel and set it equal to the update of tieCount
                self.tieCount += 1
                self.tTempLabel['text'] = str(self.tieCount)
                self.trial += 1
                
                print("TieCount Score")
                print(self.tieCount)
                print('-')
                
            elif (self.userChoice == 'rock' and self.compChoice == 'scissors') or (self.userChoice == 'paper' and self.compChoice == 'rock') and (self.userChoice == 'scissors' and self.compChoice == 'paper'):
                self.win = (f"Trial {self.trial}. The user chose " + self.userChoice + " and the computer chose " + self.compChoice + "." +
                "\nUser Wins!")
                
                # call the temporary text of uTempLavel and set it equal to the update of userCount
                self.userCount += 1
                self.uTempLabel['text'] = str(self.userCount)
                self.trial += 1
                
                print("UserCount Score")
                print(self.userCount)
                print('-')
                
            # check if the user enters something other than rock, paper, or scissors
            else:
                self.win = ("Your entry is invalid. Please try again.")
                
                self.uTempLabel['text'] = str(self.userCount)
                self.tTempLabel['text'] = str(self.tieCount)
                self.cTempLabel['text'] = str(self.compCount)
                
        else:
            self.win("Looks like 10 points have been reached!" + 
            "\nThank you for playing! To play again, click 'Start Game'." +
            "\nTo go back to the menu, click 'Back to Menu'.")
            self.rpsPlayButton.configure(state = DISABLED)
            self.uTempLabel['text'] = '0'
            self.tTempLabel['text'] = '0'
            self.cTempLabel['text'] = '0'
            
        # update the text of playUpdate by calling the text of win, cTemp, tTemp, uTemp
        self.playUpdate(self.win, self.uTempLabel['text'], self.tTempLabel['text'], self.cTempLabel['text'])
        
class game3Window(Toplevel):
    # constructor that will be called everytime the program is run
    def __init__(self):
        
        super().__init__()
        self.title("Fun Fact Quiz Game")
        self.geometry("830x650")
        self.config(background = '#CCCC99')
        
        # title label
        self.factTitleLabel = ttk.Label(self, text = 'Fun Fact Game', style = 'title.TLabel')
        self.factTitleLabel.place(relx = 0.5, rely = 0.08, anchor = CENTER)
        
        # button that starts the quiz game overall
        self.doStartButton = ttk.Button(self, text = 'Start Game', style = 'startAndBackButtons.TButton')
        self.doStartButton.place(relx = 0.15, rely = 0.9, anchor = CENTER)
        
        # button that allows you to go back to the menu
        self.goBacktoMenuButton = ttk.Button(self, text = 'Back to Menu', style = 'startAndBackButtons.TButton', command = self.destroy)
        self.goBacktoMenuButton.place(relx = 0.85, rely = 0.9, anchor = CENTER)
        
        # welcome label
        self.stateLabel = ttk.Label(self, text = "Welcome to the Fun Fact (Quiz) Game! In this game, "
        + "\nyou will be asked a total of 11 questions. For each question " + 
        "\nyou get right, your score increases by 2 points. " +
        "\nFor each question you get wrong, your score decreases " +
        "\nby 1 point. Enjoy playing!", style = 'stateLabel.TLabel')
        self.stateLabel.place(relx = 0.5, rely = 0.212, anchor = CENTER)
        
        # create style object
        self.style = ttk.Style(self)
        
        # style for labels, buttons, and maybe entries
        self.style.configure('title.TLabel', font = ('courier', 25, 'bold'), background = '#CCCC99')
        self.style.configure('startAndBackButtons.TButton', font = ('courier', 15, 'bold'), background = '#FF6633',
        foreground = 'black', width = 12)
        self.style.configure('stateLabel.TLabel', font = ('courier', 13, 'bold'), background = '#CCCC99',
        borderwidth = 2, width = 66, height = 6, relief = 'solid')
        
        # create json file that will holds your questions and answers for the quiz
        # they will hold name/value pairs and contain an array of values
        
        '''
        To create this Fun Fact Quiz Game:
        1. Import modules: tkinter and json
        2. Add widgets to display the data
        3. Add the functionalities to the button
        4. Use the data from the json file
        '''
        
        # create your variables and functions that will be called for each part of your program
        self.questionNumber = 0
        self.quizTitle()
        self.eachQuestions()
        # set your variable that will hold IntVar()
        self.optionSelection = IntVar()
        self.options = self.radio_Buttons()
        self.theOptions()
        self.buttons()
        self.totalQuestionSize = len(questions)
        self.correctQuestions = 0
        
        # function that displays the result for the quiz in a messagebox
        
# runs the mainWindow
if __name__ == "__main__":
    master = mainWindow()
    master.mainloop()