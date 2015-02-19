# durak_the_game
## Description

Simple card game, popullar in post-Soviet states. I have played it as a child in eastern Poland.

The game was created for a [An Introduction to Interactive Programming in Python (Part 1) class](https://class.coursera.org/interactivepython1-002).


Description on the [Wikipedia](http://en.wikipedia.org/wiki/Durak)


## Rules

This is a simple version of the game for 2-4 players. The goal of the game is to get rid of the cards and not be the last player holding cards in their hand, i.e. Durak (The Fool in Russian). 

### The Deck

From the standard 52 card deck, the 2,3,4 and 5 cards are removed, so the final playing deck consists of 36 cards. The thrum suit for each game is randomly selected by putting one of the cards on the bottom of the card deck. 

### Card Ranks

6:	6  
7:	7  
8:	8  
9:	9  
10:	10  
J:	11  
Q:	12  
K:	13  
A:	14  

### Thump suit

The thump card beats the other colours regardless of rank. The trump suit is selected by putting the card on top of back to bottom - it becomes the last card to be drawn and is shown to the players. 

### Gameplay

Each player receives 6 initial cards, the play proceeds clockwise from the starting player, who is chosen randomly. The starting player "attacks" the next clockwise player and he becomes a "defender".

The "attacker" is playing a card from his hand. In this variant of the game, the "defender" has to defend against the attack, by presenting the higher card of the same colour or any thump card.

At any time, other players may add a card from their hand, if the card on their table match the rank of a card in their hand. The "defender" must also defend against the new card. If defender fails to produce cards of higher standing, he is obliged to take all the cards from the table into his hand and loses his turn.

Otherwise, in case of successful defence, the cards on the table are discarded.


## Input Parameters
* Number of players - minimum is 2, maximum is 5. 

## Development Status

First draft of the game. 