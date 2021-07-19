# Author : Are Oelsner
# Description : Tarot deck simulator commissioned as a writing aid for creating plot points and character arcs
import random 

###     Deck Functions
# __init__()        Deck constructor
# shuffle()         Shuffles current deck
# reset()           returns drawn cards to deck and resets order and state
# draw()            draws and returns the top card on the deck
# find(cardNum)     draws and returns the card with the specified card number, if found
# pull(numCards)    draws and returns the specified number of cards
# pullVerbose(numCards) pulls the specified number of cards and prints them
# beforeAndAfter()  draws and prints two cards in before and after format
# print()           prints the entire current deck

# Deck class stores list of cards and associated functions
class Deck:

    # Card class represents a single tarot card
    class Card:
        # Card constructor
        def __init__(self, _number, _name, _state=True, _info = ""):
            self.number = _number
            self.name = _name
            self.state= _state
            self.info = _info
        
        # Shuffles state of card - upright vs reversed
        def shuffle(self):
            self.state = random.getrandbits(1)

        # Prints out basic card information to console
        def print(self):
            state = "upright" if self.state else "reversed" 
            print(self.number + ' : ' + self.name + " " + state)
        
        # Prints full card information to console
        def printVerbose(self):
            data = "upright" if self.state else "reversed"
            if self.info != "":
                data += " : " + self.info
            print(self.number + ' : ' + self.name + " " + data)
        
        # Only prints card information to console
        def printInfo(self):
            print(info)
            
    # Deck constructor
    def __init__(self):
        self.base_deck = []
        with open("tarot.csv") as file:
            for line in file:
                data = line.split(",")
                if(len(data) >=4): # If csv file contains state and card information
                    self.base_deck.append(self.Card(data[0],data[1], data[2], data[3]))
                else:              # If csv file only contains card numbers and names
                    self.base_deck.append(self.Card(data[0],data[1]))
        self.deck = self.base_deck[:]
    
    # Shuffles deck without returning drawn cards
    def shuffle(self):
        random.shuffle(self.deck)
        for card in self.deck:
            card.shuffle()
    
    # Resets deck to original ordering and state
    def reset(self):
        self.deck = self.base_deck[:]

    # Draws and returns a single card from the top of the deck
    def draw(self):
        if len(self.deck) < 1:
            print("Error: not enough cards left in deck")
            return None
        return self.deck.pop()

    # Searches the deck for the specified card number, removes and returns the card if found
    def find(self, cardNum):
        for card in self.deck:
            if card.number == cardNum:
                return self.deck.pop(card)
        print("Error: Card number ", cardNum, " not found in deck")
        return None
    
    # Draws and returns a list of <numCards> cards from the top of the deck
    def pull(self, numCards):
        if len(self.deck) < numCards:
            print("Error: not enough cards left in deck")
            return []
        pulledCards = []
        for card in range(numCards):
            pulledCards.append(self.draw())
        return pulledCards
    
    # Draws <numCards> cards from top of deck and prints info to console
    def pullVerbose(self, numCards):
        cards = self.pull(numCards)
        print("#####\tPulled " , numCards , " cards\t#####")
        for i in range(len(cards)):
            print(i+1, " : ", end="")
            cards[i].print()
        print("#################################\n")

    # draws and returns the top two cards in the deck, printing out their data
    def beforeAndAfter(self):
        if len(self.deck) < 2:
            print("Error: not enough cards left in deck")
            return []
        else:
            print("#####\tBefore and After\t#####")
            drawnCards = self.pull(2)
            print("before: ", end="")
            drawnCards[0].print()
            print("after: ", end="")
            drawnCards[1].print()
            print("#################################\n")
            return drawnCards
    
    # Prints deck to the console
    def print(self):
        print("Printing Deck")
        for card in self.deck:
            card.print()

        


myDeck = Deck()         # Creates deck
myDeck.shuffle()        # Shuffles current deck
myDeck.beforeAndAfter() # Before and After pull
myDeck.pullVerbose(6)   # Pulls and outputs specified cards
myDeck.reset()          # returns all cards to deck and resets order and state



        