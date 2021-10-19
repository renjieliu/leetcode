def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    map = {}
    output = []
    for i in nums1:
        map[i] = "a"

    for j in nums2:
        if map.get(j, "None")!="None":
            map[j] = "b"

    for k, v in map.items():
        if v == "b":
            output.append(k)

    return output

print(intersection([1, 2, 2, 1], [2, 2,2,2,2,1]))


