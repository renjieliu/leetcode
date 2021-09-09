class Solution:
    def numberOfWeakCharacters(self, properties: 'List[List[int]]') -> int:
        attack_group = {}
        max_attack_d = {}  # max defense with current attach
        for a, d in properties:
            if a not in attack_group:
                attack_group[a] = []
                max_attack_d[a] = -float('inf')
            attack_group[a].append(d)
            max_attack_d[a] = max(max_attack_d[a], d)

        lst = sorted(attack_group.keys())
        nxtMax = [max_attack_d[lst[-1]]]  # to record the max defensive after the current attack_group, initialize with the last element

        for i in range(len(lst) - 2, -1, -1):
            nxtMax.append(max(nxtMax[-1], max_attack_d[lst[i + 1]]))
        nxtMax = nxtMax[::-1]
        cnt = 0
        for i in range(len(lst) - 1):  # no need to check the last group
            for defense in attack_group[
                lst[i]]:  # for current attack_group, check if the max on the right is > than current
                # if nxtMax[i] > defense:
                #     print(attack_group[lst[i]], defense)
                cnt += 1 if nxtMax[i] > defense else 0
        return cnt



