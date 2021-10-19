class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        cnt = 0
        vowel = 'aeiou'
        output = 0
        for right in range(len(s)):
            if right-left + 1 == k+1:
                if s[left] in vowel:
                    cnt -= 1
                left+=1
            if s[right] in vowel:
                cnt +=1

            output = max(output, cnt)
        return output