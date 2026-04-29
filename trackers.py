
class Resource():
    
    def __init__(self, name, amount=0):
        self.name = name
        self.amount = amount

    def add_res(self, amount=1):
        self.amount += amount

    def remove_res(self, amount=1):
        self.amount -= amount

    def get_amount(self):
        return self.amount

potatoes = Resource('potatoes')