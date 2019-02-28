def lemonadeChange(bills: 'List[int]'):
    five = 0
    ten = 0
    if bills[0] != 5:
        return False
    else:
        for i in bills:
            if i == 5:
                five += 1
                continue
            if i == 10 and five > 0:
                five -= 1
                ten += 1
                continue
            if i == 10 and five <= 0:  # no change.
                return False
            if i == 20 and five > 0 and ten > 0:  # 20-5-10 for $20
                ten -= 1
                five -= 1
                continue
            if i == 20 and ten <= 0 and five >= 3:  # 20-15 for $20
                five -= 3
                continue
            if i == 20 and (five < 3 or ten <= 0):
                return False

    return True

print(lemonadeChange([5,5,5,10,20]))
print(lemonadeChange([5,5,10]))
print(lemonadeChange([10,10]))
print(lemonadeChange([10,10]))
print(lemonadeChange([5,5,5,10,5,5,10,20,20,20]))
print(lemonadeChange([5,5,5,5,10,5,10,10,10,20]))



