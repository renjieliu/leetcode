def powerfulIntegers(x: 'int', y: 'int', bound: 'int'):
    output = []

    if x == y and x == 1 and bound >= 2:
        return [2]

    for i in range(0, bound):
        if x**i <=bound:
            for j in range(0, bound):
                t = x ** i + y ** j
                if t <= bound and t not in output:
                    output.append(t)

                if t > bound:
                    stop = 1
                    break
        else:
            break

    output.sort()

    return output

print(powerfulIntegers(3,5,25))
print(powerfulIntegers(2,3,10))
print(powerfulIntegers(1,1,0))
