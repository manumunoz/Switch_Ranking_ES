from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import itertools


author = 'Manu Munoz'

doc = """
Identity Switch - Networks: Instructions FLUID
"""

class Constants(BaseConstants):
    #------------------------------------------
    name_in_url = 'inst_fluid_es'
    names = ['1','2','3','4','5','6','7']
    players_per_group = len(names)
    instructions_template = 'inst_fluid_es/Instructions.html'
    periods = 1
    num_rounds = periods
    #------------------------------------------
    # Treatment & Group parameters
    others = len(names) - 1
    total_circles = 4
    total_triangles = 3
    part_task = 1
    part_name = 2
    part_fixed = 3
    part_fluid = 4
    part_alloc = 5
    rounds_fixed = 10
    #------------------------------------------
    # Payoffs
    exp_currency = "puntos"
    currency = "pesos"
    currency_exchange = 800
    points_exchange = 1
    min_pay = 10000
    link_cost = 2
    liked_gain = 6
    disliked_gain = 4
    switch_cost = 6
    #------------------------------------------
    # Interdependent Costs
    multiplier = 2
    n_min = 3
    n_maj = 4
    #------------------------------------------
    # Group Names
    group_a = 'Leones' #Leones
    group_b = 'Tigres' #Tigres
    group_c = 'Leopardos' #Leopardos
    group_d = 'Jaguares' #Jaguares
    group_e = 'Gatos' #Gatos
    group_f = 'Coyotes' #Coyotes
    group_g = 'Chacales' #Chacales
    group_h = 'Lobos' #Lobos
    group_i = 'Zorros' #Zorros
    group_j = 'Perros' #Perros
    #------------------------------------------


class Subsession(BaseSubsession):
    def creating_session(self):
        treat = itertools.cycle([1, 2, 3, 4, 5, 6])
        # 1: Full-Free, 2: Sticky-Free, 3: Blurry-Free, 4: Full-Cost, 5: Sticky-Cost, 6: Blurry-Cost
        # for p in self.get_players():
        #     p.treat = next(treat)
        for p in self.get_players():
            if 'treatment' in self.session.config:
                # demo mode
                p.treat = self.session.config['treatment']
            else:
                # live experiment mode
                p.treat = next(treat)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treat = models.IntegerField() # Treatments from 1 to 6

    given_group = models.PositiveIntegerField(
        choices=[
            [1, 'Está fijo y no cambia'],
            [2, 'El computador lo cambia en cada ronda'],
            [3, 'Yo lo puedo cambiar en cada ronda'],
        ],
        widget=widgets.RadioSelect
    )

    appearance = models.PositiveIntegerField(
        choices=[
            [1, 'Está fija y no cambia'],
            [2, 'El computador la cambia en cada ronda'],
            [3, 'Yo la puedo cambiar en cada ronda al cambiar mi grupo'],
        ],
        widget=widgets.RadioSelect
    )

    label = models.PositiveIntegerField(
        choices=[
            [1, 'Está fija y no cambia'],
            [2, 'El computador la cambia en cada ronda'],
            [3, 'Yo la puedo cambiar en cada ronda'],
        ],
        widget=widgets.RadioSelect
    )

    cost_change_one = models.PositiveIntegerField(
        choices=[
            [1, '6 fijos + 2 por 2 personas que no se cambiaron = 10 puntos'],
            [2, '6 fijos + 0 porque todas las personas cambiaron = 6 puntos'],
            [3, '6 fijos + 2 por 1 persona que no se cambió = 8 puntos']
        ],
        widget=widgets.RadioSelect
    )

    cost_change_none = models.PositiveIntegerField(
        choices=[
            [1, '6 fijos + 2 por 2 personas que no se cambiaron = 10 puntos'],
            [2, '6 fijos + 0 porque todas las personas cambiaron = 6 puntos'],
            [3, '6 fijos + 2 por 1 persona que no se cambió = 8 puntos']
        ],
        widget=widgets.RadioSelect
    )

    pay_coord = models.PositiveIntegerField(
        choices=[
            [1, 'Yo gano 6 y pago el costo de 2 = 4 puntos en total'],
            [2, 'Yo gano 4 y pago el costo de 2 = 2 puntos en total'],
            [3, 'Yo gano 0 y pago el costo de 2 = -2 puntos en total']
        ],
        widget=widgets.RadioSelect
    )

    pay_coord2 = models.PositiveIntegerField(
        choices=[
            [1, 'Yo gano 6 y pago el costo de 2 = 4 puntos en total'],
            [2, 'Yo gano 4 y pago el costo de 2 = 2 puntos en total'],
            [3, 'Yo gano 0 y pago el costo de 2 = -2 puntos en total']
        ],
        widget=widgets.RadioSelect
    )

    information = models.PositiveIntegerField(
        choices=[
            [1, 'Ellos pueden ver el grupo que yo elija y mi nueva apariencia'],
            [2, 'Ellos pueden ver el grupo que yo elija y mi apariencia de la Parte {}'.format(Constants.part_fixed)],
            [3, 'Ellos no pueden ver el grupo que yo elija sólo mi apariencia de la Parte {}'.format(Constants.part_fixed)],
        ],
        widget=widgets.RadioSelect
    )

    def vars_for_template(self):
        return {
            'circles_name': self.participant.vars['circles_name'],
            'triangles_name': self.participant.vars['triangles_name'],
            'circles_label': self.participant.vars['circles_label'],
            'triangles_label': self.participant.vars['triangles_label'],
            'names': len(Constants.names)
        }