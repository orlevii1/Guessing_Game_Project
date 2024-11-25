import random
import pygame

pygame.mixer.init()
try:
    pygame.mixer.music.load("Dramatic Song.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
except pygame.error as e:
    print("Music file could not be loaded. Please check the file path and format.")
    print("Error:", e)

ai_win = player_win = 0
ans = "Y"

while ans == "Y":
    number = random.randint(1, 20)
    print("""
    *************************************
                Guessing Game
    *************************************
        Pick number of tries you want:
      Easy - 10 | Medium - 5 | Hard - 3
    *************************************
        Guess the random number (1-20).
    *************************************
    """)

    try:
        dif = int(input("Pick difficulty level: 1-Easy 2-Medium 3-Hard: "))
        bet1 = int(input("Place your bet: "))

        if dif == 1:
            tries, bet_multiplier = 10, 1.5
        elif dif == 2:
            tries, bet_multiplier = 5, 2
        elif dif == 3:
            tries, bet_multiplier = 3, 5
        else:
            print("Invalid difficulty choice. Defaulting to Easy.")
            tries, bet_multiplier = 10, 1.5

        bet = bet1 * bet_multiplier

    except ValueError:
        print("Invalid input! Defaulting to Easy.")
        tries, bet, bet_multiplier = 10, 0, 1.5

    for i in range(tries):
        while True:
            try:
                guess = int(input("Guess the number (1-20 Only): "))
                if 1 <= guess <= 20:
                    break
                else:
                    print("Your number is invalid! Please enter a number between 1 and 20.")
            except ValueError:
                print("Invalid input! Please enter a valid number between 1 and 20.")

        if guess == number:
            print(f"{guess} is the correct number!")
            print(f"You won {bet} Shekels")
            player_win += 1
            break
        elif guess > number:
            print("Your number is higher.")
        else:
            print("Your number is lower.")
    else:
        ai_win += 1
        print(f"You Lost! The number was: {number}")

    ans = input("Would you like to try again? (Y/N): ").upper()
    if ans == "Y":
        print("Starting Again!")

if ans == "N":
    print("No problem, see you next time!")

print(f"AI Wins: {ai_win} | Player Wins: {player_win}")