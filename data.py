from math import floor, ceil

# For storing data
main_menu_buttons = []
statuses = {'hunger': 0, 'happiness': 0}

space = {1: 'algae'}

active_perks = []

pos_perks = {'happy': 0}

neg_perks = {'picky_eaters': 0}

all_resources = []

all_products = []

all_populations = []

main_menu_game_summary = 'You are in your bunker when the wasteland arrives.' \
'Now you must work hard to keep yourself alive. Hopefully you don\'t go mad before' \
'you\'re able to make some friends!'

# Need to handle population states
pop_states = {'hunger': False, 'happiness': 0}
# waste_modifier = Population.population


# def hunger_check():

#     for food in EdibleResource.food_list:
#         if EdibleResource.food_list[food] > 0:
#             pop_states['hunger'] = False
#         else:
#             pop_states['hunger'] == True

#     if pop_states['hunger'] == True:
#         adj_happiness('DOWN', 5)
    
# def adj_happiness(direction: str = 'UP', amount=1):
#     if direction == 'UP':
#         if pop_states['happiness'] < 50:
#             pop_states['happiness'] += abs(amount)
#         else:
#             pass
#     elif direction == 'DOWN':
#         if pop_states['happiness'] > -50:
#             pop_states['happiness'] -= abs(amount)
#         else:
#             pass

def maintain_consumption(dt):
    for ant_type in Population.ant_types:
        sugar.remove_res(ant_type.get_consumption(dt))

def maintain_all(dt):
    Population.update_population()
    maintain_consumption(dt)


# Make a list of available resources and a list of the ones the player has obtained
class Resource():
    def __init__(self, name, amount:int =0):
        self.name = name
        self.amount = amount

    def add_res(self, amount: int= 1):
        self.amount += abs(amount)

    def remove_res(self, amount: int=1):
        positive_amount = abs(amount)
        if self.amount >= positive_amount:
            self.amount -= positive_amount

    def get_amount(self):
        return floor(self.amount)

# Trend for raw edible resources should be -1 per 2 population
# and +1 per 5 population
# Trend for cooked edible resources could be -1 per 5 population and +1 per 1 "cook"
# Population with "jobs" will no longer do the grunt work of collecting basic resources
dew = Resource('dew', amount=10)

class Population(Resource):
    capacity = 10
    total_population = 0
    ant_types = []
    def __init__(self, name, amount=0, consumption=1):
        super().__init__(name, amount)
        self.consumption = consumption
        Population.ant_types.append(self)

    def get_consumption(self, dt):
        return self.amount * self.consumption * dt

    def get_amount(self):
        return ceil(self.amount)
    
    def update_population():
        Population.total_population = 0
        for ant_type in Population.ant_types:
            Population.total_population += int(ant_type.amount)
    
    @staticmethod
    def increase_cap(inc_amount=1):
        Population.capacity += inc_amount

    @staticmethod
    def decrease_cap(dec_amount=1):
        Population.capacity -= abs(dec_amount)

class Queen(Population):
    def __init__(self, name, amount=1, consumption=0):
        super().__init__(name, amount, consumption)
        pass

    

class Larvae(Population):
    def __init__(self, name, amount=0, consumption=0):
        super().__init__(name, amount, consumption)

class Worker(Population):
    def __init__(self, name, amount=0, consumption=0):
        super().__init__(name, amount, consumption)


# Resources
sugar = Resource('sugar', amount=10)
dew = Resource('dew', amount=10)

# Populations
queen = Queen('queen')
larvae = Larvae("larvae")
forager = Worker('forager')
nursery = Worker('nursery')
tunneler = Worker('tunneler')
soldier = Worker('soldier')