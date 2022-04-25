class UndergroundSystem:

    def __init__(self):
        self.route = {}
        self.cust = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None: #O(1 | N)
        if id not in self.cust: 
            self.cust[id] = {}
        self.cust[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None: #O(1 | N)
        from_to = self.cust[id][0] + "-" + stationName  #the from and to station
        if from_to not in self.route:
            self.route[from_to] = [0, 0] #[total_time, count]
        
        self.route[from_to][0] += t - self.cust[id][1]
        self.route[from_to][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float: #O(1 | 1)
        # print(self.route)
        return self.route[startStation + "-" + endStation][0] / self.route[startStation + "-" + endStation][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)




# previous solution

# class UndergroundSystem:

#     def __init__(self):
#         self.customer_in = {}
#         self.station = {}

#     def checkIn(self, id: int, stationName: str, t: int) -> None:
#         self.customer_in[id] = [stationName, t]  # customer in stamp

#     def checkOut(self, id: int, stationName: str, t: int) -> None:
#         self.customer_in[id] += [stationName, t]  # [inStation, t, outStation, t] #record the customer's trip
#         arr = self.customer_in[id]
#         if (arr[0], arr[2]) not in self.station:
#             self.station[(arr[0], arr[2])] = []
#         self.station[(arr[0], arr[2])].append(arr[3] - arr[1])  # add the timestamp to the station combination
#         del self.customer_in[id]

#     def getAverageTime(self, startStation: str, endStation: str) -> float:
#         return sum(self.station[(startStation, endStation)]) / len(self.station[(startStation, endStation)])

# # Your UndergroundSystem object will be instantiated and called as such:
# # obj = UndergroundSystem()
# # obj.checkIn(id,stationName,t)
# # obj.checkOut(id,stationName,t)
# # param_3 = obj.getAverageTime(startStation,endStation)



# previous solution

# class UndergroundSystem:

#     def __init__(self):
#         self.cust = {}
#         self.route = {}      
        
#     def checkIn(self, id: int, stationName: str, t: int) -> None:
#         if id not in self.cust: #add current customer to the stk
#             self.cust[id] = [stationName, t] 
        
#     def checkOut(self, id: int, stationName: str, t: int) -> None:
#         combo = (self.cust[id][0], stationName) #current cust start station and current station
#         if combo not in self.route:
#             self.route[combo] = []
#         self.route[combo].append(t - self.cust[id][1])
#         del self.cust[id]

#     def getAverageTime(self, startStation: str, endStation: str) -> float:
#         return sum(self.route[(startStation, endStation)])/len(self.route[(startStation, endStation)])
        
# # Your UndergroundSystem object will be instantiated and called as such:
# # obj = UndergroundSystem()
# # obj.checkIn(id,stationName,t)
# # obj.checkOut(id,stationName,t)
# # param_3 = obj.getAverageTime(startStation,endStation)


