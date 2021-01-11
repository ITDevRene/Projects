# Let's create a Quiz

from Question import Question

# Represents the prompts of the question
prompts = ["Which of this characters can be used in python for naming a variable?\n(a)# \n (b)_ \n (c)%"]

#  Creates a list of questions
questions = [Question(prompts[0], 'b')]

# Will store the questions that the user needs to review because
# they got it wrong.
questions_to_review = []

for question in questions:
    answer = input(question.prompt + "\n")

    if answer == question.answer:
        print("Your answer was correct!")
    else:
        print("Your answer was not correct!")

        # Add the questions to the list of questions to review
        # because the user got it wrong
        questions_to_review.append(question)
