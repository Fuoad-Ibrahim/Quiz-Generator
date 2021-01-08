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
        is_int = False
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
        
        count = amount
        while count > 0:
            question = input("Enter question: ")
            answer = input("Enter Answer: ")
            print()
            self.add_question_and_answer(question, answer)
            count -= 1
    
    def run_quiz(self, quiz_type: str) -> None:

        print("We Will Now Begin The Quiz!\n")
        if quiz_type == '1':
            util.start_quiz_exact(self)
        elif quiz_type == '2':
            util.start_quiz_show(self)
