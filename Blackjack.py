# Text Based Blackjack Game by Dylan Ward on 5/4/2019
from random import randrange


# define deck of cards class
class Deck:

    def __init__(self, card, suit, value):

        self.card = card
        self.suit = suit
        self.value = value


# create a database of all possible cards to draw from.

# Aces
ace1 = Deck('Ace', 'of Spades', 11)
ace2 = Deck('Ace', 'of Hearts', 11)
ace3 = Deck('Ace', 'of Clubs', 11)
ace4 = Deck('Ace', 'of Diamonds', 11)
# Twos
two1 = Deck(2, 'of Spades', 2)
two2 = Deck(2, 'of Hearts', 2)
two3 = Deck(2, 'of Clubs', 2)
two4 = Deck(2, 'of Diamonds', 2)
# Threes
three1 = Deck(3, 'of Spades', 3)
three2 = Deck(3, 'of Hearts', 3)
three3 = Deck(3, 'of Clubs', 3)
three4 = Deck(3, 'of Diamonds', 3)
# Fours
four1 = Deck(4, 'of Spades', 4)
four2 = Deck(4, 'of Hearts', 4)
four3 = Deck(4, 'of Clubs', 4)
four4 = Deck(4, 'of Diamonds', 4)
# Fives
five1 = Deck(5, 'of Spades', 5)
five2 = Deck(5, 'of Hearts', 5)
five3 = Deck(5, 'of Clubs', 5)
five4 = Deck(5, 'of Diamonds', 5)
# Sixes
six1 = Deck(6, 'of Spades', 6)
six2 = Deck(6, 'of Hearts', 6)
six3 = Deck(6, 'of Clubs', 6)
six4 = Deck(6, 'of Diamonds', 6)
# Sevens
seven1 = Deck(7, 'of Spades', 7)
seven2 = Deck(7, 'of Hearts', 7)
seven3 = Deck(7, 'of Clubs', 7)
seven4 = Deck(7, 'of Diamonds', 7)
# Eights
eight1 = Deck(8, 'of Spades', 8)
eight2 = Deck(8, 'of Hearts', 8)
eight3 = Deck(8, 'of Clubs', 8)
eight4 = Deck(8, 'of Diamonds', 8)
# Nines
nine1 = Deck(9, 'of Spades', 9)
nine2 = Deck(9, 'of Hearts', 9)
nine3 = Deck(9, 'of Clubs', 9)
nine4 = Deck(9, 'of Diamonds', 9)
# Tens
ten1 = Deck(10, 'of Spades', 10)
ten2 = Deck(10, 'of Hearts', 10)
ten3 = Deck(10, 'of Clubs', 10)
ten4 = Deck(10, 'of Diamonds', 10)
# Jacks
jack1 = Deck('Jack', 'of Spades', 10)
jack2 = Deck('Jack', 'of Hearts', 10)
jack3 = Deck('Jack', 'of Clubs', 10)
jack4 = Deck('Jack', 'of Diamonds', 10)
# Queens
queen1 = Deck('Queen', 'of Spades', 10)
queen2 = Deck('Queen', 'of Hearts', 10)
queen3 = Deck('Queen', 'of Clubs', 10)
queen4 = Deck('Queen', 'of Diamonds', 10)
# Kings
king1 = Deck('King', 'of Spades', 10)
king2 = Deck('King', 'of Hearts', 10)
king3 = Deck('King', 'of Clubs', 10)
king4 = Deck('King', 'of Diamonds', 10)

# sort cards into lists by suit
spades = [ace1, two1, three1, four1, five1, six1, seven1, eight1, nine1, ten1, jack1, queen1, king1]
hearts = [ace2, two2, three2, four2, five2, six2, seven2, eight2, nine2, ten2, jack2, queen2, king2]
clubs = [ace3, two3, three3, four3, five3, six3, seven3, eight3, nine3, ten3, jack3, queen3, king3]
diamonds = [ace4, two4, three4, four4, five4, six4, seven4, eight4, nine4, ten4, jack4, queen4, king4]


# create a class for players
class Player:
    def __init__(self, bet_sum, hits, hand_value):

        self.bet_sum = bet_sum
        self.hits = hits
        self.hand_value = hand_value


dealer = Player(0, 0, 0)    # create a dealer player
user = Player(0, 0, 0)      # create a user player


def draw():  # define the function for drawing card

    x = randrange(4)  # generate a random to select a class
    y = randrange(13)   # generate a random to select a card from the random;y selected suit

    if x == 0:
        print("The", spades[y].card, spades[y].suit)  # if spades suit is drawn
        draw.drawn_value = spades[y].value     # variable for value of drawn cards to add to user.hand_value
    elif x == 1:
        print("The", hearts[y].card, hearts[y].suit)  # if spades suit is drawn
        draw.drawn_value = hearts[y].value
    elif x == 2:
        print("The", clubs[y].card, clubs[y].suit)     # if clubs suit is drawn
        draw.drawn_value = clubs[y].value
    elif x == 3:
        print("The", diamonds[y].card, diamonds[y].suit)  # if diamonds suit is drawn
        draw.drawn_value = diamonds[y].value


def flipped_card_draw():  # draws the dealers second card  without printing what it is.
    x = randrange(4)  # generate a random to select a class
    y = randrange(13)   # generate a random to select a card from the random;y selected suit

    if x == 0:
        # if spades suit is drawn
        flipped_card_draw.drawn_value = spades[y].value    # variable for value of drawn cards to add to user.hand_value
        flipped_card_draw.drawn_card = ("The", spades[y].card, spades[y].suit)
    elif x == 1:
        # if spades suit is drawn
        flipped_card_draw.drawn_value = hearts[y].value
        flipped_card_draw.drawn_card = ("The", hearts[y].card, hearts[y].suit)
    elif x == 2:
        # if clubs suit is drawn
        flipped_card_draw.drawn_value = clubs[y].value
        flipped_card_draw.drawn_card = ("The", clubs[y].card, clubs[y].suit)
    elif x == 3:
        # if diamonds suit is drawn
        flipped_card_draw.drawn_value = diamonds[y].value
        flipped_card_draw.drawn_card = ("The", diamonds[y].card, diamonds[y].suit)


