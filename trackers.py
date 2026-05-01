from utils import Timer
from math import floor, ceil

# Need to handle population states
pop_states = {'hunger': False, 'happiness': 0}
waste_modifier = Population.population

def maintain_all():
    hunger_check()
    maintain_trends()


def hunger_check():

    for food in EdibleResource.food_list:
        if EdibleResource.food_list[food] > 0:
            pop_states['hunger'] = False
        else:
            pop_states['hunger'] == True

    if pop_states['hunger'] == True:
        adj_happiness('DOWN', 5)
    
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


# Make a list of available resources and a list of the ones the player has obtained
class Resource():
    unlocked_resources = []
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
    
class EdibleResource(Resource):
    food_list = []
    def __init__(self, name, amount = 0, trend=0):
        super().__init__(name, amount, trend)

class Product(Resource):
    # Cost will eventually be a dictionary
    def __init__(self, cost: dict, name, amount = 0, trend=0):
        super().__init__(name, amount, trend)
        self.cost = cost

    def apply_cost(self):
        pass

    def change_cost(self):
        pass

# Trend for raw edible resources should be -1 per 2 population
# and +1 per 5 population
# Trend for cooked edible resources could be -1 per 5 population and +1 per 1 "cook"
# Population with "jobs" will no longer do the grunt work of collecting basic resources
potatoes = Resource('potatoes', amount=10, trend=-1)

class Population(Resource):
    capacity = 1
    def __init__(self, name, amount=0, trend=-.1):
        super().__init__(name, amount, trend)

    def increase_cap(self, amount):
        capacity += amount

    def trend(self):
        if self.amount >= abs(self.trend_amount):
            self.amount += (self.trend_amount + (pop_states['happiness'] / 100))
        else:
            self.amount = 0

    def get_amount(self):
        return ceil(self.amount)

population = Population("population", amount=10, trend=-.9)