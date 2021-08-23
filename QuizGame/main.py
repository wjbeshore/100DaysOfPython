from data import question_data
from question_model import Question

question_list = []

for each in question_data:
    question_text = each["text"]
    question_answer = each["answer"]
    new_question = Question(question_text, question_answer)
    question_list.append(new_question)

print(question_list)