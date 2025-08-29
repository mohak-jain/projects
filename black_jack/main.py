import random
import sys

Rules = '''
Rules: 
Try to get as close to 21 without going over.
Kings, Queens, and Jacks are worth 10 points.
Aces are worth 1 or 11 points.
Cards 2 through 10 are worth their face value.
(H)it to take another card.
(S)tand to stop taking cards.
On your first play, you can (D)ouble down to increase your bet
but must hit exactly one more time before standing.
In case of a tie, the bet is returned to the player.
The dealer stops hitting at 17.
'''

#setting up constants ♥ ♦ ♠ ♣
hearts = chr(9829) 
diamonds = chr(9830)
spades = chr(9824)
clubs = chr(9827)
# print(Hearts, Diamonds, Spades, Clubs)

suits = [hearts, diamonds, spades, clubs]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck_blueprint = [f"{rank}{suit}" for suit in suits for rank in ranks]

player_hand = []
dealer_hand = []

def shuffle_deck():
    deck = deck_blueprint[:]
    random.shuffle(deck)
    return deck

def deal_initial_hands():
    deck = shuffle_deck()
    player = [deck.pop(), deck.pop()]
    dealer = [deck.pop(), deck.pop()]
    return player, dealer, deck

def calculate_hand_value(hand):
    total = 0
    aces = 0

    for card in hand:
        rank = card[:-1]  # Remove suit
        if rank in ["K", "Q", "J"]:
            total += 10
        elif rank == "A":
            total += 11
            aces += 1
        else:
            total += int(rank)

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total

def hit(hand, deck):
    hand.append(deck.pop())

def stand(deck):
    print("\nDealer's hand:", dealer_hand)
    while calculate_hand_value(dealer_hand) < 17:
        hit(dealer_hand, deck)
        print("Dealer hits...")
        print("Dealer's hand:", dealer_hand)
        print("Dealer's score:", calculate_hand_value(dealer_hand))

    player_score = calculate_hand_value(player_hand)
    dealer_score = calculate_hand_value(dealer_hand)

    print("\nFinal Results:")
    print("Your score:", player_score)
    print("Dealer's score:", dealer_score)

    if dealer_score > 21 or player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("Dealer wins.")
    else:
        print("It's a tie!")
def main():
    # print(Rules)
    global player_hand, dealer_hand
    player_hand, dealer_hand, deck = deal_initial_hands()
    print("\nYour hand: ", player_hand[0], player_hand[1])
    print("Dealer's hand: ", dealer_hand[0], "##")
    print("Your score: ", calculate_hand_value(player_hand))

    while True:
        print("""\n(H)it to take another card.
(S)tand to stop taking cards.""")
        player_input = input("Enter: ").strip().lower()

        if player_input == "h":
            hit(player_hand, deck)
            print("\nYour hand: ", player_hand)
            print("Your score: ", calculate_hand_value(player_hand))
            if calculate_hand_value(player_hand) > 21:
                print("You busted! Dealer wins.")
                return
        elif player_input == "s":
            stand(deck)
            return
        else:
            print("Invalid input. Please enter H or S.")

main()


# Test dealing hands
# if __name__ == "__main__":
#     player_hand, dealer_hand, deck = deal_initial_hands()
#     print("Player's Hand:", player_hand)
#     print("Dealer's Hand:", dealer_hand)
#     print("Cards remaining in deck:", len(deck))
#     print("Player's Score:", calculate_hand_value(player_hand))
#     print("Dealer's Score:", calculate_hand_value(dealer_hand))
