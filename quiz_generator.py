class QuizGenerator:
    """
    This is a class to create quizzes.

    Attributes:
        name (str): Name of quiz.
        score (int): User's score on quiz.
        score_sheet (dict): Scoresheet from quiz.
        questions_and_answers (dict): The questions and answers for quiz.
        question_amount (int): The amount of questions the quiz contains.
    """

    def __init__(self, name: str) -> None:
        """
        The constructor for QuizGenerator class.

        Parameters:
            name (str): Name of quiz.
        """
        self.name = name
        self.score = 0
        self.score_sheet = {}
        self.questions_and_answers = {}
        self.question_amount = 0

    def get_questions_and_answers(self) -> dict:
        """
        Provides questions and answers from quiz.

        Returns:
            dict: Questions and answers from quiz.
        """
        return self.questions_and_answers

    def increment_score(self) -> None:
        """
        Provides user's score on quiz.
        """
        self.score += 1

    def add_to_score_sheet(self, key: str, value: str) -> None:
        """
        Adds question and result from answering question.

        Parameters:
            key (str): Random question from quiz.
            value (str): Result from answer.
        """
        self.score_sheet[key] = value

    def add_question_and_answer(self, question: str, answer: str) -> None:
        """
        Add question it's correct answer to quiz.

        Parameters:
            question (str): Question to be added.
            answer (str): Answer to be added.
        """
        self.questions_and_answers[question] = answer

    def create_quiz(self) -> None:
        """
        Creates quiz by adding all questions and their correct answers.
        """

        ques_amount = self._validate_ques_amount()

        while ques_amount > 0:
            question = input("Enter question: ")
            answer = input("Enter Answer: ")
            print()
            self.add_question_and_answer(question, answer)
            ques_amount -= 1

    def _validate_ques_amount(self) -> int:
        """Helper method used to ensure user enters a valid number for question
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
            except ValueError:
                print('\nError: Must input number greater than 0.\n')
                is_int = False
            if is_int is True:
                if amount < 1:
                    print('\nError: Must input number greater than 0.\n')
                    is_int = False

        self.question_amount = amount
        return amount
