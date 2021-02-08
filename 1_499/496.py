def nextGreaterElement(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    x1 = nums1
    x2 = nums2
    output = list()
    for i in range(0, len(x1)):
        found = -1
        index = x2.index(x1[i])
        for j in range(index, len(x2)):
            if x2[j] > x1[i]:
                found = x2[j]
                break

        output.append(found)

    return output

print(nextGreaterElement([2,4], [1,2,3,4]))
