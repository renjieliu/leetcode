def isNStraightHand(hand: 'List[int]', W: int):
    if W == 1:
        return True

    elif len(hand)% W !=0 :
        return False

    cnt_total = 0
    hand.sort()
    count = len(hand)
    curr = 0
    while len(hand)>0:
        curr += 1
        i = hand[0]
        cnt = 1
        for j in range(1, W):
            if i+j in hand:
                hand.remove(i+j)
                cnt+=1
            else:
                return False
        #print (hand)
        hand.remove(i)

        #count = len(hand)

    #print(hand)
    return False if len(hand) !=0 else True


print(isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
print(isNStraightHand([1, 2, 3, 4, 5], 4))
print(isNStraightHand([2, 2, 3], 1))
print(isNStraightHand([2, 2], 1))
print(isNStraightHand([1], 1))
print(isNStraightHand([2, 1], 2))
print(isNStraightHand([5, 1], 2))
print(isNStraightHand([1,2,3,4,5,6], 2))




