def minimumSwap(s1: str, s2: str):
    diff = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff.append(s1[i] + s2[i])

    if len(diff) == 0:
        return 0
    elif len(diff) % 2 == 1:
        return -1
    else:
        dict = {'xy': 0, 'yx': 0}
        # if xy and xy or yx and yx, then 1 else 2.
        for x in diff:
            dict[x] += 1

        xy_cnt = dict['xy']
        yx_cnt = dict['yx']

        xy_cnt_total = xy_cnt // 2 + (1 if xy_cnt % 2 == 1 else 0)
        yx_cnt_total = yx_cnt // 2 + (1 if yx_cnt % 2 == 1 else 0)

        return xy_cnt_total + yx_cnt_total


