# -*- coding: UTF-8 -*-
# __author__ = 'liuhc'
import random
import time


class Question:
    def __init__(self, ID, description, major, true_answer,
                 level_0_answer=False, level_1_answer=False, level_2_answer=False):
        self.ID = ID
        self.description = description
        self.major = major
        self.true_ans = true_answer
        self.false_ans = {"0": level_0_answer, "1": level_1_answer, "2": level_2_answer}
        self.ans = []


class Quiz:
    def __init__(self, level, questions):
        self.level = level
        if self.level not in [0, 1, 2]:
            raise ValueError("level必须等于0、1、2这三个数其中之一！")
        self.questions_dist = {"0": [40, 5, 5], "1": [5, 40, 5], "2": [5, 5, 40]}
        self.questions = []
        self.score = 0
        self.nta = ["A", "B", "C", "D"]
        self.qs = questions
        self.wrong_ans = []

    def collect_questions(self):
        """先从有简单备选答案的题目中选题，
           然后从未选过且有中等备选答案的题目中选题，
           最后总未选过且有困难备选答案的题目中选题；
           self.level=0（简单）：简单80%，中等10%，困难10%
           self.level=1（中等）：简单10%，中等80%，困难10%
           self.level=2（困难）：简单10%，中等10%，困难80%
        """
        for level in range(3):
            temp_questions_list = []
            for q in self.qs:
                if q.false_ans[str(level)]:
                    temp_questions_list.append(q)
            temp_questions_list = random.sample(temp_questions_list, self.questions_dist[str(self.level)][level])
            for q in temp_questions_list:
                q.ans = list(q.true_ans) + q.false_ans[level]
                random.shuffle(q.ans)
            self.questions.extend(temp_questions_list)
        random.shuffle(self.questions)

    def start_quiz(self):
        for q_i, q in enumerate(self.questions):
            print(q.description)
            for i, ans in enumerate(q.ans):
                print(self.nta[i], ans)
            selection = input("请选择：  ").upper()
            if selection not in self.nta:
                raise ValueError("请输入字母A-D选择答案！")
            selected_ans = self.nta.index(selection)
            if q.ans[selected_ans] == q.true_ans:
                self.score += 2
            else:
                self.wrong_ans.append((q_i, q))
        for i in range(4):
            if i == 0:
                print("正在改卷", end="")
                time.sleep(1)
            elif i != 3:
                print(".", end="")
                time.sleep(1)
            else:
                print(".")
        self.show_result()

    def show_result(self):
        tips = {"0": {"0": [],
                      "30": [],
                      "60": [],
                      "70": [],
                      "80": [],
                      "90": [],
                      "95": [],
                      "100": []},
                "1": {"0": [],
                      "30": [],
                      "60": [],
                      "70": [],
                      "80": [],
                      "90": [],
                      "95": [],
                      "100": []},
                "2": {"0": [],
                      "30": [],
                      "60": [],
                      "70": [],
                      "80": [],
                      "90": [],
                      "95": [],
                      "100": []}}
        if self.score == 100:
            tip = random.choice(tips[str(self.level)]["100"])
        elif self.score >= 95:
            tip = random.choice(tips[str(self.level)]["95"])
        elif self.score >= 90:
            tip = random.choice(tips[str(self.level)]["90"])
        elif self.score >= 80:
            tip = random.choice(tips[str(self.level)]["80"])
        elif self.score >= 70:
            tip = random.choice(tips[str(self.level)]["70"])
        elif self.score >= 60:
            tip = random.choice(tips[str(self.level)]["60"])
        elif self.score >= 30:
            tip = random.choice(tips[str(self.level)]["30"])
        else:
            tip = random.choice(tips[str(self.level)]["0"])
        print(tip)
