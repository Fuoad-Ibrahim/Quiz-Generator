from utility import util
import quiz_generator
import random

if __name__ == "__main__":
    print("Welcome message\n")

    # Get the quiz type from the user
    quiz_type = input("Enter 1 for ExactAnswer and 2 for ShowAnswer: \n")
    quiz_type.replace(' ', '')
    while quiz_type != '1' and quiz_type != '2':
        print("Invalid entry: Must enter 1 for ExactAnswer or 2 for ShowAnswer.")
        quiz_type = input("Enter 1 for ExactAnswer and 2 for ShowAnswer: \n")
        quiz_type.replace(' ', '')

    # Extra option for quiz type 2
    quiz_show_option = None
    if quiz_type == '2':
        quiz_show_option = input("Enter 1 if you would like to see correct answer after answering" \
              " each question or enter 2 if you would like to see correct" \
              " answers at the end: \n")
    
    # Create the quiz
    print("Let's create your quiz!\n")
    name = input('What would you like to name your quiz?\n')
    quiz = quiz_generator.QuizGenerator(name)
    quiz.create_quiz()

    # Get the users answers
    users_answers = {}
    ques_and_ans = quiz.get_questions_and_answers()
        
    ques_num = 1
    keys = list(ques_and_ans.keys()) 
    random.shuffle(keys)
    print("We Will Now Begin The Quiz!\n")
    for key in keys:

        # Print question
        print(f"Question #{ques_num}: {key}\n")

        # Get answer
        answer = input("Enter answer: \n")

        # To print the correct answer directly after the users answers
        if quiz_show_option == '1':
            print(f"Correct Answer: {ques_and_ans[key]}\n")

        users_answers[key] = answer
        ques_num += 1

    # Agregate quiz score and print results
    if quiz_type == '1':
        util.start_quiz_exact(quiz, users_answers)

    elif quiz_type == '2' and quiz_show_option == '2':
        util.start_quiz_show(quiz, users_answers)
