from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import time


class WelcomeInst(Page):
    def is_displayed(self):
        return self.round_number == 1


class Start(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        # user has X minutes to complete as many pages as possible
        self.participant.vars['expiry_timestamp'] = time.time() + Constants.time_length * 60


class Sum(Page):
    form_model = 'player'
    form_fields = ['answer']

    def vars_for_template(self):
        self.player.initialize()

        return {
        }

        participant.vars['num_correct'] = self.player.num_correct

    def before_next_page(self):
        if self.player.answer == self.player.solution:
            self.player.answer_correct = 1
        self.player.set_payoff()

    timer_text = 'Tiempo restante:'

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


page_sequence = [
    WelcomeInst,
    Start,
    Sum,
]
