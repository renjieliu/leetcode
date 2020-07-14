class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h_angle = 30 * hour + 0.5 * minutes #30 degree per hour, and 0.5 degree per minutes
        m_angle = 6 * minutes #6 degree per minute
        return abs(m_angle - h_angle) if abs(m_angle - h_angle) <= 180 else 360 - abs(m_angle - h_angle)

# previous approach
# class Solution:
#     def angleClock(self, hour: int, minutes: int) -> float:
#         h = hour*30 #30 degrees per hour
#         m = minutes * 6 #360/60, 6 degree per minutes.
#         h += minutes*(360/12/60) #hour angle moving per minutes
#         output = abs(h-m)
#         output = min(abs(output), abs(360-output))
#         return output