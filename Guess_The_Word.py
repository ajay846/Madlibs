import os
import sys
import keyboard
from time import sleep

main_run = True

while main_run == True:
    user_word_guess_1 = 0
    user_word_guess_2 = 0
    user_word_guess_3 = 0

    count_1 = 0
    count_2 = 0
    count_3 = 0

    delay = 1.5

    run = True

    print("\nGuess The Word Stored\nYou will have 10 chances to guess each alphabet of the secret word\n")

    def split(secret):
        return[char for char in secret]

    clear = lambda: os.system("cls")

    secret = input("Any one player should enter the secret word (The number of characters should not exceed 3)\n")
    clear()
    if len(secret) != 3:
        print("The secrect word must be of only 3 characters not less than that, and cannot be a number!")
        break

    while run == True:
        user_word_guess_1 = input("Enter the guess of the 1st alphabet: \n")
        count_1 += 1
        print("You are out of "+str(count_1)+" guesses and left with "+str(10-count_1)+" guesses\n")
        if count_1 >= 10:
            run = False
        if user_word_guess_1 == secret[0]:
            print("Your 1st alphabet of the secret word is correct!\nNow proceed to the 2nd alphabet\n")
            sleep(delay)
            clear()

            while run == True:
                user_word_guess_2 = input("Enter the guess of the 2nd alphabet: \n")
                count_2 += 1
                print("You are out of "+str(count_2)+" guesses and left with "+str(10-count_2)+" guesses\n")
                if count_2 >= 10:
                    run = False
                if user_word_guess_2 == secret[1]:
                    print("Your 2nd alphabet of the secret word is correct!\nNow proceed to the 3rd alphabet\n")
                    sleep(delay)
                    clear()

                    while run == True:
                        user_word_guess_3 = input("Enter the guess of the 3rd alphabet: \n")
                        count_3 += 1
                        print("You are out of "+str(count_3)+" guesses and left with "+str(10-count_3)+" guesses\n")
                        if count_3 >= 10:
                            run = False
                        if user_word_guess_3 == secret[2]:
                            print("Your guesses were correct! The secret word stored was '"+str(guess)+"'")
                            sleep(delay)
                            clear()