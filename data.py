from math import floor, ceil

active_perks = []

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
def maintain_resources(dt):
    pass    

def maintain_all(dt):
    Population.update_population()
    # Maintain Consumption Rate
    total_consumption = 0
    total_production = 0
    queen.produce(dt)
    total_production = forager.amount * forager.efficiency
    for ant_type in Population.ant_types:
        total_consumption -= ant_type.consumption * ant_type.amount
    sugar.inc_dec_amount(total_production - abs(total_consumption))
    dew.inc_dec_amount(total_production - abs(total_consumption))


# Make a list of available resources and a list of the ones the player has obtained
class Resource():
    def __init__(self, name, amount:int =0):
        self.name = name
        self.amount = amount

    def add_res(self, amount: float = 1.0):
        self.amount += abs(amount)

    def remove_res(self, amount: float = 1.0):
        positive_amount = abs(amount)
        if self.amount >= positive_amount:
            self.amount -= positive_amount

    def inc_dec_amount(self, inc_dec_amount: float):
        self.amount += inc_dec_amount
        if self.amount < 0:
            self.amount = 0

    def get_amount(self):
        return floor(self.amount)

class Population(Resource):
    capacity = 10
    total_population = 0
    ant_types = []
    def __init__(self, name, amount=0, consumption=0, efficiency=0):
        super().__init__(name, amount)
        self.consumption = consumption
        self.efficiency = efficiency
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
    def __init__(self, name, amount=1, consumption=.05, efficiency=.01):
        super().__init__(name, amount, consumption, efficiency)
    
    def produce(self, dt):
        if Population.total_population >= Population.capacity:
            pass
        else:
            larvae.add_res(self.efficiency * dt)

class Larvae(Population):
    def __init__(self, name, amount=0, consumption=.005):
        super().__init__(name, amount, consumption)

    def produce(self, dt):
        pass

class Nursery(Larvae):
    def __init__(self, name, amount=0, consumption=.02):
        super().__init__(name, amount, consumption)

class Forager(Population):
    def __init__(self, name, amount=0, consumption=.2, efficiency=.01):
        super().__init__(name, amount, consumption, efficiency)

    def produce(self, dt):
        sugar.add_res(self.amount * self.efficiency * dt)
        dew.add_res(self.amount * self.efficiency * dt)


# Resources
sugar = Resource('sugar', amount=10)
dew = Resource('dew', amount=10)

# Populations
queen = Queen('queen')
larvae = Larvae("larvae")
nursery = Nursery('Nusery')
forager = Forager('forager')
# tunneler = Worker('tunneler')
# soldier = Worker('soldier')