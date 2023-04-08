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
    keyWordLength = len(keyWord)
    guessCounter = 0
    print(f"Word is {keyWordLength} letters long")
    guess = takeGuess()
    if len(guess) == 1:
        for i in keyWord:
            if guess in keyWord:
                print(f"Yes, {guess} is in the word!")
            if guess not in keyWord:
                print(f"I'm sorry {guess} is not in the word")
                print(drawMan(guessCounter))
                guessCounter += 1
    elif len(guess) > 1:
        if guess == keyWord:
            Print(f"That's right! {guess} is the word!")
    else:
        print("I don't understand")

    
    

    

playHangman()