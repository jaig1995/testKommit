class Tank():

    def __init__(self, capacity):
        self.capacity = capacity
        self.content = 0

    def getCapacity(self):
        return self.capacity

    def getContent(self):
        return self.content

    def quantityAvailable(self):
        return self.capacity - self.content

    def fill(self, quantity):
        if quantity > self.quantityAvailable():
            self.content += self.quantityAvailable()
            return quantity - self.quantityAvailable()
        self.content += quantity
        return 0

    def isFilled(self):
        if self.content == self.capacity:
            return True
        return False

    def pump(self, quatity):
        if quatity > self.content:
            return False
        else:
            self.content -= quatity
            return True
