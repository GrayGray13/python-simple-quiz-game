from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(question["text"], question['answer'])
    question_bank.append(new_question)

qb = QuizBrain(question_bank)

while qb.still_has_questions():
    answer = qb.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {qb.score}/{qb.question_number}")
