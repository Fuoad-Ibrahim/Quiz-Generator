import random

def start_test_exact(test) -> None:
    """Test users using questions and answers from test object. This function
    records correct answers and provides a mark after completing.

    Args:
        test(object): PracticeTest object.
    """
    count = test.question_amount
    print()
    print("We Will Now Begin The Test!\n")
    d = test.questions_and_answers.copy()

    while count > 0:
        key = random.choice(list(d.keys()))
        val = d[key].replace(' ', '').lower()  #removes whitespace and makes string lower case
        del d[key]
        print(key)
        answer = input("Enter answer: ")
        answer.replace(' ', '').lower()
        print()

        if answer == val:
            test.score += 1
            test.score_sheet[key] = "Correct!"
        else:
            test.score_sheet[key] = "InCorrect"
        count -= 1
    print()
    print("Your total score is: ", test.score, "/", test.question_amount)
    print(test.score_sheet)


def start_test_show(test) -> None:
    """Test users using questions and answers from test object. Users can choose
    to show correct answer after each question they answer or show all after
    completing test.

    Args:
        test(object): PracticeTest object.
    """
    count = test.question_amount
    print()
    print("We Will Now Begin The Test!\n")
    d = test.questions_and_answers.copy()
    x = input("Enter 1 if you would like to see correct answer after answering" \
              " each question or enter 2 if you would like to see correct" \
              " answers at the end")
    print()
    users_answers = {}
    ques_num = 1

    if x == '1':
        while count > 0:
            key = random.choice(list(d.keys()))
            print(f"Question #{ques_num}: {key}\n")
            answer = input("Enter answer: ")
            users_answers[key] = answer
            print(f"Correct Answer: {d[key]}\n")
            del d[key]
            ques_num += 1
            count -= 1

    elif x == '2':
        while count > 0:
            key = random.choice(list(d.keys()))
            del d[key]
            print(key)
            answer = input("Enter answer: ")
            users_answers[key] = answer
            print()
            count -= 1
        print("--- Results ---\n")
        for i in test.questions_and_answers:
            print(f"Question #{ques_num}: {i}\n")
            print(f"Your Answer: {users_answers[i]}")
            print(f"Correct Answer: {test.questions_and_answers[i]}\n")
            ques_num += 1


def validate_test_type() -> str:
    """Docstring"""

    test_type = input("Enter 1 for ExactAnswer and 2 for ShowAnswer: ")
    test_type.replace(' ', '')
    print()

    while test_type != '1' and test_type != '2':
        print("Invalid entry: Must enter 1 for ExactAnswer or 2 for ShowAnswer.\n")
        test_type = input("Enter 1 for ExactAnswer and 2 for ShowAnswer: ")
        test_type.replace(' ', '')
        print()

    return test_type
    