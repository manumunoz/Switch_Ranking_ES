from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class InitializingWP(WaitPage):
    wait_for_all_groups = True


class ScoreWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.sum_score()
        self.group.ranking_for_groups()
        self.group.given_types()


class Score(Page):
    def before_next_page(self):
        self.player.var_between_apps()


page_sequence = [
    InitializingWP,
    ScoreWP,
    Score,
]