def deal():  # define a function for dealing cards at the start of the round

    # User Draw
    print("You're cards are:")
    for t in range(2):  # draw 2 cards for user
        draw()
        user.hand_value += draw.drawn_value     # add value of drawn card to user's hand value
    print("(The value of your hand is:", user.hand_value, ")")
    print()   # add space between blocks of text for readability

    if user.hand_value == 21:   # if player has blackjack skip to winner
        print("You have Blackjack!")
        winner()

    # Dealer Draw
    print("The Dealer's cards are:")
    draw()
    dealer.hand_value += draw.drawn_value   # add dealer's cards to their hand value
    print("and a flipped card")
    print("(The visible value of the dealer's hand is:", dealer.hand_value, ")")
    flipped_card_draw()
    dealer.hand_value += flipped_card_draw.drawn_value
    print()

    if dealer.hand_value == 21:  # if dealer has blackjack skip to winner
        print("Dealer has Blackjack!")
        winner()


def game_loop():    # crates the loop the game functions will to run in
    loop = 1
    while loop == 1:
        bet()
        deal()
        ask()
        winner()


def ask():  # ask if user wants to hit or stay
    ask = input("would you like to: Hit or Stay? (h/s)")

    #  take the users input
    if ask == 'h':
        hit()
    elif ask == 's':
        stay()


def hit():  # define a function to hit, up to three times
    if user.hits < 3:   # check that hits doesn't equal 3
        print("You drew the:")
        draw()  # draws card
        user.hand_value += draw.drawn_value     # add drawn card to hand value
        user.hits += 1  # add 1 to number of hits
        print("The value of your hand is:", user.hand_value)  # show users hand value after a new card is drawn
        check_user_bust()   # check if the user's hand value is over 21 or not
        ask()   # ask the user if they'd like to hit, or stay
    else:
        print("You're out of hits.")    # let the user know when they're out of hits
        stay()  # begin the dealers turn


def bet():      # define a function for placing bets and reset user and dealer values
    print("You have: $", user.bet_sum)  # show the user their wallet
    bet.bet_value = (input('How much would you like to bet?'))  # take the users bet and convert it from str to int

    while True:
        try:
            bet.bet = eval(bet.bet_value)     # saves their bet for later use

            user.hand_value = 0         # resets the users hand value
            user.hits = 0               # resets the users hits

            dealer.hand_value = 0       # resets the dealers hand value
            dealer.hits = 0             # resets the dealers hits
            break

        except:
            print("Invalid bet. Try again.")
            bet()


def winner():   # checks who won the game based on hand value or if they went bust
    if dealer.hand_value > 21:
        print("User wins. You've won: $", bet.bet)
        user.bet_sum += bet.bet

    elif user.hand_value > 21:
        print("Dealer wins. You've lost: $", bet.bet)
        user.bet_sum -= bet.bet

    elif dealer.hand_value > user.hand_value:
        print("Dealer wins. You've lost: $", bet.bet)
        user.bet_sum -= bet.bet

    elif user.hand_value > dealer.hand_value:
        print("User wins. You've won: $", bet.bet)
        user.bet_sum += bet.bet

    elif user.hand_value == dealer.hand_value:
        print("It's a draw")

    again = input("Would you like to play again? (y/n")  # asks if they want to play again after the winner is decided

    if again == "y":    # if yes game loop function runs again
        game_loop()

    elif again == "n":  # if no, exit game
        exit()


def stay():     # function that begins dealers turn and hits until dealers hand is greater than users.
    if dealer.hits < 3:  # ensures dealers hits less than 3            # qualifiers for dealer to draw a card (below)
        print("The dealers flipped card was", flipped_card_draw.drawn_card)
        while dealer.hand_value <= user.hand_value and dealer.hits < 3:
            if dealer.hand_value < 17:
                print("The dealer drew:")
                draw()  # Draws a card if users hand is better than dealers and dealers hits less than 3
                dealer.hand_value += draw.drawn_value   # adds dealers new card to his hand
                dealer.hits += 1    # adds one to the dealers hits value when he draws a card
                print("The value of the dealer's hand is:", dealer.hand_value)  # show the user the dealers hand per hit
                check_dealer_bust()  # checks to see if the dealers hand is over 21

            else:   # when dealer is out of hits it skips to who won the game
                print("Dealer is done taking hits.")
                winner()


def check_user_bust():  # if user's busts it skips to dealer wins
    if user.hand_value > 21:
        print("You've gone bust")
        winner()


def check_dealer_bust():    # if dealer busts it skips to user wins
    if dealer.hand_value > 21:
        print("Dealer has gone bust")
        winner()


def rules():    # function used to print the rules before initiating the game loop
    user.bet_sum += 100  # Gives the user $100 to start with (It felt weird to me be able to bet without money.)
    print("Blackjack")
    print()
    print("Rules: 2 cards are drawn at start for you and the dealer, dealer starts with a card faced up and faced down")
    print("Aces are worth 11, face cards are worth 10. The goal is 21, don't go over. to respond to a prompt:")
    print("type one of the letters in the parenthesis. Enter your bets without a $. You start with $100.")
    print()


rules()
game_loop()