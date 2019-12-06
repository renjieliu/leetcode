class Solution:
    def minAvailableDuration(self, slots1: 'List[List[int]]', slots2: 'List[List[int]]', duration: int):
        slots1.sort()
        slots2.sort()
        i = j = 0
        while i < len(slots1):
            while j < len(slots2):  # find overlapping
                if slots1[i][0] > slots2[j][1]:  # to increase j
                    j += 1
                elif slots2[j][0] > slots1[i][1]:  # to increase i
                    break
                elif slots1[i][0] <= slots2[j][0] <= slots1[i][1] and slots1[i][0] <= slots2[j][1] <= slots1[i][
                    1]:  # s2 within s1
                    if slots2[j][1] - slots2[j][0] >= duration:
                        return [slots2[j][0], slots2[j][0] + duration]
                    else:
                        break
                elif slots2[j][0] <= slots1[i][0] <= slots2[j][1] and slots2[j][0] <= slots1[i][1] <= slots2[j][
                    1]:  # s1 within s2
                    if slots1[i][1] - slots1[i][0] >= duration:
                        return [slots1[i][0], slots1[i][0] + duration]
                    else:
                        break
                elif slots1[i][0] <= slots2[j][0] <= slots1[i][1]:  # partial overlapping
                    if slots1[i][1] - slots2[j][0] >= duration:
                        return [slots2[j][0], slots2[j][0] + duration]
                    else:
                        break
                elif slots2[j][0] <= slots1[i][0] <= slots2[j][1]:  # partial overlapping
                    if slots2[j][1] - slots1[i][0] >= duration:
                        return [slots1[i][0], slots1[i][0] + duration]
                    else:
                        break

            i += 1

        return []


