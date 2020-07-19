class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        output = numBottles
        while numBottles // numExchange >= 1:
            output += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange  # can change + the fullbottles remain
        return output
