def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    Input: numbers = [2,7,8,9,11,15,19,22], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
     -->> You may assume that each input would have exactly one solution and you may not use the same element twice.
    """

    map = {}
    for i in range(0, len(numbers)):
        if numbers[i] in map:
            return [map[numbers[i]]+1, i+1]
        else:
            map[target-numbers[i]] = i

    return map

print(twoSum([2,7,8,9,11,15,19,22], 9 ))

