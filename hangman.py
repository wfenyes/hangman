#What do you I need
# two player game - input from two different players
# first player picks a word 
# second player picks a letter
# if letter there reveal letter/ if not add body part
# pick a letter or guess the word

def getName():
    wordToGuess = input("What is your word?\n")
    print("Thank you for choosing!")
    return wordToGuess

def takeGuess():
    wordOrLetter = input("Would you like to guess a letter or a word?\n")
    if "word" in wordOrLetter:
        wordGuess = input("OK, what word do you think it is?\n")
        return wordGuess
    else:
        letterGuess = input("Alright, guess a letter.\n")
        return letterGuess

def drawMan(guessNumber):
    pictureOptions = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


    return pictureOptions[guessNumber]

def playHangman():
    keyWord = getName()
    guess = takeGuess()
    while True:
        if guess == keyWord:
            print("Congratulations!!!!")
            break
        else:
            print("done")
            break
    

    

print(drawMan(1))