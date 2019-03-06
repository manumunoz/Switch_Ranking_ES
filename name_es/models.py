from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Manu Munoz'

doc = """
Identity Switch - Group Name ES
"""


class Constants(BaseConstants):
    #------------------------------------------
    name_in_url = 'name_es'
    names = ['1','2','3','4','5','6','7']
    players_per_group = len(names)
    periods = 1
    num_rounds = periods
    #------------------------------------------
    # Treatment & Group parameters
    players = len(names)
    others = len(names) - 1
    attribute = [1,5,1,5,1,1,5]
    attributes = {'1': 1, '2': 5, '3': 1, '4': 5, '5': 1, '6': 1, '7': 5}
    total_circles = 4
    total_triangles = 3
    circle = 1 # Majority
    triangle = 0 # Minority
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
    # def creating_session(self):
    #     for p in self.get_players():
    #         p.given_type = int(Constants.attribute[p.id_in_group - 1])

    # def creating_session(self):
    #     for g in self.get_groups():
    #         # assign types
    #         for p in g.get_players():
    #             p.given_type = self.participant.vars['given_type']
    #             p.chat_channel = (10 * g.id_in_subsession) + p.given_type #This works with max. 10 groups

    def assigning_given_types(self):
        for g in self.get_groups():
            # assign types
            for p in g.get_players():
                p.given_type = p.participant.vars['given_type']
                # p.given_type = int(Constants.attribute[p.id_in_group - 1])
                p.chat_channel = (10 * g.id_in_subsession) + p.given_type #This works with max. 10 groups

    def choosing_names(self):
        for g in self.get_groups():
            if g.total_group_a == Constants.total_circles:
                g.circles_coord = 1
                g.circles_name = 1
                g.circles_label = Constants.group_a
            elif g.total_group_b == Constants.total_circles:
                g.circles_coord = 1
                g.circles_name = 2
                g.circles_label = Constants.group_b
            elif g.total_group_c == Constants.total_circles:
                g.circles_coord = 1
                g.circles_name = 3
                g.circles_label = Constants.group_c
            elif g.total_group_d == Constants.total_circles:
                g.circles_coord = 1
                g.circles_name = 4
                g.circles_label = Constants.group_d
            elif g.total_group_e == Constants.total_circles:
                g.circles_coord = 1
                g.circles_name = 5
                g.circles_label = Constants.group_e

            if g.total_group_f == Constants.total_triangles:
                g.triangles_coord = 1
                g.triangles_name = 6
                g.triangles_label = Constants.group_f
            elif g.total_group_g == Constants.total_triangles:
                g.triangles_coord = 1
                g.triangles_name = 7
                g.triangles_label = Constants.group_g
            elif g.total_group_h == Constants.total_triangles:
                g.triangles_coord = 1
                g.triangles_name = 8
                g.triangles_label = Constants.group_h
            elif g.total_group_i == Constants.total_triangles:
                g.triangles_coord = 1
                g.triangles_name = 9
                g.triangles_label = Constants.group_i
            elif g.total_group_j == Constants.total_triangles:
                g.triangles_coord = 1
                g.triangles_name = 10
                g.triangles_label = Constants.group_j

    def failed_name_choice(self):
        for g in self.get_groups():
            if g.circles_coord == 0:
                g.circles_name = 1
                g.circles_label = Constants.group_a
            if g.triangles_coord == 0:
                g.triangles_name = 6
                g.triangles_label = Constants.group_f

    def try_one(self):
        for g in self.get_groups():
            if g.circles_coord == 1:
                g.circles_try_one = 1
            if g.triangles_coord == 1:
                g.triangles_try_one = 1

    def try_two(self):
        for g in self.get_groups():
            if g.circles_coord == 1 and g.circles_try_one == 0:
                g.circles_try_two = 1
            if g.triangles_coord == 1 and g.triangles_try_one == 0:
                g.triangles_try_two = 1

    def try_three(self):
        for g in self.get_groups():
            if g.circles_coord == 1 and g.circles_try_one == 0 and g.circles_try_two == 0:
                g.circles_try_three = 1
            if g.triangles_coord == 1 and g.triangles_try_one == 0 and g.triangles_try_two == 0:
                g.triangles_try_three = 1


