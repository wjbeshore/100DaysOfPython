class QuizBrain:
    def __init__(self, q_list,):
        questions = q_list

        q_right = 0

        q_wrong = 0

        q_number = 0

    def next_question(self):
        print("Q" + str(self.q_number+1) + ": " + self.questions[self.q_number]["text"])