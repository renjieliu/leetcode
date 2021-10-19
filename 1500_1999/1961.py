class Solution:
    def isPrefixString(self, s: str, words: 'List[str]') -> bool:
        left = 0
        for w in words:
            if w == s[left:left+len(w)]:
                left += len(w)
                if s[left:] == "":
                    return True
            else:
                return False
