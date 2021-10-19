class Solution:
    def uniqueMorseRepresentations(self, words: 'List[str]') -> int:
        arr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        lkp = set()
        for w in words:
            curr = ""
            for c in w:
                curr += arr[ord(c)-97]
            lkp.add(curr)
        return len(lkp)


# previous approach
# class Solution(object):
#
#     def convert_morse(self, s):
#         dict = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
#                 ".--.",
#                 "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
#         output = ""
#         for i in range(0, len(s)):
#             output += dict[ord(s[i]) - 97]
#
#         return output
#
#     def uniqueMorseRepresentations(self, words):
#         """
#         :type words: List[str]
#         :rtype: int
#         """
#         dict = {}
#         cnt = 0
#         for i in range(0, len(words)):
#             if self.convert_morse(str(words[i])) not in dict:
#                 dict[self.convert_morse(str(words[i]))] = 1
#                 cnt += 1
#         return cnt
#
