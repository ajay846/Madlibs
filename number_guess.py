#guess the num

import random
from time import sleep

number = [1,2,3,4,5,6,7,8,9,0,10,20,30,40,50,60,70,80,90,100,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,91,91,92,93,94,95,96,97,98,99]

num_of_players = input("Enter (1) if single player, enter (2) if 2 players\n")

if num_of_players =='1' or num_of_players =='2':
    if num_of_players == '1':
        print("Rules of the game:\n1. You will have unlimited chances to guess the number\n2. The number to guessed will be generated be the computer\n")
        sleep(1)
        def g1():
            s_n = input("To start the game press 's'\n")
            if s_n == 's' or s_n == 'S':
                secret_num = random.randrange(0,50)
                print(secret_num)
                count = 0
                while True:
                    guess = int(input("Enter your guess number: "))
                    if guess == secret_num:
                        print("YOU WON THE GAME! And you've tried '"+str(count)+"' times to get the num right")
                        g1()
                    elif guess <= secret_num or secret_num >= guess:
                        print("Your guessed num is less than the secret num")
                        count += 1
                    elif guess >= secret_num or secret_num <= guess:
                        print("Your guessed num is more tham the secret num")
                        count += 1

'''
    elif num_of_players == '2':
        print("Rules of the game:\n1. One player will give a integer number and other player shall guess it\n2. The player giving the number shall set the guess limit\n")
#       global count
#       count = input("Enter the number of chances your opponent gets to guess the number\n")
#        guess_counter = 0
#        global guess_given
        guess_given = input("Enter the number to be guessed\n")
        running = True

        while running == True:
            guess = input("Enter the guessed number\n")

            if guess <= guess_given:
                print("Your guessed number is less than the given number")
                print("You have used up "+str(guess_counter))

            elif guess >= guess_given:
                print("Your guessed number is more than the given number")
#                guess_counter += 1
                print("You have used up ")

            elif guess == guess_given:
                print("YOU WIN THE GAME!")

            while guess_counter == count:
                running = False
'''

else:
    print("Number of players cannot be more than 2 nor less than 1")
g1()
