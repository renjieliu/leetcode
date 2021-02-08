class Solution:
    def reverseWords(self, s: 'List[str]') -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverse(s, l, r):  # reverse from l to r
            for i in range(l, l + (r - l) // 2 + 1):  # only need to iterate the first half, current right is (i-l)
                s[i], s[r - (i - l)] = s[r - (i - l)], s[i]
                # print(s[i],s[r-(i-l)], s )

        reverse(s, 0, len(s) - 1)
        curr = 0
        for i in range(len(s)):
            if s[i] == " ":
                reverse(s, curr, i - 1)
                curr = i + 1
        reverse(s, curr, len(s) - 1)  # reverse the last part
