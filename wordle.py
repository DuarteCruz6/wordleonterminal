from english_words import english_words_lower_alpha_set
import random 
import os
import time

#Choose the random word
def gettheword():
    global chosenword
    words = list(english_words_lower_alpha_set)
    chosenword = random.choice(words)
    game()

#Now, let´s play
def game():
    hiddenword = "_"*len(chosenword)
    print(f"The word is {hiddenword} ({len(chosenword)} letters).")
    tries = 1
    while True:
        time.sleep(0.5)
        guess = input(f"Try {tries}/{len(chosenword)}: What do you think the word is? ").lower()
        if len(guess) != len(chosenword):
            print(f"Invalid option. The word has {len(chosenword)} letters.")
        elif guess not in list(english_words_lower_alpha_set):
            print(f"Please guess with an english word.")
        else:
            tries += 1
            j = 0
            for i in guess:
                if i in chosenword:
                    try:
                        if guess.index(i,j,len(guess)) == chosenword.index(i,j,len(chosenword)):
                            print(f"The letter {i} is in the word and in the correct place.")
                            time.sleep(2)
                        else:
                            print(f"The letter {i} is in the word but not in the correct place.")
                            time.sleep(2)
                    except:
                            print(f"The letter {i} is in the word but not in the correct place.")
                            time.sleep(2)
                    j += 1
                else:
                    print(f"The letter {i} isn´t in the word.")
                    time.sleep(1)

            if guess == chosenword:
                print(f"Congrats! You got it right. The word was {chosenword}.")
                time.sleep(1)
                replay = input("Do you want to play again? ").lower()
                if replay == "yes":
                    os.system("clear")
                    gettheword()
                    break
                else:
                    os.system("clear") 
                    print("Thanks for playing!")
                    time.sleep(1.2)
                    os.system("clear") 
                    break
            
            if tries > len(chosenword):
                print(f"You exceed the number of possible tries. The word was {chosenword}.")
                time.sleep(1)
                replay = input("Do you want to play again? ").lower()
                if replay == "yes":
                    os.system("clear")
                    gettheword()
                    break
                else:
                    os.system("clear") 
                    print("Thanks for playing!")
                    time.sleep(1.2)
                    os.system("clear") 
                    break

gettheword()