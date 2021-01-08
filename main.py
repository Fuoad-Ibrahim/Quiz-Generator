import utility
import quiz_generator

if __name__ == "__main__":
    print("Welcome message\n")
    test_type = utility.util.validate_test_type()
    test_type.replace(' ', '')
    print()
    print("Let's create your test!\n")
    
    name = input('What would you like to name your test?\n')
    test = quiz_generator.QuizGenerator(name)
    test.create_test()

    if test_type == '1':
        utility.util.start_test_exact(test)
    elif test_type == '2':
        utility.util.start_test_show(test)
