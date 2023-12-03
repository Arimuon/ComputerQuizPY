import pandas as pd

class question:
    def __init__(self, question_number: str, type: str, topic: str, question: str, answer: str, distractor1: str, distractor2: str, distractor3: str, is_category: bool):
        self.type = "category" if is_category else type
        self.topic = topic
        self.question = question
        self.answer = answer
        self.question_number = question_number
        if type == type == "True or False":
            if distractor1:
                self.options = [answer, distractor1]
            else:
                self.options = [answer.title(), "True" if answer == "FALSE" else "False"]
        else:
            self.options = [answer, distractor1, distractor2, distractor3]


