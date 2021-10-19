class Solution:
    def calculate(self, s: str) -> int:
        def calc(txt):
            stk = []
            curr = ""
            operator = ""
            for t in txt:
                if t not in ['*', '/']:  # it's a number
                    curr += t
                else:
                    if len(stk) < 2:
                        stk.append(int(curr))
                        if len(stk) == 2:
                            res = int(stk[0] / stk[1]) if operator == '/' else (stk[0] * stk[1])
                            stk = [res]
                    operator = t
                    curr = ""

            if curr == "":
                return stk[0]
            else:
                curr = int(curr)
                # print(curr,operator)
                return int(stk[0] / curr) if operator == '/' else (stk[0] * curr)

        s = s.replace(' ', '').replace('-', '+-')
        arr = s.split('+')  # each part can be added
        # print(arr)
        i = 0
        while i < len(arr):
            if '*' in arr[i] or '/' in arr[i]:
                arr[i] = calc(arr[i])
            else:
                arr[i] = int(arr[i])
            i += 1
        # print(arr)
        return sum(arr)


