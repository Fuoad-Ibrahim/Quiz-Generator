import random

class PracticeTest:
    
    def __init__(self, name: str) -> None:
        "A practice test generator for people studying for a subject"
        self.name = name
        self.questions_and_answers = {}
        self.score_sheet = {}
        self.score = 0
        
    def add_question_and_answer(self, question: str, answer: str) -> None:
        self.questions_and_answers[question] = answer
    
    def create_test(self) -> None:
        is_int = False
        while is_int is False:
            try:
                amount = int(input("How many questions would you like to enter? "))
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


class ExactAnswer(PracticeTest):
    def __init__(self, name) -> None:
        "A fire description"
        PracticeTest.__init__(self, name)
        self.score = 0
        
        is_int = False
        while is_int is False:
            try:
                amount = int(input("How many questions would you like to enter? "))
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
        print()
        print("Lets Create You're Test!")
        print()
        while count > 0:
            question = input("Enter question: ")
            answer = input("Enter Answer: ")
            self.add_question_and_answer(question, answer)
            count -= 1
    
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
        
        #return self.questions_and_answers  
            
            
class ShowAnswer(PracticeTest):
    def __init__(self, name) -> None:
        PracticeTest.__init__(self, name)

def createTest() -> None:
    pass

def startTest_Exact(test) -> None:
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
        startTest_Exact(test)
    elif test_type == '2':
        pass
    