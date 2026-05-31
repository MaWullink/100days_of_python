from data import data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in data["results"]:
    question = item["question"]
    answer = item["correct_answer"]
    quiz_item = Question(question, answer)
    question_bank.append(quiz_item)

quiz = QuizBrain(question_bank)

while quiz.questions_remaining():
  quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")