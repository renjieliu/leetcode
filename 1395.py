class Solution:
    def numTeams(self, rating: 'List[int]') -> int:
        cnt = 0
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                if rating[j] > rating[i]:
                    for k in range(j + 1, len(rating)):
                        if rating[k] > rating[j]:
                            cnt += 1

        rating = rating[::-1].copy()
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                if rating[j] > rating[i]:
                    for k in range(j + 1, len(rating)):
                        if rating[k] > rating[j]:
                            cnt += 1
        return cnt