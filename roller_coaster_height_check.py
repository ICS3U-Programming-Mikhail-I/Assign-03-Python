#!/usr/bin/env python3
#Author Mikhail Ibrahim
# Date: Apr 9, 2025
# Description: A Python program that determines if a user is tall enough
# to go on a roller coaster based on a minimum height requirement of 137 cm.


def main():
    # Display greeting message
    print("🎢 Welcome to the Canada’s Wonderland Roller Coaster Height Checker!")

    try:
        # Prompt the user to enter their height in centimeters
        height = int(input("Please enter your height in cm: "))

        # Decision structure to check height eligibility
        if height >= 137:
            print("✅ You can go on the roller coaster!")
        else:
            print("❌ Sorry, you are not tall enough to go on the ride.")

    except ValueError:
        # Handle invalid (non-numeric) inputs
        print("⚠️ Invalid input. Please enter a whole number in centimeters.")


# Call the main function
if __name__ == "__main__":
    main()
