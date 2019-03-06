from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from collections import OrderedDict
import json
import itertools

author = 'Manu Munoz'

doc = """
Identity Switch - Networks: FLUID
"""


class Constants(BaseConstants):
    #------------------------------------------
    name_in_url = 'fluid_es'
    names = ['1','2','3','4','5','6','7']
    players_per_group = len(names)
    instructions_template = 'fluid_es/Instructions.html'
    periods = 10
    num_rounds = periods
    #------------------------------------------
    # Treatment & Group parameters
    others = len(names) - 1
    attribute = [1,5,1,5,1,1,5]
    attributes = {'1': 1, '2': 5, '3': 1, '4': 5, '5': 1, '6': 1, '7': 5}
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
    link_cost = 2
    liked_gain = 6
    disliked_gain = 4
    personal = 1
    exchange = 2
    switch_cost = 6
    switch_free = 0
    #------------------------------------------
    one = 1
    zero = 0
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
        num_players_err = 'Too many participants for such a short name list'
        # the following may create issues with mTurk sessions where num participants is doubled
        assert len(Constants.names) <= self.session.num_participants, num_players_err
        '''
        for g in self.get_groups():
            cur_names = Constants.names.copy()
            # random.shuffle(cur_names)
            for i, p in enumerate(g.get_players()):
                p.name = cur_names[i]
        '''
        # for p in self.get_players():
        #     p.given_type = int(Constants.attribute[p.id_in_group - 1])
        #     if p.given_type == 1: # circle-circle
        #         p.was_circle = 1
        #     else: # triangle-triangle
        #         p.was_circle = 0

        if self.round_number == 1:
            paying_round_2 = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round_2'] = paying_round_2

    def assigning_given_types(self):
        for g in self.get_groups():
            # assign types
            for p in g.get_players():
                p.given_type = p.participant.vars['given_type']
                if p.given_type == 1: # circle-circle
                    p.was_circle = 1
                else: # triangle-triangle
                    p.was_circle = 0


