class Solution:
    def ambiguousCoordinates(self, s: str) -> 'List[str]':
        def cross(res, A, B):  # cross join arr A and arr B
            for a in A:
                for b in B:
                    res.append(f"({a}, {b})")

        def helper(s):  # move the dot from beginning to end, and check if it can make a valid number
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
        for i in range(1, len(s)):  # split the string into 2 parts, and get valid numbers from each part
            A = helper(s[:i])
            B = helper(s[i:])
            cross(res, A, B)  # cross join each part to get all the possibilities
        return res

















