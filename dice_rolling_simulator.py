import random
import os
import time

# Function to simulate a dice roll
def roll_dice():
    return random.randint(1, 6)

# Main function to prompt the user and simulate dice rolls
def main():
    print("Dice Rolling Simulator - Roll a 6-sided dice")
    while True:
        input("Press Enter to roll the dice (or 'exit' to quit): ")
        result = roll_dice()
        print(f"The result of your dice roll is: {result}")
        continue_prompt = input("Do you want to roll again? (yes/no): ").lower()
        if continue_prompt != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
