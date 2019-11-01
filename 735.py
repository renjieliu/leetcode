def asteroidCollision(asteroids: 'List[int]'):
    neg_left = []
    pos_right = []
    for i in asteroids[::-1]:
        crash = 0
        if i < 0:
            neg_left.append(i)

        elif i > 0:
            while neg_left != []:
                if abs(neg_left[-1]) < abs(i):
                    neg_left.pop()
                elif abs(neg_left[-1]) == abs(i):
                    neg_left.pop()
                    crash = 1
                    break
                elif abs(neg_left[-1]) > abs(i):
                    break

            if len(neg_left) == 0 and crash == 0:
                pos_right.append(i)

    return neg_left[::-1] + pos_right[::-1]

