import datetime
class Solution:     
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = date1.split('-')
        d2 = date2.split('-')
        from_date = datetime.date(int(d1[0]), int(d1[1]), int(d1[2])    )
        to_date = datetime.date(int(d2[0]), int(d2[1]), int(d2[2]))
        return abs((to_date - from_date).days)