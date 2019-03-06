from otree.api import Currency as c, currency_range, Submission
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Type)

        decisions = {}
        for p in self.player.get_others_in_group():
            decisions[p.name] = random.choice([False, True])

        yield pages.Formation, decisions

        yield (pages.Action,
               {'action': random.choice([0, 1])})

        yield (pages.Results)


# App Test
# otree test fixed_es --export=test_fixed_es
# Treatment Test
# otree test sticky_es --export=test_sticky_es