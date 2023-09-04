# Prezentu la ludon al la ludistoj
import random
from functions import *

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
# Receives the correct number of players. Minimum 1 player and Maximum 3 players
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
    response = input("Cxu vi volas nomi {} with a nickname? [Y]es / [N]o:\t".format(arrPlayers[i]))
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


Cxi tiu estas la frazo kiu vi devas diveni / This is the phrase you must guess: 

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
    print("Nenius gajnas. Neniu divenis / It's a tie. Nobody guess\n\n")
    print("La esperanta frazo estis: / The Esperanto Phrase was:")
    print(selPhrase)

else:
    print("""

    Gratulon {winner}!, vi gajnis/ Congrats {winner}!, you won


    """.format(winner = winner))