class Group(BaseGroup):
    total_init_circles = models.IntegerField()
    total_init_triangles = models.IntegerField()
    total_circles = models.IntegerField()
    total_triangles = models.IntegerField()
    total_up = models.IntegerField()
    total_down = models.IntegerField()
    network_data = models.LongStringField()
    total_circle_switch = models.IntegerField()
    total_triangle_switch = models.IntegerField()

    def assign_random_names_and_positions(self):
        name_indexes = random.sample(range(7), 7)
        positions = random.sample(range(7), 7)
        i = 0
        for p in self.get_players():
            p.name = Constants.names[name_indexes[i]]
            p.position = positions[i] + 1
            i += 1

    def generate_nodes(self):
        players = self.get_players()
        players.sort(key=lambda x: x.position)
        return [{'data': {'id': p.name, 'name': p.name, 'action': p.action, 'given': p.given_type,
                           'shape': p.chosen_type, 'location': p.position, 'treat': p.treat}, 'group': 'nodes'}
                for p in players]

    def displaying_network(self):
        nodes = self.generate_nodes()
        edges = []
        elements = nodes + edges
        style = [{'selector': 'node', 'style': {'content': 'data(name)'}}]
        self.network_data = json.dumps({'elements': elements,
                                        'style': style,
                                        })

    def forming_network(self):
        nodes = self.generate_nodes()
        edges = []
        for p in self.get_players():
            friends = json.loads(p.friends)
            edges.extend(
                [{'data': {'id': p.name + '_' + str(i), 'source': p.name, 'target': i}, 'group': 'edges'}
                 for i in friends])

            # Copio el valor de las propuestas recogido en las variables con numbre (1,2,3,...) a
            # prop_to_1, prop_to_2, ...
            for i in friends:
                setattr(p, 'prop_to_' + i, getattr(p, i))

        elements = nodes + edges
        style = [{'selector': 'node', 'style': {'content': 'data(name)'}}]
        self.network_data = json.dumps({'elements': elements,
                                        'style': style,
                                        })

    def choosing_types(self):
        for player in self.get_players():
            if player.chosen_type == 1:
                player.is_circle = 1
                player.liked_action = 1
            elif player.chosen_type == 2:
                player.is_circle = 0
                player.liked_action = 0
            elif player.chosen_type == 3:
                player.is_circle = 1
                player.liked_action = 1
            elif player.chosen_type == 4:
                player.is_circle = 0
                player.liked_action = 0
            elif player.chosen_type == 5:
                player.is_circle = 0
                player.liked_action = 0
            elif player.chosen_type == 6:
                player.is_circle = 1
                player.liked_action = 1
            elif player.chosen_type == 7:
                player.is_circle = 1
                player.liked_action = 1
            else:
                player.is_circle = 0
                player.liked_action = 0

    def switching_choice(self):
        for player in self.get_players():
            if player.treat == 1 or player.treat == 4:
                if player.given_type == 1 and player.chosen_type == 5:
                        player.switch = 1
                        player.circle_switch = 1
                elif player.given_type == 1 and player.chosen_type == 1:
                        player.switch = 0
                elif player.given_type == 5 and player.chosen_type == 1:
                        player.switch = 1
                        player.triangle_switch = 1
                elif player.given_type == 5 and player.chosen_type == 5:
                        player.switch = 0
            elif player.treat == 2 or player.treat == 5:
                if player.given_type == 1 and player.chosen_type == 2:
                        player.switch = 1
                        player.circle_switch = 1
                elif player.given_type == 1 and player.chosen_type == 1:
                        player.switch = 0
                elif player.given_type == 5 and player.chosen_type == 6:
                        player.switch = 1
                        player.triangle_switch = 1
                elif player.given_type == 5 and player.chosen_type == 5:
                        player.switch = 0
            elif player.treat == 3 or player.treat == 6:
                if player.given_type == 1 and player.chosen_type == 4:
                        player.switch = 1
                        player.circle_switch = 1
                elif player.given_type == 1 and player.chosen_type == 3:
                        player.switch = 0
                elif player.given_type == 5 and player.chosen_type == 7:
                        player.switch = 1
                        player.triangle_switch = 1
                elif player.given_type == 5 and player.chosen_type == 8:
                        player.switch = 0

    def summing_switching(self):
        players = self.get_players()
        switch_cir = [p.circle_switch for p in players]
        switch_tri = [p.triangle_switch for p in players]
        self.total_circle_switch = sum(switch_cir)
        self.total_triangle_switch = sum(switch_tri)

    def ingroup_switching(self):
        for p in self.get_players():
            if p.given_type == 1:
                p.ingroup_switch = self.total_circle_switch
                p.ingroup_noswitch = Constants.n_maj - p.ingroup_switch
            else:
                p.ingroup_switch = self.total_triangle_switch
                p.ingroup_noswitch = Constants.n_min - p.ingroup_switch

    def switching_costs(self):
        for player in self.get_players():
            if player.treat == 1 or player.treat == 2 or player.treat == 3:
                player.switch_cost = 0
            elif player.treat == 4 or player.treat == 5 or player.treat == 6:
                if player.given_type == 1 and player.switch == 1:
                    player.switch_cost = Constants.switch_cost + Constants.multiplier * (Constants.n_maj - player.ingroup_switch)
                elif player.given_type == 1 and player.switch == 0:
                        player.switch_cost = 0
                elif player.given_type == 5 and player.switch == 1:
                    player.switch_cost = Constants.switch_cost + Constants.multiplier * (Constants.n_min - player.ingroup_switch)
                elif player.given_type == 5 and player.switch == 0:
                        player.switch_cost = 0

    def summing_initial_types(self):
        players = self.get_players()
        init_circles = [p.was_circle for p in players]
        self.total_init_circles = sum(init_circles)
        self.total_init_triangles = len(Constants.names)-self.total_init_circles

    def summing_types(self):
        players = self.get_players()
        circles = [p.is_circle for p in players]
        self.total_circles = sum(circles)
        self.total_triangles = len(Constants.names)-self.total_circles

    def calculate_props_from_and_links(self):
        for player_to in self.get_players():
            for player_from in self.get_players():
                kiubo_prop_from = False
                kiubo_link = 0
                if player_from.name != player_to.name: # si no soy yo mismo
                    kiubo_prop_from = bool(getattr(player_from, 'prop_to_' + player_to.name)) # cojo el valor de la propuesta
                    if getattr(player_to, 'prop_to_' + player_from.name) == True and kiubo_prop_from == True:
                        kiubo_link = 1
                    else:
                        kiubo_link = 0
                else:
                    kiubo_link = 0 # link conmigo mismo = 1

                setattr(player_to, 'prop_from_' + player_from.name, kiubo_prop_from) # la añado a prop_from_X
                setattr(player_to, 'link_with_' + player_from.name, kiubo_link)

    def calculate_degree(self):
        for player in self.get_players():
            player.out_degree = player.prop_to_1 + player.prop_to_2 + player.prop_to_3 + player.prop_to_4 + player.prop_to_5 +\
                                player.prop_to_6 + player.prop_to_7
            player.degree = player.link_with_1 + player.link_with_2 + player.link_with_3 + player.link_with_4 + player.link_with_5 + \
                            player.link_with_6 + player.link_with_7

    def linking_costs(self):
        for player in self.get_players():
            if player.out_degree >= 1:
                player.linking_costs = player.out_degree * Constants.link_cost
            else:
                player.linking_costs = 0

    def calculate_actions(self):
        for player in self.get_players():
            for partner in self.get_players():
                action_up = partner.action
                if action_up == 1:
                    choice = 1
                else:
                    choice = 0
                setattr(player, 'action_' + partner.name, choice) # la añado a prop_from_X

    def sum_coordinations(self):
        for player in self.get_players():
            if player.action == player.action_1 and player.link_with_1 == 1:
                player.coordinate_1 = 1
            else:
                player.coordinate_1 = 0
            if player.action == player.action_2 and player.link_with_2 == 1:
                player.coordinate_2 = 1
            else:
                player.coordinate_2 = 0
            if player.action == player.action_3 and player.link_with_3 == 1:
                player.coordinate_3 = 1
            else:
                player.coordinate_3 = 0
            if player.action == player.action_4 and player.link_with_4 == 1:
                player.coordinate_4 = 1
            else:
                player.coordinate_4 = 0
            if player.action == player.action_5 and player.link_with_5 == 1:
                player.coordinate_5 = 1
            else:
                player.coordinate_5 = 0
            if player.action == player.action_6 and player.link_with_6 == 1:
                player.coordinate_6 = 1
            else:
                player.coordinate_6 = 0
            if player.action == player.action_7 and player.link_with_7 == 1:
                player.coordinate_7 = 1
            else:
                player.coordinate_7 = 0

    def coordination_score(self):
        for player in self.get_players():
            player.coordination_score = 1 + player.coordinate_1 + player.coordinate_2 + \
                                        player.coordinate_3 + player.coordinate_4 + player.coordinate_5 + \
                                        player.coordinate_6 + player.coordinate_7

    def values_coordination(self):
        for player in self.get_players():
            if player.action == player.liked_action:
                player.coordination_gains = player.coordination_score * Constants.liked_gain
            else:
                player.coordination_gains = player.coordination_score * Constants.disliked_gain

    def round_gains(self):
        for player in self.get_players():
            player.round_gains = player.coordination_gains - player.linking_costs - player.switch_cost

    def round_payoffs(self):
        for player in self.get_players():
            if self.subsession.round_number == self.session.vars['paying_round_2']:
                player.payoff = player.round_gains
            else:
                player.payoff = Constants.switch_free

    def round_points(self):
        for player in self.get_players():
            if self.subsession.round_number == self.session.vars['paying_round_2']:
                player.points_fluid = player.round_gains
            else:
                player.points_fluid = 0

    def summing_choices(self):
        players = self.get_players()
        action_up = [p.action for p in players]
        self.total_up = sum(action_up)
        self.total_down = len(Constants.names) - self.total_up


