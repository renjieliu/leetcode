class Solution:
    def carPooling(self, trips: 'List[List[int]]', capacity: int) -> bool:
        unload = {}
        for i in trips:  # for eachs stop, record how many people to be unloaded
            if i[2] not in unload:
                unload[i[2]] = 0
            unload[i[2]] += i[0]
        trips.sort(key=lambda x: x[1])

        curr = trips[0][0]
        kick = {trips[0][2]}

        if curr > capacity:
            return False
        else:
            for num, on, off in trips[1:]:
                temp = set()
                for k in kick:
                    if k <= on:  # these people need to get off
                        curr -= unload[k]
                    else:  # these people stay put
                        temp.add(k)
                kick = temp.copy()
                curr += num  # pickup current stop

                if curr > capacity:
                    return False

                if off not in kick:
                    kick.add(off)

        return True
