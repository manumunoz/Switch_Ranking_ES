from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class WelcomeInstWP(WaitPage):
    wait_for_all_groups = True


class WelcomeInst(Page):

    def vars_for_template(self):
        return self.player.vars_for_template()


class DecisionsInstWP(WaitPage):
    wait_for_all_groups = True


class DecisionsInst(Page):
    form_model = 'player'
    form_fields = ['given_group','appearance','label','active','count']

    def vars_for_template(self):
        return self.player.vars_for_template()

    def given_group_error_message(self, value):
        if value != 1:
            return 'En esta Parte su grupo está fijo por todas las 10 rondas'

    def appearance_error_message(self, value):
        if value != 1:
            return 'En esta Parte su apariencia está fija por todas las 10 rondas'

    def label_error_message(self, value):
        if value != 2:
            return 'En esta Parte su etiqueta se asigna aleatoriamente en cada ronda'

    def active_error_message(self, value):
        if value != 3:
            return 'Para que una conexión esté activa se requiere que los dos jugadores la propongan'

    def count_error_message(self, value):
        if value != 3:
            return 'Para que una conexión esté activa se requiere que los dos jugadores la propongan'


class PointsInstWP(WaitPage):
    wait_for_all_groups = True


class PointsInst(Page):
    form_model = 'player'
    form_fields = ['pay_coord','pay_nocoord']

    def vars_for_template(self):
        return self.player.vars_for_template()

    def pay_coord_error_message(self, value):
        if value != 1:
            return 'Un jugador en este grupo recibe 6 puntos por cada coordinación con una conexión activa y paga 2 ' \
                   'puntos por haber propuesto esa conexión'

    def pay_nocoord_error_message(self, value):
        if value != 3:
            return 'Un jugador no recibe puntos si no se coordina con una conexión activa pero aún así paga 2 puntos por ' \
                   'haber propuesto esa conexión'


class SummaryInstWP(WaitPage):
    wait_for_all_groups = True


class SummaryInst(Page):

    def vars_for_template(self):
        return self.player.vars_for_template()


page_sequence = [
    WelcomeInstWP,
    WelcomeInst,
    DecisionsInstWP,
    DecisionsInst,
    PointsInstWP,
    PointsInst,
    SummaryInstWP,
    SummaryInst,
]
