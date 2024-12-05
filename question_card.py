class QuestionCard:
    correct = 0
    attempts = 0
    def __init__(self, question, right_ans, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.right_ans = right_ans
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3

    def got_right(self):
        QuestionCard.correct += 1
        QuestionCard.attempts += 1

    def got_wrong(self):
        QuestionCard.attempts += 1