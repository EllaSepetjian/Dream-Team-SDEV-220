# Ella Sepetjian
# SDEV 140
# Start date - 11/28/21
# End date - 
''' This GUI program is a number guessing game. There are two windows:
one for the home and a second where the game is actually played. The first
window introduces my cat Catnip and asks the user for their name.
The second window will change colors as the user gets closer or ferther from
the number.'''


# Imports
from tkinter import *
from PIL import ImageTk,Image
from random import randint

# The root of my GUI program
Root = Tk()

# Tiyle of my application
Root.title("Trendy Guesser")

# My icon pic
Image = PhotoImage(file = "CuteCatPic.PNG")
Root.iconbitmap('CuteCatPic.png')

# Define my NameLabel before my function so I can delete it if the user tries different names
NameLabel = Label(Root)

# A function to display the user's name
def HelloName():
    global NameLabel

    # This deletes any name that the label is holding 
    NameLabel.destroy()

    # This label greats the user by their name
    NameLabel = Label(Root, text = "Hello " + InputName.get(), font=("Comic Sans MS", 20))
    NameLabel.configure(bg = "White")
    NameLabel.grid(row = 5, column = 1, sticky = "W")
    

    # Play button
    PlayButton = Button(Root, text = "Come Play With Me!", font=("Comic Sans MS", 15), command = NewWindow)
    PlayButton.configure(bg = "deepskyblue", fg = "white")
    PlayButton.grid(row = 5, column = 2)
    
# Color of the background
Root.configure(bg="pink")

# Size
Root.geometry("1000x700")

# Ctreating my labels
MyLabel = Label(Root, text = "Welcome to Trendy Guesser!", padx = 50, font=("Comic Sans MS", 24))
MyLabel.configure(bg = "white")
MyLabel.grid(row = 0, column = 0, columnspan = 3, sticky = "W")
    # A space between rows
MySpaceLabel = Label(Root)
MySpaceLabel.configure(bg = "pink")
MySpaceLabel.grid(row = 1, column = 0)    
    # Cat name
MyCatLabel = Label(Root, text = "My name is Catnip! What's yours?", font=("Comic Sans MS", 20))
MyCatLabel.configure(bg = "white")
MyCatLabel.grid(row = 2, column = 1, sticky = "W")

# Input name
InputName = Entry(Root, text = "Please enter your name.", font=("Comic Sans MS", 22))
InputName.grid(row = 3, column = 1, sticky = "W")

# Submit name button
NameButton = Button(Root, text = "Submit", command = HelloName, font=("Comic Sans MS", 15))
NameButton.configure(bg = "deepskyblue", fg = "white")
NameButton.grid(row = 3, column = 2, sticky = "W")

# A space between rows
MySpaceLabel = Label(Root)
MySpaceLabel.configure(bg = "pink")
MySpaceLabel.grid(row = 4, column = 0)




# SECOND WINDOW HURRAY!!!
def NewWindow():

    # New window and name
    GameWindow = Toplevel()
    GameWindow.title("Guess My Number")

    # Size
    GameWindow.geometry("750x500")
    
    # My main label
    GameLabel = Label(GameWindow, text = "I'm Thinking of a Number Between 1 And 10. What is it???", font=("Comic Sans MS", 20))
    GameLabel.grid(row = 0, column = 0, columnspan = 3, pady = 20, sticky = "W")

    # This function figures out if the user's entry is a number or not and changes the color
    # of the background as the user's guesses gets closer to the correct number
    def Guesser():
        

        # If the user's guess is a number then then the main label will stay and the variable
        # Difference will be defined
        if UserGuess.get().isdigit():
            GameLabel.configure(text = "I'm Thinking of a Number Between 1 And 10. What is it???", font=("Comic Sans MS", 20))

            # The Difference gets the absolute value of the random number minus the user's
            # number
            Difference = abs(Number - int(UserGuess.get()))

            # If the user's guess is correct the game will congradulate them and change the
            # color to gold
            if int(UserGuess.get()) == Number:
                BackgroundColor = "gold"
                GameLabel.configure(text = "Hurray! You Got it!", font=("Comic Sans MS", 15))

                # A new game button will appear once the first game ends
                NewGame = Button(GameWindow, text = "Play Again!?", font=("Comic Sans MS", 15), command = Random)
                NewGame.grid(row = 2, column = 1, pady = 20, sticky = "W")

            # If the difference is half way to the number the background color will change to
            # purple
            elif Difference == 5:
                BackgroundColor = "purple"
                GameLabel.configure(text = "Yay Your Half Way There!", font=("Comic Sans MS", 20))

                
            # If the difference is greater than the half way mark then the background color
            #will change shades of red as the user's guess gets closer to the answer   
            elif Difference < 5:
                BackgroundColor = f'#ff{Difference}{Difference}{Difference}{Difference}'
                GameLabel.configure(text = "Yay Your Getting Warmer!", font=("Comic Sans MS", 20))


            # If the difference is less than the half way mark then the background color
            #will change shades of blue as the user's guess gets ferther from the answer 
            else:
                BackgroundColor = f'#{Difference}{Difference}{Difference}{Difference}ff'
                GameLabel.configure(text = "Brr! Your cold!", font=("Comic Sans MS", 20))


            # The backgrounds of both the window and the labels will get set to Whatever color
            # the background color is set to 
            GameWindow.configure(bg = BackgroundColor)
            GameLabel.configure(bg = BackgroundColor)

            # After each guess is submitted the guess box will get reset
            UserGuess.delete(0, END)

        # If the User enters anything but a number the program will through an error and the
        # guess box will get reset
        else:
            UserGuess.delete(0, END)
            GameLabel.configure(text = "Hey that's not a number lol.", font=("Comic Sans MS", 20))

    # This function generates a random number
    def Random():

        # My number variable is a global variable so it can be used everywhere I need it
        global Number

        # Generates a random number
        Number = randint(1, 10)

        # This resets the guess box
        UserGuess.delete(0, END)

        # This resets the label and the window's color
        GameLabel.configure(text = "I'm Thinking of a Number Between 1 And 10. What is it???", font=("Comic Sans MS", 20), bg = "SystemButtonFace")
        GameWindow.configure(bg = "SystemButtonFace")

    # This function close the game window
    def Close():
       GameWindow.destroy()
       
    # This is the entry box for the user to guess the random number
    UserGuess = Entry(GameWindow, font=("Comic Sans MS", 30), width = 3)
    UserGuess.grid(row = 1, column = 1, pady = 20, sticky = "W")

    # This is the guess button for the user to submit their guesses
    GuessButton = Button(GameWindow, text = "Guess", font=("Comic Sans MS", 15), command = Guesser)
    GuessButton.grid(row = 1, column = 2, pady = 20, sticky = "W")

    # This is the quit button if the user wishes to quit playing
    QuitButton = Button(GameWindow, text = "Quit", font=("Comic Sans MS", 15), command = Close)
    QuitButton.grid(row = 2, column = 2, pady = 20, sticky = "W")

    # When the game window is open the the game will start
    Random()
    GameWindow.mainloop()

# This runs the first window
Root.mainloop()
