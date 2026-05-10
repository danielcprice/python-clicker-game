from math import floor

def win_loss_check():
    if food.amount < 1:
        if larvae.amount > 0:
            larvae.amount -= .1
        elif larvae.amount < 1:
            return 'lose'
        
    if Population.total_population >= 100000:
        return 'win'
            

def maintain_all(dt):
    Population.update_population()
    # Maintain Consumption Rate
    total_consumption = 0
    total_production = 0
    queen.produce(dt)
    larvae.produce(dt)
    total_production = forager.amount * forager.efficiency
    for ant_type in Population.ant_types:
        total_consumption -= ant_type.consumption * ant_type.amount
    food.inc_dec_amount(total_production - abs(total_consumption))
    print(larvae.amount)
    print(forager.amount)


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
            if self.amount < 1:
                self.amount = abs(self.amount)

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
        return floor(self.amount)
    
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
    def __init__(self, name, amount=1, consumption=.05, efficiency=.2):
        super().__init__(name, amount, consumption, efficiency)
    
    def produce(self, dt):
        if Population.total_population >= Population.capacity:
            pass
        else:
            larvae.add_res(self.efficiency * dt)

class Larvae(Population):
    def __init__(self, name, amount=0, consumption=.005, efficiency=1):
        super().__init__(name, amount, consumption)
        self.efficiency = efficiency
        self.ant_limits = {'forager': 3, 'nursery': 3, 'tunneller': 3, 'soldier': 3}


    def update_ant_limites():
        pass

    def produce(self, dt):
        larvae_change = self.efficiency * dt
        if larvae.amount > 1:
            if forager.get_amount() < self.ant_limits['forager']:
                larvae.amount -= 1
                forager.amount += 1
                pass
            elif nursery.get_amount() < self.ant_limits['nursery']:
                larvae.amount -= 1
                nursery.amount += 1
                pass
            elif soldier.get_amount() < self.ant_limits['soldier']:
                larvae.amount -= 1
                soldier.amount += 1
                pass
            elif tunneller.get_amount() < self.ant_limits['tunneller']:
                larvae.amount -= 1
                tunneller.amount += 1
                pass



class Nursery(Larvae):
    def __init__(self, name, amount=0, consumption=.02):
        super().__init__(name, amount, consumption)

class Forager(Population):
    def __init__(self, name, amount=0, consumption=.2, efficiency=.21):
        super().__init__(name, amount, consumption, efficiency)

    def produce(self, dt):
        food.add_res(self.amount * (self.efficiency * dt))

class Tunneler(Population):
    def __init__(self, name, amount=0, consumption=.2, efficiency=.21):
        super().__init__(name, amount, consumption, efficiency)

    def produce(self, dt):
        food.add_res(self.amount * (self.efficiency * dt))

class Soldier(Population):
    def __init__(self, name, amount=0, consumption=.2, efficiency=.21):
        super().__init__(name, amount, consumption, efficiency)

    def produce(self, dt):
        food.add_res(self.amount * (self.efficiency * dt))


# Resources
food = Resource('food', amount=2)
# dew = Resource('dew', amount=10)

# Populations
queen = Queen('queen', 1)
larvae = Larvae("larvae", 1)
nursery = Nursery('Nusery')
forager = Forager('forager', 0)
tunneller = Tunneler('tunneler')
soldier = Soldier('soldier')