from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

quiz_list = []
for item in question_data:
    question = Question(item["question"], item["correct_answer"])
    quiz_list.append(question)

quiz = QuizBrain(quiz_list)

while quiz.still_has_questions():
    quiz.next_question()