class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a = ''.join([str(ord(c) - 97) for c in firstWord])
        b = ''.join([str(ord(c) - 97) for c in secondWord])
        c = ''.join([str(ord(c) - 97) for c in targetWord])
        return int(a) + int(b) == int(c)

