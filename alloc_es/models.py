from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import json

author = 'Manu Munoz'

doc = """
Identity Switch - ALLOCATION
"""


class Constants(BaseConstants):
    #------------------------------------------
    name_in_url = 'alloc_es'
    names = ['1','2','3','4','5','6','7']
    players_per_group = len(names)
    periods = 1
    num_rounds = periods
    #------------------------------------------
    # Treatment & Group parameters
    players = len(names)
    others = len(names) - 1
    attribute = [1,5,1,5,1,1,5]
    attributes = {'1': 1, '2': 5, '3': 1, '4': 5, '5': 1, '6': 1, '7': 5}
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
    exp_currency = "puntos"
    currency = "pesos"
    currency_exchange = 800
    points_exchange = 1
    min_pay = 10000
    min_pay_pesos = c(10000)
    link_cost = 2
    liked_gain = 6
    disliked_gain = 4
    #------------------------------------------
    # Group Names
    group_a = 'Leones' #Leones
    group_b = 'Tigres' #Tigres
    group_c = 'Leopardos' #Leopardos
    group_d = 'Jaguares' #Jaguares
    group_e = 'Gatos' #Gatos
    group_f = 'Coyotes' #Coyotes
    group_g = 'Chacales' #Chacales
    group_h = 'Lobos' #Lobos
    group_i = 'Zorros' #Zorros
    group_j = 'Perros' #Perros
    #------------------------------------------
    # Dictator
    pie = 10
    #------------------------------------------


class Subsession(BaseSubsession):
    def creating_session(self):
        # for p in self.get_players():
        #     p.given_type = int(Constants.attribute[p.id_in_group - 1])

        if self.round_number == 1:
            chosen_player = random.randint(1, Constants.players)
            self.session.vars['chosen_player'] = chosen_player

    def assigning_given_types(self):
        for g in self.get_groups():
            for p in g.get_players():
                p.given_type = p.participant.vars['given_type']


class Group(BaseGroup):
    chosen_player = models.IntegerField()

    def chosen_allocation(self):
        self.chosen_player = self.session.vars['chosen_player']

    def set_allocations(self):
        if self.session.vars['chosen_player'] == 1:
            self.get_player_by_id(3).alloc_received = self.get_player_by_id(1).alloc
            self.get_player_by_id(2).alloc_received = Constants.pie - self.get_player_by_id(1).alloc
        elif self.session.vars['chosen_player'] == 2:
            self.get_player_by_id(3).alloc_received = self.get_player_by_id(2).alloc
            self.get_player_by_id(4).alloc_received = Constants.pie - self.get_player_by_id(2).alloc
        elif self.session.vars['chosen_player'] == 3:
            self.get_player_by_id(5).alloc_received = self.get_player_by_id(3).alloc
            self.get_player_by_id(4).alloc_received = Constants.pie - self.get_player_by_id(3).alloc
        elif self.session.vars['chosen_player'] == 4:
            self.get_player_by_id(5).alloc_received = self.get_player_by_id(4).alloc
            self.get_player_by_id(7).alloc_received = Constants.pie - self.get_player_by_id(4).alloc
        elif self.session.vars['chosen_player'] == 5:
            self.get_player_by_id(6).alloc_received = self.get_player_by_id(5).alloc
            self.get_player_by_id(7).alloc_received = Constants.pie - self.get_player_by_id(5).alloc
        elif self.session.vars['chosen_player'] == 6:
            self.get_player_by_id(1).alloc_received = self.get_player_by_id(6).alloc
            self.get_player_by_id(2).alloc_received = Constants.pie - self.get_player_by_id(6).alloc
        else:
            self.get_player_by_id(6).alloc_received = self.get_player_by_id(7).alloc
            self.get_player_by_id(2).alloc_received = Constants.pie - self.get_player_by_id(7).alloc

    def round_payoffs(self):
        for player in self.get_players():
            player.points_alloc = player.alloc_received
            player.payoff = player.points_alloc
            # player.total_points = {{ Constants.currency_exchange}} * (player.participant.vars['part_fixed_payoff'] + player.participant.vars['part_fluid_payoff'] + player.participant.vars['part_alloc_payoff'])

    # def total_payoff(self):
    #     for player in self.get_players():
    #         if player.participant.payoff >= Constants.min_pay_pesos:
    #             player.participant.payoff = player.participant.payoff
    #         else:
    #             player.participant.payoff = Constants.min_pay_pesos


class Player(BasePlayer):
    given_type = models.IntegerField() # combination of symbol and preference
    alloc_received = models.IntegerField(initial=0)
    points_alloc = models.IntegerField()

    alloc = models.PositiveIntegerField(
        choices=[0,1,2,3,4,5,6,7,8,9,10]
    )

    def vars_for_template(self):
        return {
            'circles_name': self.participant.vars['circles_name'],
            'triangles_name': self.participant.vars['triangles_name'],
            'circles_label': self.participant.vars['circles_label'],
            'triangles_label': self.participant.vars['triangles_label'],
        }

    def var_between_apps(self):
        self.participant.vars['part_alloc_payoff'] = self.points_alloc
