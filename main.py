from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range(0, len(question_data)):
    question_bank.append(Question(question_data[i]['question'], question_data[i]['correct_answer']))

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
else:
    print("You have completed the quiz!")
    print(f"Your final score: {quiz.score}/{quiz.question_number}")
