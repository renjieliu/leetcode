class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        loc = word.find(ch)
        return (word[:loc+1][::-1]+word[loc+1:]) if ch !=-1 else word



