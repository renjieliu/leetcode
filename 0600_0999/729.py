class MyCalendar:

    def __init__(self): #O( 1 | 1 )
        self.cal = []
        

    def book(self, start: int, end: int) -> bool: #O(N**2 | 1)
        for a, b in self.cal: #go through the calendar, and see if overlapped with currend start, end
            if a <= start < b or start <= a < end: # check if overlapping
                return False
        self.cal.append([start, end]) 
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)





# previous solution

# class MyCalendar:

#     def __init__(self):
#         self.stk = []


#     def book(self, start: int, end: int) -> bool:
#         for s, e in self.stk:
#             if start <= s < end or s <= start < e:
#                 return False
#         self.stk.append([start, end])
#         return True


# # Your MyCalendar object will be instantiated and called as such:
# # obj = MyCalendar()
# # param_1 = obj.book(start,end)




# previous approach
# class MyCalendar:
#
#     def __init__(self):
#         self.cal = []
#
#     def book(self, start: int, end: int) -> bool:
#         if len(self.cal) == 0:
#             self.cal.append([start, end - 1])
#             return True
#         else:
#             for j in self.cal:
#                 if j[0] <= start <= j[1] or j[0] <= end - 1 <= j[1] or (start <= j[0] and end - 1 >= j[1]):
#                     return False
#
#             self.cal.append([start, end - 1])
#             return True
#
# # Your MyCalendar object will be instantiated and called as such:
# # obj = MyCalendar()
# # param_1 = obj.book(start,end)