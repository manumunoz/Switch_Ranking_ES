from otree.api import Currency as c, currency_range, Submission
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Type)

        if self.player.treat == 1 or self.player.treat == 4:
            yield (pages.ChosenType,
                   {'chosen_type': random.choice([1, 5])})
        elif self.player.treat == 2 and self.player.given_type == 1:
            yield (pages.ChosenType,
                   {'chosen_type': random.choice([1, 2])})
        elif self.player.treat == 5 and self.player.given_type == 1:
            yield (pages.ChosenType,
                   {'chosen_type': random.choice([1, 2])})
        elif self.player.treat == 2 and self.player.given_type == 5:
            yield (pages.ChosenType,
                   {'chosen_type': random.choice([5, 6])})
        elif self.player.treat == 5 and self.player.given_type == 5:
            yield (pages.ChosenType,
                   {'chosen_type': random.choice([5, 6])})
        elif self.player.treat == 3 and self.player.given_type == 1:
            yield (pages.ChosenType,
                   {'chosen_type': random.choice([3, 4])})
        elif self.player.treat == 6 and self.player.given_type == 1:
            yield (pages.ChosenType,
                   {'chosen_type': random.choice([3, 4])})
        elif self.player.treat == 3 and self.player.given_type == 5:
            yield (pages.ChosenType,
                   {'chosen_type': random.choice([7, 8])})
        elif self.player.treat == 6 and self.player.given_type == 5:
            yield (pages.ChosenType,
                   {'chosen_type': random.choice([7, 8])})

        decisions = {}
        for p in self.player.get_others_in_group():
            decisions[p.name] = random.choice([False, True])

        yield pages.Formation, decisions

        yield (pages.Action,
               {'action': random.choice([0, 1])})

        yield (pages.Results)

        # if self.round_number == 10:
        #     yield (pages.RandomPay)


# App Test
# otree test fluid_es --export=test_fluid_es
# Treatment Test
# otree test sticky_es --export=test_sticky_es
# otree test blurry_es --export=test_blurry_es
# otree test sticky_cost_es --export=test_sticky_cost_es
# otree test blurry_cost_es --export=test_blurry_cost_es