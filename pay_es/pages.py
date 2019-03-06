from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class RandomPayWP(WaitPage):
    # wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.group.round_payoffs()


class RandomPay(Page):
    def vars_for_template(self):
        return self.player.vars_for_template()


page_sequence = [
    RandomPayWP,
    RandomPay,
]
