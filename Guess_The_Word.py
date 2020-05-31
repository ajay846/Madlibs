guess = ['d','o','g']

user_word_guess_1 = 0
user_word_guess_2 = 0
user_word_guess_3 = 0

count_1 = 0
count_2 = 0
count_3 = 0

run = True

print("\nGuess The Word Stored\nYou will have 10 chances to guess each alphabet of the secret word\nThe word here relates to an animal")


while run == True:
    user_word_guess_1 = input("Enter the guess of the 1st alphabet: \n")
    count_1 += 1
    print("You are out of "+str(count_1)+" guesses and left with "+str(10-count_1)+" guesses\n")
    if count_1 >= 10:
        run = False
    if user_word_guess_1 == guess[0]:
        print("Your 1st alphabet of the secret word is correct!\nNow proceed to the 2nd alphabet\n")

        while run == True:
            user_word_guess_2 = input("Enter the guess of the 2nd alphabet: \n")
            count_2 += 1
            print("You are out of "+str(count_2)+" guesses and left with "+str(10-count_2)+" guesses\n")
            if count_2 >= 10:
                run = False
            if user_word_guess_2 == guess[1]:
                print("Your 2nd alphabet of the secret word is correct!\nNow proceed to the 3rd alphabet\n")

                while run == True:
                    user_word_guess_3 = input("Enter the guess of the 3rd alphabet: \n")
                    count_3 += 1
                    print("You are out of "+str(count_3)+" guesses and left with "+str(10-count_3)+" guesses\n")
                    if count_3 >= 10:
                        run = False
                    if user_word_guess_3 == guess[2]:
                        print("Your guesses were correct! The secret word stored was '"+str(guess)+"'")





















