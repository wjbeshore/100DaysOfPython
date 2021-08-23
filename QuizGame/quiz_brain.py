class QuizBrain:
    def __init__(self, q_list):
        self.questions = q_list
        self.q_right = 0
        self.q_wrong = 0
        self.q_number = 0

    def next_question(self):
        current_question = self.questions[self.q_number]
        print("Q" + str(self.q_number+1) + ": " + current_question.text)
        answer = input("True or false?")
        if answer == current_question.answer:
            print("Correct!")
            self.q_right += 1
        else:
            print("I'm sorry, that's incorrect.")
            self.q_wrong += 1
        self.q_number += 1
        print("You've answered " + str(self.q_right) + " questions correct out of " + str(self.q_number))
        self.next_question()