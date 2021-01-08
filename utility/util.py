def start_quiz_exact(quiz, users_answers) -> None:
    """Quiz users using questions and answers from quiz object. This function
    records correct answers and provides a grade after completing.

    Args:
        quiz(object): QuizGenerator object.
    """

    for key, value in users_answers.items():

        org_ans = quiz.questions_and_answers[key].replace(' ', '').lower()
        user_ans = value.replace(' ', '').lower()

        if org_ans == user_ans:
            quiz.increment_score()
            quiz.add_to_score_sheet(key, "Correct!")
        else:
            quiz.add_to_score_sheet(key, "InCorrect")

    print("Your total score is: ", quiz.score, "/", len(users_answers))
    print(quiz.score_sheet)


def start_quiz_show(quiz, users_answers) -> None:
    """Quiz users using questions and answers from quiz object. Users can choose
    to show correct answer after each question they answer or show all after
    completing quiz.

    Args:
        quiz(object): QuizGenerator object.
    """

    ques_num = 1

    print("--- Results ---\n")
    for key, value in quiz.questions_and_answers.items():

        print(f"Question #{ques_num}: {key}\n")
        print(f"Your Answer: {users_answers[key]}")
        print(f"Correct Answer: {value}\n")
        ques_num += 1
