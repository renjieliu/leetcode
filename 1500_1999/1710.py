class Solution:
    def maximumUnits(self, boxTypes: 'List[List[int]]', truckSize: int) -> int: # O( NlogN | 1 )
        boxTypes.sort(key = lambda x: -x[1]) # sort the boxes with unitsPerBox in reverse order
        output = 0 
        for cnt , units in boxTypes: # keep taking the boxes, until the truck is full.
            if cnt > truckSize:
                return output + truckSize*units
            else:
                output += cnt*units
                truckSize -= cnt
        return output
    


# previous solution

# class Solution:
#     def maximumUnits(self, boxTypes: 'List[List[int]]', truckSize: int) -> int:
#         boxTypes.sort(key = lambda x :x[1], reverse = True)
#         total = 0
#         rem = truckSize
#         while boxTypes and rem > 0:
#             quantity, units  = boxTypes.pop(0)
#             if quantity <= rem: #all the current units can be placed
#                 total += quantity * units
#                 rem -= quantity
#             else:
#                 total += units * rem
#                 rem -= rem
#                 return total
#         return total


# previous approach
# class Solution:
#     def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
#         boxTypes.sort(key = lambda x:x[1], reverse = True)
#         output = 0
#         rem = truckSize #remaining space on the truck
#         for b in boxTypes:
#             if rem >= b[0]: #take all the current boxes
#                 output += b[0] *b[1]
#                 rem -= b[0]
#             else: #cannot take all the boxes
#                 output += rem*b[1]
#                 return output
#             if rem == 0:
#                 return output
#         return output