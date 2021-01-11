# This program creates a file where the questions will be save

# Let's input a title for the quiz file from the user.
# Name of the file should be short
name_of_quiz = input("Give it a name to the quiz") # For example "Chapter 1"

# Let's create a text file with that name
quiz_file = open(name_of_quiz, 'w')

# Works as a flag for the user to stop adding questions
stop_adding = False

# Stores the question
question = ""

while not stop_adding:
    # Get the questions from the user
    question = input("Question:")

    # Write the question to the file

    # Write the answer to the file

    # Ask the user if they want to add more questions 

# Let's close the file
quiz_file.close()