from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
import numpy
import math

author = 'Manu Munoz'

doc = """
Real effort task. A player is shown two matrices. He has to find the highest number each matrix and report the sum
"""


class Constants(BaseConstants):
    #------------------------------------------
    name_in_url = 'task_sums'
    names = ['1','2','3','4','5','6','7']
    players_per_group = len(names)
    num_rounds = 40
    #------------------------------------------
    # Matrices
    max_rand = 99
    min_rand = 0
    num_rows = 6
    num_cols = 6
    code_length = 10
    time_length = 1 #3
    #------------------------------------------
    players = len(names)
    others = len(names) - 1
    total_circles = 4
    total_triangles = 3
    circle = 1 # Majority
    triangle = 0 # Minority
    part_task = 1
    part_name = 2
    part_fixed = 3
    part_fluid = 4
    part_alloc = 5
    rounds_fixed = 10
    # ------------------------------------------
    exp_currency = "puntos"
    currency = "pesos"
    currency_exchange = 800
    points_exchange = 1
    min_pay = 10000
    link_cost = 2
    liked_gain = 6
    disliked_gain = 4
    # ------------------------------------------

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    code = models.StringField()

    # def validate_answer(self, code):
    #     if len(code) < Constants.code_length or code == 'None':
    #         return False
    #     return True

    rand_left = models.PositiveIntegerField()
    rand_right = models.PositiveIntegerField()
    solution = models.PositiveIntegerField()
    answer = models.PositiveIntegerField()
    answer_correct = models.PositiveIntegerField(initial=0)
    num_correct = models.PositiveIntegerField(initial=0)
    m_left = numpy.zeros((Constants.num_rows, Constants.num_cols))
    m_right = numpy.zeros((Constants.num_rows, Constants.num_cols))

    def initialize(self):
        self.num_correct = sum([p.answer_correct for p in self.in_all_rounds()])
        self.rand_left = (math.floor((random.random() * 33)) + math.floor((random.random() * 33)) + math.floor((random.random() * 33)))
        self.rand_right = (math.floor((random.random() * 33)) + math.floor((random.random() * 33)) + math.floor((random.random() * 33)))
        self.solution = self.rand_left + self.rand_right

        for i in range(Constants.num_rows):
            for j in range(Constants.num_cols):
                self.m_left[i][j] = random.randint(0, self.rand_left - 1)
                self.m_right[i][j] = random.randint(0, self.rand_right - 1)

        self.m_left[random.randint(0, Constants.num_rows - 1)][random.randint(0, Constants.num_cols - 1)] = self.rand_left
        self.m_right[random.randint(0, Constants.num_rows - 1)][random.randint(0, Constants.num_cols - 1)] = self.rand_right

    def set_payoff(self):
        # self.payoff = self.answer_correct
        self.participant.vars['num_correct'] = self.num_correct
