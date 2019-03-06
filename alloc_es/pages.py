from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class BeforeAllocationWP(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.assigning_given_types()

class Allocation(Page):
    form_model = 'player'
    form_fields = ['alloc']

    def vars_for_template(self):
        return self.player.vars_for_template()


class AllocationWP(WaitPage):
    # wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.group.chosen_allocation()
        self.group.set_allocations()
        self.group.round_payoffs()
        # self.group.total_payoff()


class ClosingPage(Page):
    def before_next_page(self):
        self.player.var_between_apps()


page_sequence = [
    BeforeAllocationWP,
    Allocation,
    AllocationWP,
    ClosingPage,
]
