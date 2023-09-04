# Get a valid number of players
def getNumPlayers():
    try:
        numPlayers = int(input())
    except:
        print("Bonvolu registri validan nombron / Please input a valid number")
        return 0
    return numPlayers

# Turn it into a hidden phrase
def createHiddenPhrase(phrase):
    hiddenPhrase = ""
    for i in phrase:
        if i != ' ':
            hiddenPhrase += "_"
        else:
            hiddenPhrase += i
    return hiddenPhrase.split()

# Receives a hiddenPhrase as a list and prints it
def displayHiddenPhrase(hidden):
    for i in hidden:
        print(i, end = " ")
    print("\n\n")

# This makes a guess and returns the hidden phraese with the character guesses uncovered
def makeGuess(guess, originalPhrase, hiddenPhrase):
    # It doesnt matter if the guess is in lowercase or uppercase
    lowerOriginalPhrase = originalPhrase.lower()
    guess = guess.lower()

    # keep a list with original characters
    phraseList = originalPhrase.split()

    if guess in lowerOriginalPhrase:
        for i in range(len(phraseList)):
            if guess in phraseList[i].lower():
                newWord = ""
                for j in range(len(phraseList[i])):
                    if phraseList[i][j].lower() == guess:
                        # Copies the exact letter according to original phrase
                        newWord += phraseList[i][j]
                    else:
                        newWord += hiddenPhrase[i][j]
                hiddenPhrase[i] = newWord
    else:
        print("'{}' It's not in the phrase".format(guess))
    displayHiddenPhrase(hiddenPhrase)
    return hiddenPhrase

# Checks if players can still make a guess
def playersStillGuess(players):
    sum = 0
    for i in players.values():
        sum += i
    if sum <= 0:
        return False
    return True
# Check if a specified player can guess
def playerCanGuess(players, player):
    return players[player] > 0

# decrease tries for player
def decreaseTries(players, player):
    players[player] -= 1

# copies content from a list to another list
def copyList(original):
    newList = []
    for i in original:
        newList.append(i)
    return newList

# compares original list with guess list
def comparesToGuess(originalList, guessList):
    for i in range(len(originalList)):
        if originalList[i] != guessList[i]:
            return False
    return True

# function to receive the guess input correctly:
def receiveGuess():
    receive = True
    while receive:
        try:
            guess = input()[0]
            # In case user inputs a number or whatsoever
            if len(guess) > 1:
                raise RuntimeError
            if not guess.isalpha():
                raise ValueError
            receive = False

        except ValueError:
            print("La esperanta frazo ne havas nombrojn / The esperanto phrase doesn't have a number")

        except:
            print("Faru validan divenon / Make a valid guess.")
    return guess

