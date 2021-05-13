class Solution:
    def ambiguousCoordinates(self, s: str) -> 'List[str]':
        def cross(res, A, B):
            for a in A:
                for b in B:
                    res.append(f"({a}, {b})")

        def helper(s):
            output = []
            if len(s) == 1:
                output = [s]
            elif s[0] == "0":
                if s[-1] != "0":
                    output.append(s[0] + "." + s[1:])
            elif s[0] != "0":
                output.append(s)
                if s[-1] != "0":  # strings like 142433143
                    for i in range(1, len(s)):
                        output.append(s[:i] + "." + s[i:])
            # print(s, output)
            return output

        s = s.replace("(", "").replace(")", "")
        res = []
        for i in range(1, len(s)):
            A = helper(s[:i])
            B = helper(s[i:])
            cross(res, A, B)
        return res

















