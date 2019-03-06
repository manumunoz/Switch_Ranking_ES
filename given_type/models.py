from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Manu Munoz'

doc = """
Identity Switch - Networks: Score
"""


class Constants(BaseConstants):
    #------------------------------------------
    name_in_url = 'score_test'
    names = ['1','2','3','4','5','6','7']
    players_per_group = len(names)
    periods = 1
    num_rounds = periods
    #------------------------------------------
    # Treatment & Group parameters
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
    #------------------------------------------
    # Payoffs
    exp_currency = "points"
    currency = "pesos"
    currency_exchange = 1000
    points_exchange = 1
    min_pay = 10000
    min_points = 10
    link_cost = 2
    liked_gain = 6
    disliked_gain = 4
    #------------------------------------------


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def sum_score(self):
        for player in self.get_players():
            player.score = player.participant.vars['num_correct']

    def ranking_for_groups(self):
        scores = [p.score for p in self.get_players()]
        scores.sort(reverse=True)

        for b in set(scores):
            rank_set = [i for i, x in enumerate(scores, 1) if x == b]
            for p in self.get_players():
                if p.score == b:
                    p.rank = rank_set.pop(random.randrange(0, len(rank_set)))

    def given_types(self):
        for player in self.get_players():
            if player.rank <= 3:
                player.given_type = 5
            else:
                player.given_type = 1


class Player(BasePlayer):
    score = models.IntegerField()
    rank = models.IntegerField()
    given_type = models.IntegerField()

    def var_between_apps(self):
        self.participant.vars['given_type'] = self.given_type
