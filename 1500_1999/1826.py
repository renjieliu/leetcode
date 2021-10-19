class Solution:
    def badSensor(self, sensor1: 'List[int]', sensor2: 'List[int]') -> int:
        for i in range(len(sensor1)-1): #no need to compare the last digit. if last one is diff, then it will be -1
            if sensor1[i] != sensor2[i]:
                if sensor1[i:-1] == sensor2[i+1:]: # sensor 1 shifted 1 position, should match the rest of 2
                    return 1
                elif sensor2[i:-1] == sensor1[i+1:]: # sensor 2 shifted 1 position, should match the rest of 1
                    return 2
                else:
                    return -1
        return -1
