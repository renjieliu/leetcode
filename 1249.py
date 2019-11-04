class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        yes = []
        pending_left = []
        for i in range(len(s)):
            j = s[i]
            if j == "(":
                pending_left.append(i)
            elif j == ")":
                if pending_left != []:
                    yes.append(pending_left.pop())
                    yes.append(i)
            else:
                yes.append(i)

        yes.sort()
        output = ""

        for i in yes:
            output += s[i]
        return output


