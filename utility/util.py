import random


def start_quiz_exact(quiz) -> None:
    """Quiz users using questions and answers from quiz object. This function
    records correct answers and provides a grade after completing.

    Args:
        quiz(object): QuizGenerator object.
    """
    count = quiz.question_amount
    ques_and_ans = quiz.questions_and_answers.copy()

    while count > 0:
        key = random.choice(list(ques_and_ans.keys()))
        val = ques_and_ans[key].replace(' ', '').lower()  #removes whitespace and makes string lower case
        del ques_and_ans[key]
        print(key)
        answer = input("Enter answer: ")
        answer.replace(' ', '').lower()
        print()

        if answer == val:
            quiz.score += 1
            quiz.score_sheet[key] = "Correct!"
        else:
            quiz.score_sheet[key] = "InCorrect"
        count -= 1
    print()
    print("Your total score is: ", quiz.score, "/", quiz.question_amount)
    print(quiz.score_sheet)


def start_quiz_show(quiz) -> None:
    """Quiz users using questions and answers from quiz object. Users can choose
    to show correct answer after each question they answer or show all after
    completing quiz.

    Args:
        quiz(object): QuizGenerator object.
    """
    count = quiz.question_amount
    ques_and_ans = quiz.questions_and_answers.copy()
    user_input = input("Enter 1 if you would like to see correct answer after answering" \
              " each question or enter 2 if you would like to see correct" \
              " answers at the end: ")
    print()
    users_answers = {}
    ques_num = 1

    if user_input == '1':
        while count > 0:
            key = random.choice(list(ques_and_ans.keys()))
            print(f"Question #{ques_num}: {key}\n")
            answer = input("Enter answer: ")
            users_answers[key] = answer
            print(f"Correct Answer: {ques_and_ans[key]}\n")
            del ques_and_ans[key]
            ques_num += 1
            count -= 1

    elif user_input == '2':
        while count > 0:
            key = random.choice(list(ques_and_ans.keys()))
            del ques_and_ans[key]
            print(key)
            answer = input("Enter answer: ")
            users_answers[key] = answer
            print()
            count -= 1
        print("--- Results ---\n")
        for ques in quiz.questions_and_answers:
            print(f"Question #{ques_num}: {ques}\n")
            print(f"Your Answer: {users_answers[ques]}")
            print(f"Correct Answer: {quiz.questions_and_answers[ques]}\n")
            ques_num += 1


def validate_quiz_type() -> str:
    """Docstring"""

    quiz_type = input("Enter 1 for ExactAnswer and 2 for ShowAnswer: ")
    quiz_type.replace(' ', '')
    print()

    while quiz_type != '1' and quiz_type != '2':
        print("Invalid entry: Must enter 1 for ExactAnswer or 2 for ShowAnswer.\n")
        quiz_type = input("Enter 1 for ExactAnswer and 2 for ShowAnswer: ")
        quiz_type.replace(' ', '')
        print()

    return quiz_type
