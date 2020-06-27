class Solution:
    def average(self, salary: 'List[int]') -> float:
        a = list(filter(lambda x : x != max(salary) and x!=min(salary),salary))
        return sum(a)/len(a)