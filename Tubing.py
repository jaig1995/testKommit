class Tubing():

    def __init__(self, flowCapacity, tanks):
        self.flowCapacity = flowCapacity
        self.tanks = tanks
        self.currentFlow = 0

    def getFlowCapacity(self):
        return self.flowCapacity

    def flowAvailable(self):
        return self.flowCapacity - self.currentFlow

    def addFlow(self):
        for tank in self.tanks:
            quantity = tank.getContent()
        if (self.currentFlow + quantity) > self.flowCapacity:
            self.currentFlow += self.flowAvailable()
            for tank in self.tanks:
                tank.pump(self.flowAvailable())
            return quantity - self.flowAvailable()
        self.currentFlow += quantity
        for tank in self.tanks:
            tank.pump(quantity)
        return 0

    def isBusy(self):
        if self.currentFlow == self.flowCapacity:
            return True
        return False