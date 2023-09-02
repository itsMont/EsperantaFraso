# Prezentu la ludon al la ludistoj
import random
def getNumPlayers():
    try:
        numPlayers = int(input())
    except:
        print("Bonvolu registri validan nombron / Please input a valid number")
        return 0
    return numPlayers

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

players = {key : value for (key, value) in zip(arrPlayers,[0 for i in arrPlayers])}
print(players)

# Pick a random phrase and display it
phrases = ["Mi konas vin ekde la lasta somero", "Ni kisas la katidojn sur la cxapo", "La cxapelo estas tre granda por la infano"]
selPhrase = random.choice(phrases)
print(selPhrase)

# Turn it into a hidden phrase
hiddenPhrase = ""
for i in selPhrase:
    if i != ' ':
        hiddenPhrase += "_"
    else:
        hiddenPhrase += i
print("""


This is the phrase you must guess: 


{}
""".format(hiddenPhrase))

print("Now guess {}".format(arrPlayers[0]))
guess = input()

phraseList = selPhrase.split()
hiddenList = hiddenPhrase.split()
print(phraseList)
print(hiddenList)
if guess in selPhrase:
    for i in range(len(phraseList)):
        if guess in phraseList[i]:
            newWord = ""
            for j in range(len(phraseList[i])):
                
                if phraseList[i][j] == guess:
                    newWord += guess
                else:
                    newWord += "_"
            hiddenList[i] = newWord
                    
    print(hiddenList)
   
else:
    print("'{}' It's not in the phrase".format(guess))

for i in hiddenList:
    print(i, end = " ")
print()

