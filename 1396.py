class UndergroundSystem:

    def __init__(self):
        self.cust = {}
        self.route = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.cust:  # add current customer to the stk
            self.cust[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        combo = (self.cust[id][0], stationName)  # current cust start station and current station
        if combo not in self.route:
            self.route[combo] = []
        self.route[combo].append(t - self.cust[id][1])
        del self.cust[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.route[(startStation, endStation)]) / len(self.route[(startStation, endStation)])

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)