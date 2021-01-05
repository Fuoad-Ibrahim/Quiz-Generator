import random
from practice_test import PracticeTest


def start_test(self) -> dict:
    "Starts test"
    count = self.question_amount
    print()
    print("We Will Now Begin The Test!")
    print()
    while count > 0:
        d = self.questions_and_answers
        key = random.choice(list(d.keys()))
        val = self.questions_and_answers[key]
        del self.questions_and_answers[key]
        print(key)
        a = input("Enter answer: ")

        if int(a) == int(val):
            self.score += 1
            self.score_sheet[key] = "Correct!"
        else:
            self.score_sheet[key] = "InCorrect"
        count -= 1
    print()
    print("Your total score is: ", self.score, "/", self.question_amount)
    return self.score_sheet


def start_test_exact(test) -> None:
    "Starts test"
    count = test.question_amount
    print()
    print("We Will Now Begin The Test!\n")
    d = test.questions_and_answers

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


if __name__ == "__main__":
    print('Welcome message')
    test_type = input('Enter 1 for ExactAnswer and 2 for ShowAnswer: ')
    print()
    print("Let's create your test!\n")
    name = input('What would you like to name your test?\n')
    test = PracticeTest(name)
    test.create_test()

    if test_type == '1':
        start_test_exact(test)
    elif test_type == '2':
        pass
