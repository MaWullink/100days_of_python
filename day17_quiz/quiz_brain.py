class QuizBrain:
    question_list: object

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def questions_remaining(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        answer = input(f"Q{self.question_number +1}: {self.question_list[self.question_number].question} ")
        self.check_answer(answer, self.question_list[self.question_number].answer)
        self.question_number +=1
    def check_answer(self, answer, correct):
        if answer.lower() == correct.lower():
            print("You got it right!")
            self.score+=1
        else:
            print("You got it wrong.")
            print(correct)
        print(f"Score: {self.score}")



