
import random as rm 

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def showCard(self):
        print(f"{self.value} of {self.suit}")
    
class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        for s_suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v_val in range(1,14):
                self.cards.append(Card(s_suit, v_val))         
                
    def showDeck(self):
        for c in self.cards:
            c.showCard()  
            
    def shuffle(self):
        for i in range(len(self.cards)-1 , 0, -1):
            rand = rm.randint(0,i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]
    
    def drawCard(self):
        return self.cards.pop()
    
    
class Player(object):
    def __init__(self):
        self.hand = []
        
    def drawHand(self, deck):
        self.hand.append(deck.drawCard())
        return self
        
    def showHand(self):
        for card in self.hand:
            card.showCard()
            
    def discard(self):
        return self.hand.pop()
    
# card = Card("Clubs",6)
# card.show()

deck = Deck()
deck.shuffle()
deck.showDeck()
print("\n")
deck.drawCard().showCard()
# deck.show()

# player = Player()
# player.drawHand(deck).drawHand(deck)
# player.showHand()