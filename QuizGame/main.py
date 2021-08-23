from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_list = []

for each in question_data:
    question_text = each["text"]
    question_answer = each["answer"]
    new_question = Question(question_text, question_answer)
    question_list.append(new_question)

Quiz_Brain = QuizBrain(question_list)

Quiz_Brain.next_question()