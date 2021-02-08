class Solution:
    def generateAbbreviations(self, word: str) -> 'List[str]':
        def combo(output, N, curr, rest_arr):
            if len(curr) == N:
                output.append(curr)
                return 1
            else:
                i = 0
                while i < len(rest_arr):
                    t = curr + [rest_arr[i]]
                    combo(output, N, t, rest_arr[i + 1:])
                    i += 1

        if word == "": return [""]
        arr = [_ for _ in range(len(word))]
        pool = []
        for N in range(1, len(arr) + 1):  # pick from 1 to N
            i = 0
            while i < len(arr):
                curr = [arr[i]]
                combo(pool, N, curr, arr[i + 1:])
                i += 1
        output = [str(len(word))]
        for p in pool:  # to pick the one based on the order
            if p[0] != 0:
                curr = str(p[0])
            elif p[0] == 0:
                curr = word[0]
            i = 0 if p[0] != 0 else 1
            while i < len(p):
                c = p[i]
                if c - p[i - 1] > 1:
                    curr += str(c - p[i - 1] - 1)  # how many in between
                curr += word[c]
                i += 1

            if p[-1] != len(word) - 1:
                curr += str(len(word) - 1 - p[-1])  # for the number like 02, need to add the last letter back
            output.append(curr)

        return output

















