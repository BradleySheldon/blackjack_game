# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 23:18:22 2024

@author: Bradley Sheldon
"""

import random
import time

# ASCII art for card values
card_art = {
    '2': "  _____\n |2    |\n |     |\n |    2|\n  ‾‾‾‾‾",
    '3': "  _____\n |3    |\n |     |\n |    3|\n  ‾‾‾‾‾",
    '4': "  _____\n |4    |\n |     |\n |    4|\n  ‾‾‾‾‾",
    '5': "  _____\n |5    |\n |     |\n |    5|\n  ‾‾‾‾‾",
    '6': "  _____\n |6    |\n |     |\n |    6|\n  ‾‾‾‾‾",
    '7': "  _____\n |7    |\n |     |\n |    7|\n  ‾‾‾‾‾",
    '8': "  _____\n |8    |\n |     |\n |    8|\n  ‾‾‾‾‾",
    '9': "  _____\n |9    |\n |     |\n |    9|\n  ‾‾‾‾‾",
    '10': "  _____\n |10  o|\n |     |\n |o   10|\n  ‾‾‾‾‾",
    'J': "  _____\n |J  ww|\n |  {)|\n |ww  J|\n  ‾‾‾‾‾",
    'Q': "  _____\n |Q  ww|\n |  {(|\n |ww  Q|\n  ‾‾‾‾‾",
    'K': "  _____\n |K  WW|\n |  {)|\n |WW  K|\n  ‾‾‾‾‾",
    'A': "  _____\n |A _  |\n | ( ) |\n |  T  A|\n  ‾‾‾‾‾"
}

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [{'suit': suit, 'value': value} for suit in suits for value in values]

def deal_card(deck):
    if len(deck) == 0:
        return None
    return deck.pop(random.randint(0, len(deck) - 1))

def get_card_value(card, current_total):
    value = card['value']
    if value in ['J', 'Q', 'K']:
        return 10
    if value == 'A':
        return 11 if current_total + 11 <= 21 else 1
    return int(value)

def print_hand(hand, hidden=False):
    # Assuming each card's ASCII art is 7 characters wide
    card_width = 7
    hand_art_lines = []
    for i, card in enumerate(hand):
        if i == 0 and hidden:
            card_lines = [
                "  _____ ",
                " |////| ",
                " |////| ",
                " |////| ",
                "  ‾‾‾‾‾ "
            ]
        else:
            card_lines = card_art[card['value']].split('\n')
        hand_art_lines.append(card_lines)

    # Print each line of the cards side by side
    for i in range(5):  # Each card's ASCII art has 5 lines
        for card_lines in hand_art_lines:
            print(f"{card_lines[i]:<{card_width}}", end='  ')  # Adjust spacing if necessary
        print()  # New line at the end of each card row

# Ensure the rest of your game logic is intact and calls `print_hand` where needed


def calculate_hand_total(hand):
    total = 0
    for card in hand:
        total += get_card_value(card, total)
    return total

def main():
    deck = create_deck()
    random.shuffle(deck)
    
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    print("Dealer's hand:")
    print_hand(dealer_hand, hidden=True)
    
    print("\nYour hand:")
    print_hand(player_hand)
    
    player_total = calculate_hand_total(player_hand)
    while player_total < 21:
        action = input("\nDo you want to (h)it or (s)tand? ").lower()
        if action == 'h':
            new_card = deal_card(deck)
            player_hand.append(new_card)
            print("\nYour new card:")
            print_hand([new_card])  # Print just the new card
            player_total = calculate_hand_total(player_hand)
            print("\nYour hand:")
            print_hand(player_hand)  # Reprint the entire hand side by side
            if player_total > 21:
                print("Bust! Your total is over 21.")
                break
        elif action == 's':
            break

    if player_total <= 21:
        print("\nDealer's hand revealed:")
        print_hand(dealer_hand)
        dealer_total = calculate_hand_total(dealer_hand)
        while dealer_total < 17:
            time.sleep(2)
            new_card = deal_card(deck)
            dealer_hand.append(new_card)
            print("\nDealer draws:")
            print_hand([new_card])  # Print just the new card
            dealer_total = calculate_hand_total(dealer_hand)
            print("\nDealer's hand:")
            print_hand(dealer_hand)  # Reprint the dealer's hand side by side

        print(f"\nDealer's total: {dealer_total}")

    print(f"\nYour total: {player_total}")
    if player_total > 21 or (dealer_total <= 21 and dealer_total > player_total):
        print("Dealer wins.")
    elif dealer_total > 21 or player_total > dealer_total:
        print("You win!")
    else:
        print("It's a tie.")

if __name__ == "__main__":
    main()

