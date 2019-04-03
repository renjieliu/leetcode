def shiftingLetters(S: str, shifts: 'List[int]'):
    map = [chr(_) for _ in range(97,123)]

    moves = 0
    temp = ""
    for i in range(len(shifts)-1, -1,-1): #from right the left to find how many positions each character will move
        moves+= shifts[i]
        original = map.index(S[i])


        temp =  map [ (moves + original) % 26] + temp

    return temp

print(shiftingLetters('abc',[3,5,9]))
print(shiftingLetters('ashfksahdfkhaoifdsuao',[300]))


