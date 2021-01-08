from utility import util
import quiz_generator

if __name__ == "__main__":
    print("Welcome message\n")
    quiz_type = util.validate_quiz_type()
    
    print("Let's create your quiz!\n")
    name = input('What would you like to name your quiz?\n')
    quiz = quiz_generator.QuizGenerator(name)
    quiz.create_quiz()
    quiz.run_quiz(quiz_type)
