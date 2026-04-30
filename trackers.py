from utils import Timer
# Make a list of available resources and a list of the ones the player has obtained
class Resource():
    
    def __init__(self, name, amount:int =0, trend=0):
        self.name = name
        self.amount = amount
        self.trend = trend
        self.timer = Timer(self.name, self.add_res, 200)

    def add_res(self, amount: int= 1):
        self.amount += abs(amount)

    def remove_res(self, amount: int=1):
        positive_amount = abs(amount)
        if self.amount >= positive_amount:
            self.amount -= positive_amount

    def change_trend(self, new_trend):
        self.trend = new_trend

    def trend(self):
        self.amount += self.trend

    def get_amount(self):
        return self.amount

potatoes = Resource('potatoes', amount=10)

class Population(Resource):
    def __init__(self, name, amount=2, trend=1, lifespan=0):
        super().__init__(name, amount, trend)
        self.lifespan = lifespan

# Create class EdibleResource for food with "preference" attribute
# Every "day" each Population will consume 1 EdibleResource

population = Population("population")