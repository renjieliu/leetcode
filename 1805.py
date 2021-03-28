class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        arr = [chr(_) for _ in range(97, 123)]
        for a in arr: #replace all the letter as space
            word = word.replace(a, " ")
        res=set()
        for w in word.split(" "): #split by space, and check how many distinct numbers
            if w and w != " ":
                res.add(int(w))
        return len(res)

