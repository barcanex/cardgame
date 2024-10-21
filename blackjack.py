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

#Creating chips , giving chips according to win_bet,lose_bet            
class Chips():

    def __init__(self,total=100):
        self.total = total 
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

#Taking bets function

def take_bet(chips):
    
    while True:
        try:
            chips.bet= int(input ("How many chips would you like to bet? "))
        except:
            print("Error.Please provide an integer.")
        else:
            if chips.bet > chips.total :
                print("Error, exceeded limit. You have : {}".format(chips.total))
            elif chips.bet <= 0 :
                print("Negative or 0 value detected. Please try again")
            else:
                print(f"\nBet : {chips.bet} chips.")
                break
#Hit 0

def hit(deck,hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace
#Hit or stand

def hit_or_stand(deck,hand):
    global playing 

    while True:
        x = input("Hit or Stand? Enter H or S ")

        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stands, dealer's turn")
            playing = False
        else:
            print("Sorry please try again")
            continue
        break
#Show some cards beginning\

def show_some(player,dealer):
    #Show only One of the dealer's cards
    print("\nDealer_hand's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])
    #Show all (2 cards) of the player's hand/cards
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)
#Show all cards

def show_all(player,dealer):

    #Show all the dealer's cards
    print("\n dealer_hand's Hand: ")
    for card in player.cards:
        print(card)
    #calculate and disp value (J+K == 20)
    print(f"Value of dealer_hand's hand is {dealer.value}")
    #Show all the player's cards
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of dealer_hand's hand is {dealer.value}")
#Result

def player_busts(player,dealer,chips):
    print("Bust Player!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):#TIE
    print("Dealer and player tie!")

while True:
#Create & Shuffle Deck
    test_deck = Deck()
    test_deck.shuffle()

    #Create each player's hand with nothing
    player_hand = Hand()
    dealer_hand = Hand()

    #Add cards to their hand

    for x in range(2):
        player_hand.add_card(test_deck.deal())
        player_hand.adjust_for_ace()
        dealer_hand.add_card(test_deck.deal())
        dealer_hand.adjust_for_ace()

    #Bet chips
    Pchips = Chips()
    take_bet(Pchips)

    #Show initial cards
    show_some(player_hand,dealer_hand)
    playing = True
    while playing:

        #Prompt for Player to Hit or Stand
        hit_or_stand(test_deck,player_hand)

        #Show cards again (keep dealer hidden)
        show_some(player_hand,dealer_hand)

        #Check player's cards sum

        if player_hand.value > 21  :
            player_busts(player_hand,dealer_hand,Pchips)
        
            break
        
    #If player hasnt bust , dealer draws until greater than 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(test_deck,dealer_hand)
        #show all cards
        show_all(player_hand,dealer_hand)

    # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,Pchips)
    
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,Pchips)
    
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,Pchips)
        else:
            push(player_hand,dealer_hand)

    print("\n Player total chips are at : {}" .format(Pchips.total))

    new_game = input ("Would you like to play again? Y/N: ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you")
        break