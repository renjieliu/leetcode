class Solution:
    def maximumUnits(self, boxTypes: 'List[List[int]]', truckSize: int) -> int:
        boxTypes.sort(key = lambda x:x[1], reverse = True)
        output = 0
        rem = truckSize #remaining space on the truck
        for b in boxTypes:
            if rem >= b[0]: #take all the current boxes
                output += b[0] *b[1]
                rem -= b[0]
            else: #cannot take all the boxes
                output += rem*b[1]
                return output
            if rem == 0:
                return output
        return output