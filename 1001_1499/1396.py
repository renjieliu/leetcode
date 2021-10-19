class UndergroundSystem:

    def __init__(self):
        self.customer_in = {}
        self.station = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer_in[id] = [stationName, t]  # customer in stamp

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.customer_in[id] += [stationName, t]  # [inStation, t, outStation, t] #record the customer's trip
        arr = self.customer_in[id]
        if (arr[0], arr[2]) not in self.station:
            self.station[(arr[0], arr[2])] = []
        self.station[(arr[0], arr[2])].append(arr[3] - arr[1])  # add the timestamp to the station combination
        del self.customer_in[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.station[(startStation, endStation)]) / len(self.station[(startStation, endStation)])

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)