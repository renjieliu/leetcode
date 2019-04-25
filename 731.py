class MyCalendarTwo:

    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:

        if len(self.cal) < 2:
            self.cal.append([start, end - 1])
            self.cal.sort()
            return True

        else:

            self.cal.append([start, end - 1])
            self.cal.sort()
            pos = self.cal.index([start, end - 1])
            scan = [start, end - 1]
            for i in range(pos):
                if start <= self.cal[i][1] <= end - 1:
                    scan.append(self.cal[i][1])

            for i in range(pos + 1, len(self.cal)):
                if self.cal[i][0] <= end - 1:
                    scan.append(self.cal[i][0])
                if self.cal[i][1] <= end - 1:
                    scan.append(self.cal[i][1])

            scan = sorted(list(set(scan)))

            for s in scan:
                cnt = 0
                for j in self.cal:
                    if j[0] <= s <= j[1]:
                        cnt += 1

                    if cnt >= 3:
                        del self.cal[pos]
                        return False

            return True

# Your MyCalendarTwo object will be instantiated and called as such:
obj = MyCalendarTwo()
print(obj.book(26,35))
print(obj.book(26,32))
print(obj.book(25,32))


