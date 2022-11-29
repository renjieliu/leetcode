import random

class RandomizedSet:

    def __init__(self):
        self.loc = {} # to record the location of the values
        self.arr = []
        

    def insert(self, val: int) -> bool: # O( 1 | 1 )
        if val not in self.loc: # add the new val to the end of the arr
            self.arr.append(val)
            self.loc[val] = len(self.arr) - 1 
            return True 
        return False

    def remove(self, val: int) -> bool: # O( 1 | 1 )
        if val not in self.loc:
            return False
        val_loc = self.loc[val] # the new location of current last val
        
        self.arr[-1], self.arr[val_loc] = self.arr[val_loc], self.arr[-1] # swap val with the last value
        self.loc[self.arr[val_loc]] = val_loc # record the new location for the previous last value
        del self.loc[val]
        self.arr.pop()
        return True 

    def getRandom(self) -> int: # O( 1 | 1 )
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()





# previous solution

# import random

# class RandomizedSet:

#     def __init__(self):
#         self.loc = {} # to record the location of the values
#         self.arr = []
        

#     def insert(self, val: int) -> bool: # O( 1 | 1 )
#         if val not in self.loc: # add the new val to the end of the arr
#             self.arr.append(val)
#             self.loc[val] = len(self.arr) - 1 
#             return True 
#         return False

#     def remove(self, val: int) -> bool: # O( 1 | 1 )
#         if val not in self.loc:
#             return False
#         val_loc = self.loc[val] # the new location of current last val
        
#         self.arr[-1], self.arr[val_loc] = self.arr[val_loc], self.arr[-1] # swap val with the last value
#         self.loc[self.arr[val_loc]] = val_loc # record the new location for the previous last value
#         del self.loc[val]
#         self.arr.pop()
#         return True 

#     def getRandom(self) -> int: # O( 1 | 1 )
#         return random.choice(self.arr)
        


# # Your RandomizedSet object will be instantiated and called as such:
# # obj = RandomizedSet()
# # param_1 = obj.insert(val)
# # param_2 = obj.remove(val)
# # param_3 = obj.getRandom()





# previous solution

# import random

# class RandomizedSet:

#     def __init__(self):
#         self.lkp = set()
        

#     def insert(self, val: int) -> bool: # O( 1 | 1 )
#         if val not in self.lkp:
#             self.lkp.add(val)
#             return True
#         return False

#     def remove(self, val: int) -> bool: # O( 1 | 1)
#         if val not in self.lkp:
#             return False
#         self.lkp.remove(val)
#         return True

#     def getRandom(self) -> int: # O(N)
#         return list(self.lkp)[random.randint(0, len(self.lkp)-1)]
        


# # Your RandomizedSet object will be instantiated and called as such:
# # obj = RandomizedSet()
# # param_1 = obj.insert(val)
# # param_2 = obj.remove(val)
# # param_3 = obj.getRandom()



# previous solution

# class RandomizedSet:

#     def __init__(self):
#         self.hmp_loc = {}
#         self.arr = []
        

#     def insert(self, val: int) -> bool:
#         if val in self.hmp_loc:
#             return False
#         self.hmp_loc[val] = len(self.arr)
#         self.arr.append(val)
#         return True
        
        

#     def remove(self, val: int) -> bool:
#         if val not in self.hmp_loc:
#             return False
#         else:
#             loc = self.hmp_loc[val]
#             self.arr[loc], self.arr[-1] = self.arr[-1], self.arr[loc] #swap the value loc with the last value of arr
#             self.hmp_loc[self.arr[loc]] = loc #update the last value location
#             del self.hmp_loc[val] #del the previous loc from the hmp
#             self.arr.pop()       # pop the last value
#             return True
        

#     def getRandom(self) -> int:
#         return random.choice(self.arr)
        


# # Your RandomizedSet object will be instantiated and called as such:
# # obj = RandomizedSet()
# # param_1 = obj.insert(val)
# # param_2 = obj.remove(val)
# # param_3 = obj.getRandom()



# previous approach
# class RandomizedSet:

#     def __init__(self):
#         self.arr = []
#         self.hmp = {} #to store the location of the value
        

#     def insert(self, val: int) -> bool:
#         if val in self.hmp:
#             return False
#         else:
#             self.hmp[val] = len(self.arr)
#             self.arr.append(val)
#             return True
        

#     def remove(self, val: int) -> bool:
#         if val not in self.hmp:
#             return False
#         else:
#             last = self.arr[-1] #swap the val and last item in the list, and pop the last item
#             loc = self.hmp[val]
#             self.arr[loc] = last 
#             self.arr[-1] = val
#             self.hmp[last] = loc #update the location of the previously last item
#             del self.hmp[val]
#             self.arr.pop()
#             return True
            
            
        

#     def getRandom(self) -> int:
#         return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()



# previous approach
# import random;


# class RandomizedSet:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.hmp = {}

#     def insert(self, val: int) -> bool:
#         """
#         Inserts a value to the set. Returns true if the set did not already contain the specified element.
#         """
#         if val not in self.hmp:
#             self.hmp[val] = None
#             return True
#         return False

#     def remove(self, val: int) -> bool:
#         """
#         Removes a value from the set. Returns true if the set contained the specified element.
#         """
#         if val in self.hmp:
#             del self.hmp[val]
#             return True
#         return False

#     def getRandom(self) -> int:
#         """
#         Get a random element from the set.
#         """
#         k = list(self.hmp.keys())
#         return k[random.randint(0, len(k) - 1)]

# # Your RandomizedSet object will be instantiated and called as such:
# # obj = RandomizedSet()
# # param_1 = obj.insert(val)
# # param_2 = obj.remove(val)
# # param_3 = obj.getRandom()