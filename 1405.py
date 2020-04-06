class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        output = ""
        A, B, C = ["a"] * a, ["b"] * b, ["c"] * c
        lst = sorted([A, B, C], key=lambda x: len(x), reverse=1)
        while lst[-1] == []: lst.pop()  # remove the empties
        while lst:
            for i in (0,
                      1):  # take 2 from the first one, then 1 from the next, and 2 from the first .. until the stk is empty or only one left
                if len(lst) == 1:
                    if len(lst[0]) > 1:
                        output += lst[0].pop()
                        output += lst[0].pop()
                    else:
                        output += lst[0].pop()
                    x = output[-1]
                    return output.replace(x * 4, x * 2).replace(x * 3,
                                                                x * 2)  # in case the last character repeated 3 times more

                else:
                    if output != "" and i == 0 and lst[i][0] == output[-1]:
                        continue
                    if (i == 0 and len(lst[i]) > 1):
                        output += lst[i].pop()
                        output += lst[i].pop()
                    else:
                        output += lst[i].pop()

                    if lst[i] == []:
                        lst = lst[:i] + lst[i + 1:]

            lst.sort(key=lambda x: len(x), reverse=1)  # bump the greatest to the top
        return output

