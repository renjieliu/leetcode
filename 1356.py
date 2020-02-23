class Solution:
    def sortByBits(self, arr: 'List[int]') -> 'List[int]':
        arr.sort(key = lambda x: [str(bin(x)).count('1'),x])  #bin every number, turn to string and count 1
        return arr