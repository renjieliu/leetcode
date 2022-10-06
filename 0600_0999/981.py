class TimeMap:

    def __init__(self):
        self.hmp = defaultdict(lambda: [])
        

    def set(self, key: str, value: str, timestamp: int) -> None: # O( 1 | N )
        self.hmp[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str: # O( logN | 1)
        if key not in self.hmp:
            return ""
        else: 
            def binFind(arr, v): # binary find the max location with timestamp <= v
                if v > arr[-1][0]:
                    return len(arr)-1
                elif v < arr[0][0]:
                    return -1
                s = 0
                e = len(arr)-1
                while s <= e :
                    mid = s-(s-e)//2
                    if arr[mid][0] == v :
                        return mid
                    elif arr[mid][0] > v:
                        e = mid - 1 
                    else:
                        output = mid
                        s = mid + 1
                return output
            
            T = binFind(self.hmp[key], timestamp)
            if T == -1:
                return ""
            else:
                return self.hmp[key][T][1]
            
                    

        
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)




# previous solution

# class TimeMap:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.hash = {}

#     def set(self, key: str, value: str, timestamp: int) -> None:

#         if key not in self.hash:
#             self.hash[key] = {}
#             self.hash[key][-2] = timestamp  # used to store the lowest value

#         self.hash[key][timestamp] = value
#         self.hash[key][-1] = timestamp  # used to store the latest value

#     def get(self, key: str, timestamp: int) -> str:

#         if key not in self.hash:
#             return ""

#         latest = self.hash[key][-1]
#         lowest = self.hash[key][-2]

#         if timestamp >= latest:
#             return self.hash[key][latest]

#         elif timestamp == lowest:
#             return self.hash[key][lowest]

#         elif timestamp < lowest:
#             return ""


#         else:
#             for i in range(timestamp, -1, -1):
#                 if i in self.hash[key]:
#                     return self.hash[key][i]

#         # latest = -float('inf')
#         # for i in self.hash[key].keys():
#         #     if i<=timestamp:
#         #         latest = max(latest, i)

# # Your TimeMap object will be instantiated and called as such:
# # obj = TimeMap()
# # obj.set(key,value,timestamp)
# # param_2 = obj.get(key,timestamp)





