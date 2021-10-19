class Solution:
    def alertNames(self, keyName: 'List[str]', keyTime: 'List[str]') -> 'List[str]':
        hmp = {}
        for i in range(len(keyName)):
            if keyName[i] not in hmp:
                hmp[keyName[i]] = []
            hmp[keyName[i]].append(keyTime[i])
        output = []
        for k, v in hmp.items():
            if len(v) >= 3:
                arr = sorted(v)
                for i in range(2, len(arr)):
                    if arr[i][:2] == arr[i - 2][:2]:  # same hour
                        output.append(k)
                        break
                    elif int(arr[i][:2]) <= int(arr[i - 2][:2]) + 1 and int(arr[i][-2:]) <= int(arr[i - 2][-2:]):
                        output.append(k)
                        break
        return sorted(output)

