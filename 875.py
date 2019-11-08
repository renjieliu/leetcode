class Solution:
    def minEatingSpeed(piles: 'List[int]', H: int) -> int:
        if len(piles) == H:
            return max(piles)
        else:
            # use binary search to find the number, range 1 to max(piles). #if none fits, return the best one that fits the criteria.
            end = max(piles)
            start = 1
            output = end
            while start <= end:
                mid = (start + end) // 2
                shadow = piles.copy()
                hours = 0
                i = 0
                while i < len(shadow):
                    needed = shadow[i] % mid
                    hours += shadow[i] // mid + (
                        1 if needed != 0 else 0)  # need 1 more hour to finish the remaining of the pile.
                    i += 1

                if hours == H:
                    return mid

                elif hours > H:  # it does not fit
                    start = mid + 1

                elif hours < H:  # it fits, but it can be improved
                    output = min(output, mid)
                    end = mid - 1

            return output
