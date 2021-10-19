class Solution:
    def peopleIndexes(self, favoriteCompanies: 'List[List[str]]') -> 'List[int]':
        output = []
        for i in range(len(favoriteCompanies)):
            good = 1
            for j in list(range(i)) + list(range(i+1, len(favoriteCompanies))):
                if len (set(favoriteCompanies[i]) - set(favoriteCompanies[j])) == 0:
                    good = 0
                    break
            if good == 1:
                output.append(i)
        return output