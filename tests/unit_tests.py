import unittest

import sys
sys.path.append("..")
import quiz_generator


class TestQuizGenerator(unittest.TestCase):

    def test_adding_questions_and_answers(self):
        
        #Assume
        test = quiz_generator.QuizGenerator("Tim")
        question1 = "What is 2+2"
        answer1 = "4"
        question2 = "What is 3*3"
        answer2 = "9"
        correct_dict = {question1: answer1, question2: answer2}

        # Action

        test.add_question_and_answer(question1, answer1)
        test.add_question_and_answer(question2, answer2)

        # Assert
        self.assertTrue(correct_dict == test.questions_and_answers)
