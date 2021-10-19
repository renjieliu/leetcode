def minWindow(s: str, t: str):
    def c_dict(t):
        dict = {}
        for i in t:
            if i not in dict:
                dict[i] = 0
            dict[i] += 1
        return dict

    def compare_dict(d1, d2):
        cnt = 0
        for k, v in d1.items():
            if k in d2 and v <= d2[k]:
                cnt += 1

        return 1 if cnt == len(d1.keys()) else 0

    ref = c_dict(t)
    l = 0
    r = 0
    curr = ""
    output = ""
    curr_dict = {}
    minn = float('inf')
    while r <= len(s) - 1:  # expand
        curr += s[r]
        if s[r] not in curr_dict:
            curr_dict[s[r]] = 0
        curr_dict[s[r]] += 1
        if compare_dict(ref, curr_dict) == 1:
            if len(curr) < minn:
                minn = len(curr)
                output = curr
            while l <= r:
                if compare_dict(ref, curr_dict) == 1:
                    if len(curr) < minn:
                        minn = len(curr)
                        output = curr
                    l += 1
                    curr_dict[curr[0]] -= 1
                    curr = curr[1:]
                else:
                    break

        r += 1

    return output


print(minWindow("ADOBECODEBANC", "ABC"))
