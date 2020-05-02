class Solution:
    def kidsWithCandies(self, candies: 'List[int]', extraCandies: int) -> 'List[bool]':
        return map(lambda x: (x+extraCandies) >= max(candies), candies)