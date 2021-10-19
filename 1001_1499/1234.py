def balancedString(s: str):
    def compare_dict(d1, d2):
        cnt = 0
        for k, v in d1.items():
            if k in d2 and d2[k] >= v:
                cnt += 1

        return 1 if cnt == len(d1.keys()) else 0

    balance = len(s) // 4
    dict = {}
    ref_dict = {}

    for i in s:
        if i not in dict:
            dict[i] = 0
        dict[i] += 1

    for k, v in dict.items():
        if v > balance:
            ref_dict[k] = v - balance

    if len(ref_dict.keys()) ==0 :
        return 0

    l, r = 0, 0
    output = float('inf')
    curr_dict = {}

    while r < len(s):
        if s[r] not in curr_dict:
            curr_dict[s[r]] = 0
        curr_dict[s[r]] += 1

        if compare_dict(ref_dict, curr_dict) == 1:  # OK
            curr = s[l:r + 1]
            output = min(output, len(curr))
            while l <= r:  # shrink
                if compare_dict(ref_dict, curr_dict) == 1:
                    output = min(output, len(curr))
                    curr_dict[curr[0]] -= 1
                    curr = curr[1:]
                    l += 1
                else:
                    break
        r += 1

    return output


print(balancedString("QWER"))  # 0
print(balancedString("QQWE"))  # 1
print(balancedString("QQQW"))  # 2
print(balancedString("QQQQ"))  # 3
print(balancedString("QQQQWWWWEEEE"))  # 6
print(balancedString("QQQQWWWWERRRRRRRRRRRRRRRRRRRRRRRRRRR"))  # 18
print(balancedString("WWEQERQWQWWRWWERQWEQ"))  # 4
print(balancedString("WQWRQQQW"))  # 3
print(balancedString("RQRERREWEEWWQWRRRWQQEQQQ"))  # 2
print(balancedString("QEQRWRRWWWRQQQWQQEQEQREWRQEQRQQRRQEW"))  # 6
