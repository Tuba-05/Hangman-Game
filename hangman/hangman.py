from string import ascii_lowercase
import time, random

# Main game function
def game():
    print("1: Admin \n2: User \n3: Exit \nYou are playing as: ", end="")
    user_input = int(input(""))
    
    # Handle different roles
    if user_input == 1:
        time.sleep(1.5)
        Admin()  # Admin mode
    elif user_input == 2:
        time.sleep(1.5)
        User()   # User mode (play game)
    elif user_input == 3:
        time.sleep(1.5)
        print("* EXIT FROM GAME *")
        exit()   # Exit the game
    else: 
        time.sleep(1.5)
        print("Invalid choice")  # Invalid input

# Admin mode functionalities
def Admin():
    print("* ADMIN MODE * \n1: Add a word in text file \n2: Reset the highscore \n3: Play hangman game")
    time.sleep(1.5) 
    option = int(input("Enter your choice: "))
    
    # Option to add a new word
    if option == 1:
        new_word = input("Enter the new word: ")
        file1 = open("words.txt", 'a+')
        file1_ = file1.read().split()
        if new_word in file1_:
            print("The word already exists in file.")
        else:
            file1.write(new_word)
            print("The word has successfully written in file.")    
        file1.close()

    # Option to reset highscore
    elif option == 2:
        file2 = open("highscore.txt", 'w')
        file2.close()
        print("Highscore reset.")

    # Option to directly play the game
    elif option == 3:
        time.sleep(1.5)
        User()

    else:
        time.sleep(1.5)
        print("Invalid choice")        

# User mode (main hangman game logic)
def User():
    player = input("Enter your name: ")
    time.sleep(1.5)
    print(f"* PLAYER MODE * \nWelcome To Hangman {player}" )

    # Read all words from the file
    file1 = open("words.txt", 'r')
    words_file = file1.read().split()
    file1.close()

    # Randomly select a word
    word = random.choice(words_file)
    secret_word = len(word) * '_'
    time.sleep(1.5)
    print("I am thinking of a word which is", len(word), "letters long.\nGUESS THE SECRET WORD.")

    guesses = 6    # Initial number of guesses
    warnings = 3   # Initial number of warnings
    time.sleep(1.5)
    print("Guesses =", guesses, "\nWarnings =", warnings)

    # List of available letters
    alphabets = [i for i in ascii_lowercase]
    time.sleep(1.5)
    print("available letters = ", "".join(alphabets))
    time.sleep(1.5)
    print(secret_word)

    # Main game loop
    while guesses != 0:
        letter = input("Guess a letter: ")

        if letter in alphabets:
            # Correct letter guessed
            if letter in word:
                for blanks in range(len(word)):
                    if word[blanks] == letter:
                        secret_word = secret_word[:blanks] + letter + secret_word[blanks+1:]
                time.sleep(1.5)        
                print(secret_word, "\nGuesses =", guesses, " and Warnings =", warnings)  
                alphabets.remove(letter)
                print("available letters = ", "".join(alphabets))
            else:
                # Incorrect letter guessed
                if letter in ['a', 'e', 'i', 'o', 'u']:
                    guesses -= 2  # Vowels cost more guesses
                else:
                    guesses -= 1
                time.sleep(1.5)    
                print(secret_word, "\nGuesses =", guesses, " and Warnings =", warnings)  
                alphabets.remove(letter)
                print("available letters = ", "".join(alphabets))

        else:
            # Invalid character guessed (not in alphabet)
            if letter in ['a', 'e', 'i', 'o', 'u']:
                guesses -= 2
            else:
                guesses -= 1
            warnings -= 1
            if warnings < 0:
                warnings = 0
            time.sleep(1.5)    
            print(secret_word, "\nGuesses =", guesses, " and Warnings =", warnings)  
            print("available letters = ", "".join(alphabets))              
        
        # Game ends if word is fully guessed
        if secret_word == word:
            break            

    time.sleep(1.5)

    # Display game result
    if secret_word == word:
        print("CONGRATULATIONS! You guessed the word correctly. \nThe word is", secret_word)
    else:
        print("OOPs! You guessed wrong. \nThe correct word is", word)    

    # Score calculation
    score = guesses * len(word)

    # Append score to file
    file3 = open('scores.txt', 'a+')
    file3.write(f"{player} = {str(score)}\n")
    file3.seek(0)
    lines = file3.readlines()

    # Find the highest score
    h_score = -1
    for line in lines:
        if '=' in line:
            parts = line.strip().split('=')
            if len(parts) == 2:
                value = int(parts[1])
                if value > h_score:
                    h_score = value
                    file2 = open("highscore.txt", 'w')
                    file2 = file2.write(f"{parts[0]} = {str(h_score)}\n")

    time.sleep(1.5)

    # Show score and highscore
    if score > h_score:
        print('HIGH SCORE!!! Your score is', score)
    else:
        print('* Your score is', score, "*\n* Highscore is", h_score, "*")

    file3.close()

# Start the game
game()
