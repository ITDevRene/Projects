# Let's create a Quiz

from Question import Question

# Represents the prompts of the question
prompts = ["Which of this characters can be used in python for naming a variable?\n(a)# \n (b)_ \n (c)%"]

questions = [Question(prompts[0], 'b')]

for question in questions:
    answer = input(question.prompt)

    if answer == question.answer:
        print("Your answer was correct!")
    else:
        print("Your answer was not correct!")