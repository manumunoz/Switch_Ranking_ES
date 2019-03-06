from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
from collections import OrderedDict
import json


class BeforeTypeWP(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.assigning_given_types()


class Type(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return self.player.vars_for_template()


class BeforeFormationWP(WaitPage):
    # wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.group.assign_random_names_and_positions()
        self.group.choosing_types()
        self.group.displaying_network()


class Formation(Page):
    form_model = 'player'

    def vars_for_template(self):
        return self.player.vars_for_template()

    def get_form_fields(self):
        other_player_names = list(map(lambda x: x.name, self.player.get_others_in_group()))
        other_player_names.sort()
        return other_player_names

    def before_next_page(self):
        self.player.friends = json.dumps([i.name for i in self.player.get_others_in_group() if getattr(self.player, i.name)])


class BeforeActionWP(WaitPage):
    # wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.group.forming_network()
        self.group.calculate_props_from_and_links() # una vez generada la red, calculo las props from
        self.group.calculate_degree()
        self.group.linking_costs()


class Action(Page):
    form_model = 'player'
    form_fields = ['action']

    def vars_for_template(self):
        self.group.forming_network()
        return self.player.vars_for_template()


class BeforeResultsWP(WaitPage):
    # wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.group.calculate_actions()
        self.group.sum_coordinations()
        self.group.coordination_score()
        self.group.values_coordination()
        self.group.round_gains()
        self.group.round_payoffs()
        self.group.forming_network()


class Results(Page):
    def vars_for_template(self):
        self.group.forming_network()
        return self.player.vars_for_template()

    def before_next_page(self):
        self.player.var_between_apps()


page_sequence = [
    BeforeTypeWP,
    Type,
    BeforeFormationWP,
    Formation,
    BeforeActionWP,
    Action,
    BeforeResultsWP,
    Results
]
