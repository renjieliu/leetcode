class MyCalendar:

    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:
        if len(self.cal) == 0:
            self.cal.append([start, end - 1])
            return True
        else:
            for j in self.cal:
                if j[0] <= start <= j[1] or j[0] <= end - 1 <= j[1] or (start <= j[0] and end - 1 >= j[1]):
                    return False

            self.cal.append([start, end - 1])
            return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)