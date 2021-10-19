def dayOfTheWeek(day: int, month: int, year: int):
    # Zeller’s Congruence
    days = [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    m=month
    if month in [1,2]:
        m+=12
        year-=1

    d = day
    y = year%100
    c = (year // 100)
    formula = y+int(y/4)+ int(c/4) - 2*c + int( 26*(m+1)/10  ) +d-1

    return days[formula %7]



print(dayOfTheWeek(8,9, 2019))
print(dayOfTheWeek(7,9, 2019))
print(dayOfTheWeek(6,9, 2019))
print(dayOfTheWeek(5,9, 2019))
print(dayOfTheWeek(29,2,2016)) #Monday




