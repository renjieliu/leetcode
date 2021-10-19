class Solution:
    def shiftingLetters(self, s: str, shifts: 'List[int]') -> str:
        lkp = [chr(_) for _ in range(97, 123)] + [chr(_) for _ in range(97, 123)]
        arr = [shifts[-1]]
        for n in shifts[:-1][::-1]:  #accumulated sum from right to left
            arr.append(arr[-1]+n)
        arr = arr[::-1]
        output = ""
        for i in range(len(s)):
            pos = ord(s[i])-97 + (arr[i]%26)
            output += lkp[pos]
        return output



# previous approach
# def shiftingLetters(S: str, shifts: 'List[int]'):
#     map = [chr(_) for _ in range(97,123)]
#
#     moves = 0
#     temp = ""
#     for i in range(len(shifts)-1, -1,-1): #from right the left to find how many positions each character will move
#         moves+= shifts[i]
#         original = map.index(S[i])
#
#
#         temp =  map [ (moves + original) % 26] + temp
#
#     return temp
#
# print(shiftingLetters('abc',[3,5,9]))
# print(shiftingLetters('ashfksahdfkhaoifdsuao',[300]))
#
#
