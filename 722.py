class Solution:
    def removeComments(self, source: 'List[str]') -> 'List[str]':
        b_comment = 0  # the block comment
        curr = ""
        output = []
        for s in source:
            i = 0
            while i < len(s):
                c = s[i]
                if b_comment == 0:  # not in the block comment
                    curr += c
                    if len(curr) >= 2 and curr[-2:] == "//":  # no need to go thru the rest of the curr line
                        curr = curr[:-2]  # take out the //
                        break
                    elif len(curr) >= 2 and curr[-2:] == "/*":
                        b_comment = 1
                        curr = curr[:-2]
                elif b_comment == 1 and len(s[i:]) > 1 and s[i:i + 2] == "*/":  # it's in block comment, and find */
                    b_comment = 0
                    i += 1  # bypass the * , and it will pass the / in the in the while loop
                i += 1

            if b_comment == 0 and curr != "":  # as long as it's not in the blocked comment, it should be printed out
                output.append(curr)
                curr = ""

        return output