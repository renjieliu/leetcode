def findRestaurant(list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    temp = {}
    output  = []
    for i in range(0, len(list1 )):
        if list1[i] in list2:
            temp[list1[i]] = i + list2.index(list1[i])

    min = len(list2) + len(list1)

    for v in temp.values():
        if v < min:
            min = v


    for k, v in temp.items():
        if v==min:
            output.append(k)

    return  output

print(findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
print(findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"]))
