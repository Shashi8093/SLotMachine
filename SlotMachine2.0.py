# Swayam Suresh Thripathy - UCSE22043
# Somya Sworupa Dash  - UCSE22039
# Shabyasachi Thripathy - UCSE22030
# Shashikanta Chinara - UCSE22063
# Aryan Divyadarshee - UCSE22060

import random
import numpy as np
import time

# Define characters for the slot machine
characters = ['Apple', 'Gold', 'Pig', 'Cherry', 'Banana', 'Diamond']

# Set the initial balance
balance = 1000  # You can customize the initial balance
min_bet = 10    # You can customize the minimum bet amount

# Adjusted character odds
character_odds = {
    'Apple': 5,
    'Gold': 4,
    'Pig': 3,
    'Cherry': 2,
    'Banana': 3,
    'Diamond': 4
}

# Function to spin the slot machine
def spin_slot_machine():
    result = [random.choice(characters) for _ in range(3)]
    return result

# Function to calculate winnings
def calculate_winnings(result, bets):
    total_winnings = 0
    for character, bet in bets.items():
        if all(c == character for c in result):
            total_winnings += bet * character_odds[character]
    return total_winnings

# Function to display the slot machine
def display_slot_machine(result):
    print("Slot Machine:")
    for _ in range(3):
        print("  |  ".join(random.choice(characters) for _ in range(3)))
        time.sleep(1)
    print("Slot Machine Result:", result)

# Main game loop
while balance > 0:
    print("Welcome to the Slot Machine!")
    print(f"Your current balance: {balance}")
    print("Characters to choose from:")
    for index, character in enumerate(characters, 1):
        print(f"{index}. {character}")

    bets = {}
    while True:
        choice = int(input("Choose a character to bet on (1-6, 0 to stop selecting characters): "))
        if choice == 0:
            break
        if choice < 1 or choice > 6:
            print("Invalid choice. Please select a valid character.")
            continue
        character = characters[choice - 1]
        bet = int(input(f"Place a bet on {character}: "))
        if bet < min_bet:
            print(f"Minimum bet amount not met for {character}. Please try again.")
            continue
        if bet > balance:
            print("Insufficient balance. Please place a lower bet.")
            continue
        bets[character] = bet

    if not bets:
        print("No bets placed. Thanks for playing!")
        break

    balance -= sum(bets.values())

    result = spin_slot_machine()
    display_slot_machine(result)

    winnings = calculate_winnings(result, bets)
    balance += winnings

    if winnings > 0:
        print(f"Congratulations! You won {winnings}!")
    else:
        print("Sorry, you lost.")

# End of the game
print("Out of funds. Thanks for playing!")
