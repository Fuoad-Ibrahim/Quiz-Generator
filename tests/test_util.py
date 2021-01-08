import unittest

import sys
sys.path.append("..")
from quiz_generator import QuizGenerator
from utility.util import start_quiz_exact, start_quiz_exact


class TestUtil(unittest.TestCase):

    def test_start_quiz_exact_gives_correct_score_and_scoresheet(self):
        
        # Arrange
        quiz = QuizGenerator("Name")
        question1 = "What is 2+2"
        answer1 = "4"
        question2 = "What is 3*3"
        answer2 = "9"

        users_answers = {question1: "4", question2: "7"}
        expected_score = 1
        expected_score_sheet = {question1: "Correct!", question2: "InCorrect"}
        
        # Action
        quiz.add_question_and_answer(question1, answer1)
        quiz.add_question_and_answer(question2, answer2)

        start_quiz_exact(quiz, users_answers)

        # Assert
        self.assertEqual(quiz.score, expected_score)
        self.assertEqual(quiz.score_sheet, expected_score_sheet)
