def dayOfYear(date: str):
    def isLeap(y):
        if (y%4 == 0 and y%100 !=0) or (y%400 ==0):
            return 1
        else:
            return 0

    y = int(date.split("-")[0])
    m = int(date.split("-")[1])
    d = int(date.split("-")[2])

    md = [31, 28, 31, 30, 31,30,31,31,30,31,30,31]

    output = sum(md[:m-1]) + d + (1 if isLeap(y) ==1 and m>2  else 0)

    return output


print(dayOfYear("2019-01-09"))
print(dayOfYear("2019-02-10"))
print(dayOfYear("2003-03-01"))
print(dayOfYear("2004-03-01"))
print(dayOfYear("2016-02-29"))