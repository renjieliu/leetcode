class Solution:
    def findSmallestRegion(self, regions: 'List[List[str]]', region1: str, region2: str) -> str:
        def findHierar(looking, place_list, hierar):  # find the next hierarchy
            pos = 0
            found = 0
            for i in range(len(
                    place_list)):  # this is to find the current looking place in the place list and append the first item to the hier
                r = place_list[i]
                for _ in r:
                    if _ == looking:
                        hierar.append(r[0])
                        looking = r[0]  # current parent will be the next looking
                        found = 1
                        pos = i
                        break
            if found == 0:
                return 0
            else:
                if findHierar(looking, place_list[:pos] + place_list[pos + 1:], hierar) == 0:
                    return 0
                else:
                    return 1

        A, B = [region1], [region2]  # initialize the hier with current region
        findHierar(region1, regions, A)
        findHierar(region2, regions, B)
        # print(A,B)

        for i in range(len(A)):  # bottom up
            if A[i] in B:
                return A[i]



