from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


# class WelcomeInst(Page):
#     pass
#     # def is_displayed(self):
#     #     return self.round_number == 1


class NameChoiceWP(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.assigning_given_types()
        self.subsession.choosing_names()


class NameChoice(Page):
    form_model = 'player'
    form_fields = ['group_name']

    # def is_displayed(self):
    #     return self.round_number == 1

    def before_next_page(self):
        self.player.choice_value()

        group = self.group
        players = group.get_players()
        g_a = [p.group_a for p in players]
        group.total_group_a = sum(g_a)
        g_b = [p.group_b for p in players]
        group.total_group_b = sum(g_b)
        g_c = [p.group_c for p in players]
        group.total_group_c = sum(g_c)
        g_d = [p.group_d for p in players]
        group.total_group_d = sum(g_d)
        g_e = [p.group_e for p in players]
        group.total_group_e = sum(g_e)
        g_f = [p.group_f for p in players]
        group.total_group_f = sum(g_f)
        g_g = [p.group_g for p in players]
        group.total_group_g = sum(g_g)
        g_h = [p.group_h for p in players]
        group.total_group_h = sum(g_h)
        g_i = [p.group_i for p in players]
        group.total_group_i = sum(g_i)
        g_j = [p.group_j for p in players]
        group.total_group_j = sum(g_j)


class NameOutcomeWP1(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.choosing_names()
        self.subsession.try_one()


class NameChoiceC(Page):
    form_model = 'player'
    form_fields = ['group_name']

    def is_displayed(self):
        return self.player.given_type == 1 and self.group.circles_coord == 0

    def before_next_page(self):
        self.player.choice_value()

        group = self.group
        players = group.get_players()
        g_a = [p.group_a for p in players]
        group.total_group_a = sum(g_a)
        g_b = [p.group_b for p in players]
        group.total_group_b = sum(g_b)
        g_c = [p.group_c for p in players]
        group.total_group_c = sum(g_c)
        g_d = [p.group_d for p in players]
        group.total_group_d = sum(g_d)
        g_e = [p.group_e for p in players]
        group.total_group_e = sum(g_e)
        g_f = [p.group_f for p in players]
        group.total_group_f = sum(g_f)
        g_g = [p.group_g for p in players]
        group.total_group_g = sum(g_g)
        g_h = [p.group_h for p in players]
        group.total_group_h = sum(g_h)
        g_i = [p.group_i for p in players]
        group.total_group_i = sum(g_i)
        g_j = [p.group_j for p in players]
        group.total_group_j = sum(g_j)


class NameChoiceT(Page):
    form_model = 'player'
    form_fields = ['group_name']

    def is_displayed(self):
        return self.player.given_type == 5 and self.group.triangles_coord == 0

    def before_next_page(self):
        self.player.choice_value()

        group = self.group
        players = group.get_players()
        g_a = [p.group_a for p in players]
        group.total_group_a = sum(g_a)
        g_b = [p.group_b for p in players]
        group.total_group_b = sum(g_b)
        g_c = [p.group_c for p in players]
        group.total_group_c = sum(g_c)
        g_d = [p.group_d for p in players]
        group.total_group_d = sum(g_d)
        g_e = [p.group_e for p in players]
        group.total_group_e = sum(g_e)
        g_f = [p.group_f for p in players]
        group.total_group_f = sum(g_f)
        g_g = [p.group_g for p in players]
        group.total_group_g = sum(g_g)
        g_h = [p.group_h for p in players]
        group.total_group_h = sum(g_h)
        g_i = [p.group_i for p in players]
        group.total_group_i = sum(g_i)
        g_j = [p.group_j for p in players]
        group.total_group_j = sum(g_j)

        self.player.var_between_apps()


class NameOutcomeWP2(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.choosing_names()
        self.subsession.try_two()


class NameChoiceC2(Page):
    form_model = 'player'
    form_fields = ['group_name']

    def is_displayed(self):
        return self.player.given_type == 1 and self.group.circles_coord == 0

    def before_next_page(self):
        self.player.choice_value()

        group = self.group
        players = group.get_players()
        g_a = [p.group_a for p in players]
        group.total_group_a = sum(g_a)
        g_b = [p.group_b for p in players]
        group.total_group_b = sum(g_b)
        g_c = [p.group_c for p in players]
        group.total_group_c = sum(g_c)
        g_d = [p.group_d for p in players]
        group.total_group_d = sum(g_d)
        g_e = [p.group_e for p in players]
        group.total_group_e = sum(g_e)
        g_f = [p.group_f for p in players]
        group.total_group_f = sum(g_f)
        g_g = [p.group_g for p in players]
        group.total_group_g = sum(g_g)
        g_h = [p.group_h for p in players]
        group.total_group_h = sum(g_h)
        g_i = [p.group_i for p in players]
        group.total_group_i = sum(g_i)
        g_j = [p.group_j for p in players]
        group.total_group_j = sum(g_j)


class NameChoiceT2(Page):
    form_model = 'player'
    form_fields = ['group_name']

    def is_displayed(self):
        return self.player.given_type == 5 and self.group.triangles_coord == 0

    def before_next_page(self):
        self.player.choice_value()

        group = self.group
        players = group.get_players()
        g_a = [p.group_a for p in players]
        group.total_group_a = sum(g_a)
        g_b = [p.group_b for p in players]
        group.total_group_b = sum(g_b)
        g_c = [p.group_c for p in players]
        group.total_group_c = sum(g_c)
        g_d = [p.group_d for p in players]
        group.total_group_d = sum(g_d)
        g_e = [p.group_e for p in players]
        group.total_group_e = sum(g_e)
        g_f = [p.group_f for p in players]
        group.total_group_f = sum(g_f)
        g_g = [p.group_g for p in players]
        group.total_group_g = sum(g_g)
        g_h = [p.group_h for p in players]
        group.total_group_h = sum(g_h)
        g_i = [p.group_i for p in players]
        group.total_group_i = sum(g_i)
        g_j = [p.group_j for p in players]
        group.total_group_j = sum(g_j)

        self.player.var_between_apps()


class NameOutcomeWP3(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.choosing_names()
        self.subsession.failed_name_choice()
        self.subsession.try_three()


class NameOutcome(Page):

    def before_next_page(self):
        self.player.var_between_apps()


page_sequence = [
    # WelcomeInst,
    NameChoiceWP,
    NameChoice,
    NameOutcomeWP1,
    NameChoiceC,
    NameChoiceT,
    NameOutcomeWP2,
    NameChoiceC2,
    NameChoiceT2,
    NameOutcomeWP3,
    NameOutcome
]
