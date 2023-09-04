# Prezentu la ludon al la ludistoj
import random
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

numPlayers = 0
print("""


  _____                                _          _____                   
 | ____|___ _ __   ___ _ __ __ _ _ __ | |_ __ _  |  ___| __ __ _ _______  
 |  _| / __| '_ \ / _ \ '__/ _` | '_ \| __/ _` | | |_ | '__/ _` |_  / _ \ 
 | |___\__ \ |_) |  __/ | | (_| | | | | || (_| | |  _|| | | (_| |/ / (_) |
 |_____|___/ .__/ \___|_|  \__,_|_| |_|\__\__,_| |_|  |_|  \__,_/___\___/ 
           |_|                                                            
...........................................................................
ESPERANTO:
    REGULOJ:

    1. Vi povas registri unu leteron. Se via letero estas en la frazo tiam vi povas registri unu leteron denove.

    2. Vi nur havas 10 provos por diveni la tutan frazon.

    3. Gajnas tiu kiu divenas la lastan leteron por kompletigi la frazon.

...........................................................................
ENGLISH:
    RULES:

    1. You can input a character and then, if your character is in the phrase then you can input a character once again.

    2. You only have 10 attempts to guess the whole phrase.

    3. Wins the one who guesses the last character to complete the phrase

""")

# Get number of players: from 1 to 3
print("Diru al mi la nombron de ludantoj (Max. 3): / Tell me the number of players (Max. 3): ")

while(numPlayers <= 0 or numPlayers > 3):
    numPlayers = getNumPlayers()
    if numPlayers == 0:
        print("Devas esti almenaux unu ludanto / There must be at least one player")
    if numPlayers > 3 or numPlayers < 0:
        print("Registri validan nombron: 1, 2, 3")

# Create array of Players with points for each one
arrPlayers = ["player" + str(i+1) for i in range(numPlayers) ]


# You can use a nickname instead of generic game nicknames
for i in range(len(arrPlayers)):
    response = input("Cxu vi volas nomi {} with a nickname? y/n:\t".format(arrPlayers[i]))
    if response == 'y' or response == 'Y':
        nickname = input("Write the name you want for {}:\t".format(arrPlayers[i]))
        arrPlayers[i] = nickname

players = {key : value for (key, value) in zip(arrPlayers,[10 for i in arrPlayers])}
print(players)

# Pick a random phrase and display it
phrases = ["Mi konas vin ekde la lasta somero", "Ni kisas la katidojn sur la cxapo", "La cxapelo estas tre granda por la infano"]
selPhrase = random.choice(phrases)
print(selPhrase)
phraseList = selPhrase.split()

hiddenList = createHiddenPhrase(selPhrase)

print("""


This is the phrase you must guess: 

""")
displayHiddenPhrase(hiddenList)

# Ask the players to make a guess until they can't or the whole phrase is uncovered
idPlayer = 0
# Create an empty string to save the winner nickname
winner = ""
while(not comparesToGuess(phraseList, hiddenList) and playersStillGuess(players)):
    # Get the nickname of the player
    currentPlayer = arrPlayers[idPlayer]
    originalTries = players[currentPlayer]
    winner = currentPlayer
    while playerCanGuess(players, currentPlayer):
        print("Divenu {current} / Now guess {current}".format(current = currentPlayer))
        # Receives the first character of the word it gets
        guess = receiveGuess()
        # Need to compare the original hideen List to the one after the player makesa a guess
        original = copyList(hiddenList)
        # Update the hiddenList with the guess of the player
        hiddenList = makeGuess(guess, selPhrase, hiddenList)
        # Compares the previous version of the Hidden List with the one when the player makes a guess
        # if the previous version of hidden list is the same as the current one, then the guess was invalid
        if comparesToGuess(original, hiddenList):
            decreaseTries(players, currentPlayer)
            print(players)
            break
        # In case the player guess the last chasracter to be guessed
        if comparesToGuess(phraseList, hiddenList):
            break
    idPlayer = (idPlayer + 1) % numPlayers

# if the players didn't guess the whole phrase then there's no winner
if not comparesToGuess(phraseList, hiddenList):
    print("Nenius gajnas. Neniu divenis / It's a tie. Nobody guess")
    print("La esperanta frazo estis: / The Esperanto Phrase was:")
    print(selPhrase)
else:
    print("Gratulon {}!, vi gajnis/ Congrats {}!, you won".format(winner,winner))

