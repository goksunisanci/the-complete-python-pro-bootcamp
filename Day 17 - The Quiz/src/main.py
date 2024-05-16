from src.data.question_data import question_data
from src.models.question import Question
from src.models.quiz_brain import QuizBrain

from typing import List


def create_question_bank(questions: List) -> List[Question]:
    bank = []
    for question in questions:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        bank.append(new_question)
    return bank


question_bank = create_question_bank(question_data)
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f'Your final score was: {quiz.score}/{len(question_bank)}')
