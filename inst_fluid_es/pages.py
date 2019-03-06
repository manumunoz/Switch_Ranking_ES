from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class WelcomeP2WP(WaitPage):
    wait_for_all_groups = True


class WelcomeP2(Page):

    def vars_for_template(self):
        return self.player.vars_for_template()


class GroupChangeInstWP(WaitPage):
    wait_for_all_groups = True


class GroupChangeInst(Page):
    form_model = 'player'

    def get_form_fields(self):
        if self.player.treat <= 3:
            return ['given_group','appearance','label','pay_coord','pay_coord2','information']
        else:
            return ['given_group','appearance','label','pay_coord','pay_coord2','information','cost_change_one', 'cost_change_none']

    def vars_for_template(self):
        return self.player.vars_for_template()

    def given_group_error_message(self, value):
        if value != 3:
            return 'En esta Parte usted puede cambiarse de grupo en cada ronda'

    def appearance_error_message(self, value):
        if self.player.treat == 1 or self.player.treat == 4:
            if value != 3:
                return 'En esta Parte usted puede cambiar su apariencia cuando usted cambia su grupo'
        elif self.player.treat != 1 and self.player.treat != 4:
            if value != 1:
                return 'En esta Parte usted no puede cambiar su apariencia aunque cambie de grupo'

    def label_error_message(self, value):
        if value != 2:
            return 'En esta Parte su etiqueta se asigna aleatoriamente en cada ronda'

    def pay_coord_error_message(self, value):
        if value != 2:
            return 'Un jugador en este grupo recibe 4 puntos por cada coordinación en la acción violeta con una ' \
                   'conexión activa y paga 2 puntos por proponer esa conexión'

    def pay_coord2_error_message(self, value):
        if value != 1:
            return 'Un jugador en este grupo recibe 6 puntos por cada coordinación en la acción violeta con una ' \
                   'conexión activa y paga 2 puntos por proponer esa conexión'

    def information_error_message(self, value):
        if self.player.treat == 1 or self.player.treat == 4:
            if value != 1:
                return 'Los demás jugadores verán el grupo que usted haya elegido. También verán su nueva apariencia'
        elif self.player.treat == 2 or self.player.treat == 5:
            if value != 2:
                return 'Los demás jugadores verán el grupo que usted haya elegido. También verán su apariencia que no cambia respecto ' \
                       'a las partes anteriores'
        elif self.player.treat == 3 or self.player.treat == 6:
            if value != 3:
                return 'Ls demás jugadores no verán el grupo que usted ha elegido. Pero sí verán su apariencia que no cambia ' \
                       'respecto a las partes anteriores'

    def cost_change_one_error_message(self, value):
        if self.player.treat >= 4:
            if value != 3:
                return 'Usted paga el costo fijo de 6 puntos más dos puntos por la única persona que decidió quedarse en el grupo'

    def cost_change_none_error_message(self, value):
        if self.player.treat >= 4:
            if value != 2:
                return 'Usted paga el costo fijo de 6 puntos y como todos los demás también se cambiaron, no paga ningún costo adicional'

class SummaryInstWP(WaitPage):
    wait_for_all_groups = True


class SummaryInst(Page):

    def vars_for_template(self):
        return self.player.vars_for_template()


page_sequence = [
    WelcomeP2WP,
    WelcomeP2,
    GroupChangeInstWP,
    GroupChangeInst,
    SummaryInstWP,
    SummaryInst,
]
