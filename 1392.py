class Solution:
    def longestPrefix(self, s: str) -> str:
        pre = list(s[:-1])
        suf = list(s[1:])
        while pre and suf and pre!=suf:
            pre.pop()
            suf.pop(0)
            while pre and suf and pre[0] != suf[0]:
                pre.pop()
                suf.pop(0)
        return "".join(pre)