class Player(BasePlayer):
    treat = models.IntegerField() # Treatments from 1 to 3
    given_type = models.IntegerField() # combination of symbol and preference
    chosen_type = models.IntegerField() # combination of symbol and preference
    was_circle = models.IntegerField()
    is_circle = models.IntegerField()
    action = models.IntegerField() # Reported belief on P3's verification
    old_action = models.IntegerField() # Reported belief on P3's verification
    liked_action = models.IntegerField()
    out_degree = models.IntegerField()
    degree = models.IntegerField()
    coordination_score = models.IntegerField()
    coordination_gains = models.IntegerField()
    linking_costs = models.IntegerField()
    round_gains = models.IntegerField()
    points_fluid = models.IntegerField()
    switch = models.IntegerField()
    switch_cost = models.IntegerField()
    circle_switch = models.IntegerField(initial=0)
    triangle_switch = models.IntegerField(initial=0)
    ingroup_switch = models.IntegerField(initial=0)
    ingroup_noswitch = models.IntegerField(initial=0)

    def vars_for_template(self):
        return {
            'circles_name': self.participant.vars['circles_name'],
            'triangles_name': self.participant.vars['triangles_name'],
            'circles_label': self.participant.vars['circles_label'],
            'triangles_label': self.participant.vars['triangles_label'],
            'names': len(Constants.names)
        }

    def var_between_apps(self):
        if self.subsession.round_number == self.session.vars['paying_round_2']:
            self.participant.vars['part_fluid_round'] = self.session.vars['paying_round_2']
            self.participant.vars['part_fluid_payoff'] = self.points_fluid

    name = models.StringField()
    friends = models.LongStringField()
    position = models.IntegerField()

    for i in Constants.names:
        locals()[i] = models.BooleanField(widget=widgets.CheckboxInput, blank=True)
        # Añado a Player las variables de propuestas con friendly names que luego rellenaremos
        locals()['prop_to_' + i] = models.BooleanField(initial=0)
        locals()['prop_from_' + i]= models.BooleanField(initial=0)
        locals()['link_with_' + i]= models.IntegerField(initial=0)
        locals()['action_' + i]= models.IntegerField(initial=0)
        locals()['coordinate_' + i]= models.IntegerField(initial=0)

    del locals()['i']