from time import sleep
import random

class Card:
    def __init__(self, type='2', suit=chr(3)):
        self.type = type
        self.suit = suit

        if ord(self.type) <= 57:
            self.value = int(self.type)
        elif self.type == 'X':
            self.value = 10
        elif self.type == 'J':
            self.value = 11
        elif self.type == 'Q':
            self.value = 12
        elif self.type == 'K':
            self.value = 13
        elif self.type == 'A':
            self.value = 14
        else:
            self.value = 1
    def changeType(self, type):
        self.type = type
        if ord(self.type) <= 57:
            self.value = int(self.type)
        elif self.type == 'X':
            self.value = 10
        elif self.type == 'J':
            self.value = 11
        elif self.type == 'Q':
            self.value = 12
        elif self.type == 'K':
            self.value = 13
        elif self.type == 'A':
            self.value = 14
        else:
            self.value = 1
    def __str__(self):
        return "|" + self.type + " " + self.suit + "|"

deck = []
computer = []
player = []

playerScore = 0
computerScore = 0

def initializeDeck():
    for i in range(2,10):  #for(int i = 2; i < 10; i++)
        for j in range(3,7):
            deck.append(Card(str(i), chr(j)))
    for i in range(3,7):
        deck.append(Card('X', chr(i)))
        deck.append(Card('J', chr(i)))
        deck.append(Card('Q', chr(i)))
        deck.append(Card('K', chr(i)))
        deck.append(Card('A', chr(i)))

def printDeck(deck):
    for c in deck:
        print(c, end='')
    print()

def shuffle():
    global deck
    temp = deck.copy()
    deck.clear()
    while len(temp) > 0:
        idx = random.randint(0, len(temp)-1)
        deck.append(temp.pop(idx))
def deal():
    global player
    global computer
    global deck
    while len(deck) > 0:
        player.append(deck.pop())
        computer.append(deck.pop())
def play():
    global player
    global computer
    global playerScore
    global computerScore

    while len(player) > 0 and len(computer) > 0:
        print("----------------------------")
        input("Press Enter to Draw Cards...")
        print("----------------------------")

        plrCard = player.pop()
        cpuCard = computer.pop()

        print("You   Drew: " + str(plrCard))
        print("Comp. Drew: " + str(cpuCard))

        if plrCard.value > cpuCard.value:
            print("You Won!")
            playerScore += 1
        elif cpuCard.value > plrCard.value:
            print("CPU Won.")
            computerScore += 1
        else:
            print("It's a tie!")
            
    print("----------")
    print("Final Score:")
    #Even though Python prints integers fine, there's already a string, and we can't add an int to a string! So we need to convert it.
    print("CPU: " + str(computerScore))
    print("You: " + str(playerScore))

    if playerScore > computerScore:
        print("You Won the Game!")
    elif computerScore > playerScore:
        print("The Computer Won the Game!")
    else:
        print("It's a Tie!")



