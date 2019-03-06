from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Manu Munoz'

doc = """
Identity Switch - Networks: Instructions FIXED
"""


class Constants(BaseConstants):
    #------------------------------------------
    name_in_url = 'inst_fixed_es'
    names = ['1','2','3','4','5','6','7']
    players_per_group = len(names)
    instructions_template = 'inst_fixed_es/Instructions.html'
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
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

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

    active = models.PositiveIntegerField(
        choices=[
            [1, 'Cuando yo le propongo una relación a otro jugador sin importar si este me propone una relación a mí'],
            [2, 'Cuando otro jugador me propone una relación a mí sin importar si yo le propongo una relación a él'],
            [3, 'Cuando yo le propongo una relación a otro jugador que también me propone una relación a mí']
        ],
        widget=widgets.RadioSelect
    )

    count = models.PositiveIntegerField(
        choices=[
            [1, '5'],
            [2, '4'],
            [3, '3']
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

    pay_nocoord = models.PositiveIntegerField(
        choices=[
            [1, 'Yo gano 6 y pago el costo de 2 = 4 puntos en total'],
            [2, 'Yo gano 4 y pago el costo de 2 = 2 puntos en total'],
            [3, 'Yo gano 0 y pago el costo de 2 = -2 puntos en total']
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
