import random

suits = ("Hearts","Diamonds", "Spades","Clubs")

ranks = ("Two","Three","Four","Five","Six","Seven"
         ,"Eight","Nine","Ten","Jack","Queen","King","Ace")

values = {"Two" : 2 , "Three" : 3 , "Four":4, "Five":5,"Six":6,
          "Seven":7, "Eight":8, "Nine":9, "Ten":10 , "Jack":10,
          "Queen":10 , "King":10, "Ace":11}

class Card():

    def __init__(self,suit,rank):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        
        return self.rank+" of "+ self.suit

class Deck():

    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand():

    def __init__(self):
        self.cards =[] 
        self.value = 0 #Player starts with 0 value
        self.aces = 0 #Cause they are special occasion
    
    def add_card(self,card):#from Deck.deal(), we ll grab a card from Deck
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == "Ace":
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 
            pass
    
test_deck = Deck()
test_deck.shuffle()

#Player
test_player = Hand()#Creating Hand
pulled_card = test_deck.deal()#Drawing card from Deck
print('First card = ',pulled_card)
test_player.add_card(pulled_card)#Add card to player's hand
print('First hand value = ', test_player.value)
pulled_card_two = test_deck.deal()#Drawing second card
print('Second card = ', pulled_card_two)
test_player.add_card(pulled_card_two)
print('Second hand value = ', test_player.value)

        