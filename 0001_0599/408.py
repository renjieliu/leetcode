class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        num = [str(_) for _ in range(10)]
        n = ""
        for p in range(len(abbr)):  # to see if current matches
            if n == "" and abbr[p] == "0":  # for the numbers like '01', '02'
                return False
            elif abbr[p] in num:
                n += abbr[p]
            else:
                if n == "":  # no number, compare both
                    if abbr[p] != word[0]:
                        return False
                    else:
                        word = word[1:]
                else:  # number, skip and compare
                    if int(n) >= len(word):
                        return False
                    word = word[int(n):]
                    if abbr[p] != word[0]:
                        return False
                    else:
                        word = word[1:]
                    n = ""
        n = 0 if n == "" else int(n)
        if len(word) == n:
            return True
        else:
            return False



