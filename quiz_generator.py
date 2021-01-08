from utility import util


class QuizGenerator:

    def __init__(self, name: str) -> None:
        """A quiz generator."""
        self.name = name
        self.questions_and_answers = {}
        self.score_sheet = {}
        self.score = 0
        self.question_amount = 0

    def add_question_and_answer(self, question: str, answer: str) -> None:
        self.questions_and_answers[question] = answer

    def create_quiz(self) -> None:
        """A fire docstring"""

        ques_amount = self.validate_ques_amount()

        while ques_amount > 0:
            question = input("Enter question: ")
            answer = input("Enter Answer: ")
            print()
            self.add_question_and_answer(question, answer)
            ques_amount -= 1

    def run_quiz(self, quiz_type: str) -> None:

        print("We Will Now Begin The Quiz!\n")
        if quiz_type == '1':
            util.start_quiz_exact(self)
        elif quiz_type == '2':
            util.start_quiz_show(self)

    def _validate_ques_amount(self) -> int:
        """Helper Method. Used to ensure user enters a valid number for question
         amount when creating a quiz.

         Returns:
             int: Valid integer for question amount.
         """
        is_int = False
        amount = 0
        while is_int is False:
            try:
                amount = int(
                    input("How many questions would you like to enter? "))
                print()
                is_int = True
            except:
                print('\nError: Must input number greater than 0.\n')
                is_int = False
            if is_int is True:
                if amount < 1:
                    print('\nError: Must input number greater than 0.\n')
                    is_int = False

        self.question_amount = amount
        return amount
