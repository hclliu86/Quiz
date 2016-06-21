# -*- coding: UTF-8 -*-
# __author__ = 'liuhc'


class Question:
    def __init__(self, ID, description, major, true_answer,
                 level_0_answer=False, level_1_answer=False, level_2_answer=False):
        self.ID = ID
        self.description = description
        self.major = major
        self.true_answer = true_answer
        self.level_0_answer = level_0_answer
        self.level_1_answer = level_1_answer
        self.level_2_answer = level_2_answer

    def display(self):
        pass


class Quiz:
    def __init__(self, level):
        self.level = level
        self.questions = []
        self.score = 0
        self.nta = {"0": "A. ", "1": "B. ", "2": "C. ", "3": "D. "}
        self.qs = []

    def collect_questions(self):
        """先从有简单备选答案的题目中选题，
           然后从未选过且有中等备选答案的题目中选题，
           最后总未选过且有困难备选答案的题目中选题；
           self.level=0（简单）：简单80%，中等10%，困难10%
           self.level=1（中等）：简单10%，中等80%，困难10%
           self.level=2（困难）：简单10%，中等10%，困难80%
        """
        if self.level == 0:
            level_0_questions = []
            level_1_questions = []
            level_2_questions = []
            for q in self.qs:
                if q.level_0_ans:
                    level_0_questions.append(q)
            level_0_questions.random_choose(40)
            for q in level_0_questions:
                q.ans = list(q.true_ans) + q.level_0_questions

            for q in self.qs:
                if q.level_1_ans != False and q not in level_0_questions:
                    level_1_questions.append(q)
            level_1_questions.random_choose(5)
            for q in level_1_questions:
                q.ans = list(q.true_ans) + q.level_1_questions

            for q in self.qs:
                if q.level_2_ans != False and q not in level_0_questions and q not in level_1_questions:
                    level_2_questions.append(q)
            level_2_questions.random_choose(5)
            for q in level_2_questions:
                q.ans = list(q.true_ans) + q.level_2_questions

    def start_quiz(self):
        for q in self.questions:
            print(q.description)
            for i, ans in enumerate(q.ans):
                print(self.nta[str(i)], ans)
            selection = input("请选择：  ")
            selected_ans = [lambda i: self.nta[i] = selection]
            if q.ans[selected_ans] == q.true_ans:
                self.score += 2
