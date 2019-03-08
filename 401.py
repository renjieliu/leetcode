def combo(n, k):
    if len(n) == k:
        return [n]

    else:
        output = []
        for i in range(len(n)):
            rest = n[:i] + n[i+1:]
            for x in combo(rest, k):
                output.append(x)

    return list(set(output))


def readBinaryWatch(num: 'int'):
    if num == 0:
        return ['0:00']
    else:
        map = {} # key: hour <=4 , value : minutes < =6
        for i in range(0, num+1):
            if i<=4 and num-i <= 6:
                map[i] = num - i

    output = []

    for k,v in map.items():
        hours = []
        minutes = []
        if k ==0:
            hours.append(0)
        if v ==0:
            minutes.append(0)

        for h in combo('0123',k): #this is to calculate the hours
            hour = 0
            for t in h:
                hour += 2**int(t)

            if hour<=11:
                hours.append(hour)

        for m in combo('012345', v): # this is to calculate the minutes
            minute = 0
            for t in m:
                minute += 2**int(t)

            if minute<=59:
                minutes.append(minute)

        #now to combine the hours and minutes and add to the final


        for h in hours :
            for m in minutes:
                f_minute = ''
                if m == 0:
                    f_minute = '00'
                elif m<10:
                    f_minute = '0'+ str(m)
                else:
                    f_minute = str(m)

                output.append(str(h)+':'+f_minute)

    return list(set(output))


print(readBinaryWatch(4))
