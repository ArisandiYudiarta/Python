from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    questions = data["text"]
    answer = data["answer"]
    new_q = Question(questions, answer)
    question_bank.append(new_q)

question = QuizBrain(question_bank)

while question.still_has_question():
    question.next_q()
print("Congratulation! You completed the entire quiz!")
print(f"Your final score is {question.user_score} out of {question.question_number}")
