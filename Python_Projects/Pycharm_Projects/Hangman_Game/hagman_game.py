# This is a hang man game

# A function to change the character in a string
def change_char_at(index, string, new_char):
    # Change the string variable into a list
    string = list(str(string))
    string[index] = new_char

    return "".join(string)


# Returns a list with the index of the character in a string
# the length of the list depends on how many occurrences of the
# the character are in the string
def return_indexes_of(character, string):

    # For saving the indexes
    indexes = []

    # Represent an index
    i = 0

    for char in string:
        if char == character:
            # Saving the index in a list
            indexes.append(i)

        # Incrementing the index variable everytime the code in the loop
        # executes for appending the value of index, which will be an index of
        # the character specified in the parameter
        i += 1

    return indexes


# Prompt one player for a word that the other player will have to guess
word_to_guess = input("Enter a word for the other player to guess:")

# Represents the word entered by the first player but hidden
hidden_word = ""

# Construct the hidden word
for word in word_to_guess:
    if word == " ":
        hidden_word = hidden_word + " "
    else:
        hidden_word = hidden_word + "_"

# Revealing only the first character of the word to guess.
# Changes the character at the index specified by the first parameter
# of the string specified by the second parameter with the character
# in the third parameter
hidden_word = change_char_at(0, hidden_word, word_to_guess[0])

# Prompt the other player to guess
print("Now is time for the other player to guess the word.")
print(hidden_word)

# Stores the attempts
attempts = 5

# If the word or phrase is guessed then this will be True
guessed = False

while attempts > 0 and not guessed:
    # Stores the letter guessed by the player that guesses
    letter_to_guess = input("Guess:")[0]

    # Reveal the letter if word_to_guess has it
    if letter_to_guess in word_to_guess:

        # Returns a list of the indexes of a letter in a phrase
        list_of_indexes = return_indexes_of(letter_to_guess, word_to_guess)

        for index in list_of_indexes:
            hidden_word = change_char_at(index, hidden_word, letter_to_guess)

        # Replace all letters guessed with "_" to mark them as guessed
        # that the program does not mistakenly look for them
        word_to_guess = word_to_guess.replace(letter_to_guess, "_")

        # Print how many attempts are left if the word has not been guessed
        if not guessed:
            print("You have " + str(attempts) + " attempts.")

    else:
        # One attempt lost
        attempts -= 1

        # Prints how many attempts are left if the word has not been guessed
        if not guessed:
            print("You guessed wrong. You have " + str(attempts) + " attempts.")

    if "_" not in hidden_word:
        print("You guessed the phrase. You won the game!")
        guessed = True

    # Prints the hidden word only when there are attempts left
    if attempts > 0 and not guessed:
        print(hidden_word)

# Prints the game ended
print("\n The game has ended!")
