from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):
        if self.player.given_type == 1:
            yield (pages.NameChoice,
                   {'group_name': random.choice([1,2,3,4,5])})

        if self.player.given_type == 5:
            yield (pages.NameChoice,
                   {'group_name': random.choice([6,7,8,9,10])})

        if self.player.given_type == 1 and self.group.circles_coord == 0:
            yield (pages.NameChoiceC,
                   {'group_name': random.choice([1,2,3,4,5])})

        if self.player.given_type == 5 and self.group.triangles_coord == 0:
            yield (pages.NameChoiceT,
                   {'group_name': random.choice([6,7,8,9,10])})

        if self.player.given_type == 1 and self.group.circles_coord == 0:
            yield (pages.NameChoiceC2,
                   {'group_name': random.choice([1,2,3,4,5])})

        if self.player.given_type == 5 and self.group.triangles_coord == 0:
            yield (pages.NameChoiceT2,
                   {'group_name': random.choice([6,7,8,9,10])})

        yield (pages.NameOutcome)

# App Test
# otree test name_es --export=test_name_es
# Treatment Test
# otree test sticky_es --export=test_sticky_es