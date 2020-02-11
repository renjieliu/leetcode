class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = hour*30 #30 degrees per hour
        m = minutes * 6 #360/60, 6 degree per minutes.
        h += minutes*(360/12/60) #hour angle moving per minutes
        output = abs(h-m)
        output = min(abs(output), abs(360-output))
        return output