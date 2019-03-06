from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.WelcomeP2)

        if self.player.treat == 1:
            yield (pages.GroupChangeInst,
                   {'given_group': 3, 'appearance': 3, 'label': 2, 'pay_coord': 2, 'pay_coord2': 1, 'information': 1})
        elif self.player.treat == 2:
            yield (pages.GroupChangeInst,
                   {'given_group': 3, 'appearance': 1, 'label': 2, 'pay_coord': 2, 'pay_coord2': 1, 'information': 2})
        elif self.player.treat == 3:
            yield (pages.GroupChangeInst,
                   {'given_group': 3, 'appearance': 1, 'label': 2, 'pay_coord': 2, 'pay_coord2': 1, 'information': 3})
        elif self.player.treat == 4:
            yield (pages.GroupChangeInst,
                   {'given_group': 3, 'appearance': 3, 'label': 2, 'pay_coord': 2, 'pay_coord2': 1, 'information': 1,
                    'cost_change_one': 3,'cost_change_none': 2})
        elif self.player.treat == 5:
            yield (pages.GroupChangeInst,
                   {'given_group': 3, 'appearance': 1, 'label': 2, 'pay_coord': 2, 'pay_coord2': 1, 'information': 2,
                    'cost_change_one': 3,'cost_change_none': 2})
        elif self.player.treat == 6:
            yield (pages.GroupChangeInst,
                   {'given_group': 3, 'appearance': 1, 'label': 2, 'pay_coord': 2, 'pay_coord2': 1, 'information': 3,
                    'cost_change_one': 3,'cost_change_none': 2})
        yield (pages.SummaryInst)


# otree test sticky_es --export=test_sticky_es

# App Test
# otree test inst_fluid_es --export=test_inst_fluid_es
# Treatment Test
# otree test sticky_es --export=test_sticky_es
# otree test blurry_es --export=test_blurry_es
# otree test sticky_cost_es --export=test_sticky_cost_es
# otree test blurry_cost_es --export=test_blurry_cost_es

