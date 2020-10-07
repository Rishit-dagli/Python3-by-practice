# Building the popular Game BLACKJACK

* First,
  let’s think about what classes we need. In Blackjack, you have specific game rules, game
  actions, and the deck itself. Then we also need to consider that there is a player and a
  dealer playing the game. 

*  create two classes, one for the game
   itself and one for the two players.

* Game class needs:
   • Game Attributes
        deck – holds all 52 cards to be used within the game
        suites – used to create deck, tuple of all four suits
        values – used to create deck, tuple of all card values
    • Game Methods
        makeDeck – creates new 52-card deck when called
        pullCard – pops random card from deck and returns it

* Player class need:
   • Player Attributes
        hand – stores cards within player’s hand
        name – string variable that stores name of the player or dealer

   • Player Methods
        calcHand – returns the calculated total of points in hand
        showHand – prints out player’s hand in a nicely formatted statement
        addCard – takes in a card and adds it to the player’s hand