class Solution:
    def sortByBits(self, arr: 'List[int]') -> 'List[int]':
        arr.sort()
        arr.sort(key = lambda x: sum(int(_) for _ in list(str(bin(x)).replace('0b','')))) #bin every number, turn to string and and sum
        return arr