class Group(BaseGroup):
    total_group_a = models.IntegerField()
    total_group_b = models.IntegerField()
    total_group_c = models.IntegerField()
    total_group_d = models.IntegerField()
    total_group_e = models.IntegerField()
    total_group_f = models.IntegerField()
    total_group_g = models.IntegerField()
    total_group_h = models.IntegerField()
    total_group_i = models.IntegerField()
    total_group_j = models.IntegerField()
    circles_coord = models.IntegerField(initial=0)
    triangles_coord = models.IntegerField(initial=0)
    circles_name = models.PositiveIntegerField()
    triangles_name = models.PositiveIntegerField()
    circles_label = models.StringField()
    triangles_label = models.StringField()
    circles_try_one = models.PositiveIntegerField(initial=0)
    circles_try_two = models.PositiveIntegerField(initial=0)
    circles_try_three = models.PositiveIntegerField(initial=0)
    triangles_try_one = models.PositiveIntegerField(initial=0)
    triangles_try_two = models.PositiveIntegerField(initial=0)
    triangles_try_three = models.PositiveIntegerField(initial=0)

    # def choosing_names(self):
    #     if self.total_group_a == Constants.total_circles:
    #         self.circles_coord = 1
    #         self.circles_name = 1
    #         self.circles_label = Constants.group_a
    #     elif self.total_group_b == Constants.total_circles:
    #         self.circles_coord = 1
    #         self.circles_name = 2
    #         self.circles_label = Constants.group_b
    #     elif self.total_group_c == Constants.total_circles:
    #         self.circles_coord = 1
    #         self.circles_name = 3
    #         self.circles_label = Constants.group_c
    #     elif self.total_group_d == Constants.total_circles:
    #         self.circles_coord = 1
    #         self.circles_name = 4
    #         self.circles_label = Constants.group_d
    #     elif self.total_group_e == Constants.total_circles:
    #         self.circles_coord = 1
    #         self.circles_name = 5
    #         self.circles_label = Constants.group_e
    #
    #     if self.total_group_f == Constants.total_triangles:
    #         self.triangles_coord = 1
    #         self.triangles_name = 6
    #         self.triangles_label = Constants.group_f
    #     elif self.total_group_g == Constants.total_triangles:
    #         self.triangles_coord = 1
    #         self.triangles_name = 7
    #         self.triangles_label = Constants.group_g
    #     elif self.total_group_h == Constants.total_triangles:
    #         self.triangles_coord = 1
    #         self.triangles_name = 8
    #         self.triangles_label = Constants.group_h
    #     elif self.total_group_i == Constants.total_triangles:
    #         self.triangles_coord = 1
    #         self.triangles_name = 9
    #         self.triangles_label = Constants.group_i
    #     elif self.total_group_j == Constants.total_triangles:
    #         self.triangles_coord = 1
    #         self.triangles_name = 10
    #         self.triangles_label = Constants.group_j
    #
    # def failed_name_choice(self):
    #     if self.circles_coord == 0:
    #         self.circles_name = 1
    #         self.circles_label = Constants.group_a
    #     if self.triangles_coord == 0:
    #         self.triangles_name = 6
    #         self.triangles_label = Constants.group_f
    #
    # def try_one(self):
    #     if self.circles_coord == 1:
    #         self.circles_try_one = 1
    #     if self.triangles_coord == 1:
    #         self.triangles_try_one = 1
    #
    # def try_two(self):
    #     if self.circles_coord == 1 and self.circles_try_one == 0:
    #         self.circles_try_two = 1
    #     if self.triangles_coord == 1 and self.triangles_try_one == 0:
    #         self.triangles_try_two = 1
    #
    # def try_three(self):
    #     if self.circles_coord == 1 and self.circles_try_one == 0 and self.circles_try_two == 0:
    #         self.circles_try_three = 1
    #     if self.triangles_coord == 1 and self.triangles_try_one == 0 and self.triangles_try_two == 0:
    #         self.triangles_try_three = 1


class Player(BasePlayer):
    given_type = models.IntegerField() # combination of symbol and preference
    chat_channel = models.IntegerField()
    group_a = models.IntegerField(initial=0)
    group_b = models.IntegerField(initial=0)
    group_c = models.IntegerField(initial=0)
    group_d = models.IntegerField(initial=0)
    group_e = models.IntegerField(initial=0)
    group_f = models.IntegerField(initial=0)
    group_g = models.IntegerField(initial=0)
    group_h = models.IntegerField(initial=0)
    group_i = models.IntegerField(initial=0)
    group_j = models.IntegerField(initial=0)

    group_name = models.PositiveIntegerField(
        choices=[
            [1, "{}%".format(Constants.group_a)],
            [2, "{}%".format(Constants.group_b)],
            [3, "{}%".format(Constants.group_c)],
            [4, "{}%".format(Constants.group_d)],
            [5, "{}%".format(Constants.group_e)],
            [6, "{}%".format(Constants.group_f)],
            [7, "{}%".format(Constants.group_g)],
            [8, "{}%".format(Constants.group_h)],
            [9, "{}%".format(Constants.group_i)],
            [10, "{}%".format(Constants.group_j)],
        ],
    )

    def role(self):
        return {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7'}[self.id_in_group]

    def chat_nickname(self):
        return 'Jugador {}'.format(self.role())

    def choice_value(self):
        if self.group_name == 1:
            self.group_a = 1
        elif self.group_name == 2:
            self.group_b = 1
        elif self.group_name == 3:
            self.group_c = 1
        elif self.group_name == 4:
            self.group_d = 1
        elif self.group_name == 5:
            self.group_e = 1
        if self.group_name == 6:
            self.group_f = 1
        elif self.group_name == 7:
            self.group_g = 1
        elif self.group_name == 8:
            self.group_h = 1
        elif self.group_name == 9:
            self.group_i = 1
        elif self.group_name == 10:
            self.group_j = 1

    def var_between_apps(self):
        self.participant.vars['circles_name'] = self.group.circles_name
        self.participant.vars['triangles_name'] = self.group.triangles_name
        self.participant.vars['circles_label'] = self.group.circles_label
        self.participant.vars['triangles_label'] = self.group.triangles_label
