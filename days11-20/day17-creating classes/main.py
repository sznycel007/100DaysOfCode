from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for entry in question_data:
    # q_text = entry["text"]
    q_text = entry["question"]
    q_answer = entry["correct_answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

# print(question_bank)
# print(question_bank[0].text, question_bank[0].answer)

quiz = QuizBrain(question_bank)


# while still_has_questions:
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number} ")




