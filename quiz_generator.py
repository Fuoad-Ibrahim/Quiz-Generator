from utility import util


class QuizGenerator:

    def __init__(self, name: str) -> None:
        """A quiz generator."""
        self.name = name
        self.score = 0
        self.score_sheet = {}
        self.questions_and_answers = {}
        self.question_amount = 0

    def get_questions_and_answers(self) -> dict:
        return self.questions_and_answers
    
    def increment_score(self) -> None:
        self.score += 1
    
    def add_to_score_sheet(self, key, value) -> None:
        self.score_sheet[key] = value

    def add_question_and_answer(self, question: str, answer: str) -> None:
        self.questions_and_answers[question] = answer

    def create_quiz(self) -> None:
        """A fire docstring"""

        ques_amount = self._validate_ques_amount()

        while ques_amount > 0:
            question = input("Enter question: ")
            answer = input("Enter Answer: ")
            print()
            self.add_question_and_answer(question, answer)
            ques_amount -= 1

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
