class HitCounter:

    def __init__(self):
        self.arr = []
        

    def hit(self, timestamp: int) -> None:
        self.arr.append(timestamp)

    def getHits(self, timestamp: int) -> int: # O( logN | 1 )
        def binFindStart(arr, v): #find the first loc where arr[loc] >= v
            s = 0 
            e = len(arr)-1
            output = None
            while s<=e:
                mid = s - (s-e)//2
                if arr[mid] >= v:
                    e = mid - 1 
                    output = mid
                else: 
                    s = mid + 1 
            return output

        def binFindEnd(arr, v): # find the last loc where arr[loc] <= v
            s = 0
            e = len(arr)-1
            output = None
            while s<=e:
                mid = s - (s-e)//2
                if arr[mid] <= v:
                    s = mid + 1
                    output = mid
                else:
                    e = mid - 1
            return output
        
        S = binFindStart(self.arr, timestamp-300+1) #the start value is current timestamp-300+1
        E = binFindEnd(self.arr, timestamp) # the end value is current timestamp
        return 0 if S == None or E == None else E-S+1
        
        
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

# previous solution 

# class HitCounter:

#     def __init__(self):
#         self.arr = []
        

#     def hit(self, timestamp: int) -> None:
#         self.arr.append(timestamp)

#     def getHits(self, timestamp: int) -> int:
#         def binFindStart(arr, v): #find the first loc where arr[loc] >= v
#             s = 0 
#             e = len(arr)-1
#             output = None
#             while s<=e:
#                 mid = s - (s-e)//2
#                 if arr[mid] >= v:
#                     e = mid - 1 
#                     output = mid
#                 else: 
#                     s = mid + 1 
#             return s

#         def binFindEnd(arr, v): # find the last loc where arr[loc] <= v
#             s = 0
#             e = len(arr)-1
#             output = None
#             while s<=e:
#                 mid = s - (s-e)//2
#                 if arr[mid] <= v:
#                     s = mid + 1
#                     output = mid
#                 else:
#                     e = mid - 1
#             return s
        
#         S = binFindStart(self.arr, timestamp-300+1) #the start value is current timestamp-300+1
#         E = binFindEnd(self.arr, timestamp) # the end value is current timestamp
#         return 0 if S == E == None else E-S
        
        
        


# # Your HitCounter object will be instantiated and called as such:
# # obj = HitCounter()
# # obj.hit(timestamp)
# # param_2 = obj.getHits(timestamp)


