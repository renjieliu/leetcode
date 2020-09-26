class Solution:
    def findPoisonedDuration(self, timeSeries: 'List[int]', duration: int) -> int:
        if timeSeries == []:
            return 0
        else:
            output = duration
            wake = timeSeries[0] + duration - 1  # time when it wakes up
            for t in timeSeries[1:]:
                if t > wake:  # if the attack is after it wakes up
                    wake = t + duration - 1
                    output += duration
                else:  # before it wakes up
                    prev_wake = wake
                    wake = max(wake, t + duration - 1)  # if the attack will cause more damage
                    output += (wake - prev_wake)  # add the addtional damage

            return output