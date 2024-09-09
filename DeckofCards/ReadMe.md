# Deck of Cards OOP Project 
## Why am I doing it? 
a. Because it is fun????

b. Because OOP gives me a feeling of OOPs. Hence I am exploring that feeling more.

### Reference
This project is based on video : https://www.youtube.com/watch?v=t8YkjDH86Y4&t=37s

# Understanding the code
1. We begin by defining three classes : Card, Deck and Player all written in new style python.

2. In class 'Card', we pass two variables, value and suit and define a show method which when called will print the type of card.

3. We then go on to define the Deck class. We  define a build() method which will built a pack of cards. This build method is called under the __init__ constructor to ensure that as soon as the Deck object is instantiated, the deck of cards is automatically populated by invoking the build() method. 

4. Within the Build() method we create a nested for loop in order to associate every card with its value. An object of Card class is created which is appended into the instance attribute self.cards. This creates a deck of cards.

5. A showDeck method is added to print the deck of cards and a shuffle method is added to shuffle it. In order to shuffle the deck, we again start by creating a for loop from length of the list self.cards -1 to 0, decrementing. We then select a random value called rand which basically acts as a random index within range of 0 to the outer for loop. We use the value of variable i from outer for loop and one index and value of rand as second index and swap the two values. 

6. Next is we define the drawCard() method which will then help draw the first card in the deck using the pop() method.

7. We then define the Player class which will have an attribute to draw a hand. We pass a deck in drawHand() method. This deck is the deck object instantiated via Deck class. This method returns self. In the drawHand() method, returning self allows for method chaining, which means you can call multiple methods in a single line on the same object. Specifically, in this case, returning self after drawing a card enables you to chain other methods (such as drawHand() again or showHand()) on the same Player object.

8. Finally the player object has two other methods, one is showHand() which allows it to show the hand and discardCard which discards the latest hand.

