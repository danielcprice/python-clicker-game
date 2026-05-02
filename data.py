from utils import Timer
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
    
def adj_happiness(direction: str = 'UP', amount=1):
    if direction == 'UP':
        if pop_states['happiness'] < 50:
            pop_states['happiness'] += abs(amount)
        else:
            pass
    elif direction == 'DOWN':
        if pop_states['happiness'] > -50:
            pop_states['happiness'] -= abs(amount)
        else:
            pass

def maintain_trends():
    for timer in Timer.timer_list:
        timer.check_timer()

def maintain_all():
    Population.update_population()
    maintain_trends()


# Make a list of available resources and a list of the ones the player has obtained
class Resource():
    def __init__(self, name, amount:int =0, trend=0):
        self.name = name
        self.amount = amount
        self.trend_amount = trend
        self.timer = Timer(self.name, self.trend, 1000)

    def add_res(self, amount: int= 1):
        self.amount += abs(amount)

    def remove_res(self, amount: int=1):
        positive_amount = abs(amount)
        if self.amount >= positive_amount:
            self.amount -= positive_amount

    def change_trend(self, new_trend):
        self.trend = new_trend

    def trend(self):
        if self.amount >= abs(self.trend_amount):
            if pop_states['hunger'] == True:
                self.amount += (abs(self.trend_amount) * -2)
            else:
                self.amount += self.trend_amount
        else:
            self.amount = 0

    def get_amount(self):
        return floor(self.amount)

# Trend for raw edible resources should be -1 per 2 population
# and +1 per 5 population
# Trend for cooked edible resources could be -1 per 5 population and +1 per 1 "cook"
# Population with "jobs" will no longer do the grunt work of collecting basic resources
dew = Resource('dew', amount=10, trend=-1)

class Population(Resource):
    capacity = 10
    total_population = 0
    ant_types = []
    def __init__(self, name, amount=0, trend=0):
        super().__init__(name, amount, trend)
        Population.ant_types.append(self)

    def trend(self):
        if Population.total_population >= Population.capacity:
            pass
        else:
            if self.amount >= abs(self.trend_amount):
                self.amount += (self.trend_amount + (pop_states['happiness'] / 100))
            else:
                self.amount = 0

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
    def __init__(self, name, amount=1, trend=0):
        super().__init__(name, amount, trend)

    

class Larvae(Population):
    def __init__(self, name, amount=0, trend=0):
        super().__init__(name, amount, trend)

class Worker(Population):
    def __init__(self, name, amount=0, trend=0):
        super().__init__(name, amount, trend)


# Resources
sugar = Resource('sugar', amount=10, trend=-1)
dew = Resource('dew', amount=10, trend=-1)

# Populations
queen = Queen("queen")
larvae = Larvae("larvae", amount=0, trend=.1)
forager = Worker('forager')
nursery = Worker('nursery')
tunneler = Worker('tunneler')
soldier = Worker('soldier')