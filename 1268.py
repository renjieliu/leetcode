class Solution:
    def suggestedProducts(self, products: 'List[str]', searchWord: str):
        candidates = sorted(products)
        output = []
        i = 0
        while i < len(searchWord):  # prefix
            prefix = searchWord[:i + 1]
            output.append([])
            j = 0  # the index within candidates
            while j < len(candidates):
                if candidates[j][:i + 1] == prefix:  # find a match of the prefix, put the next items to the temp arr
                    if len(candidates[j:]) >= 3:
                        tempArr = candidates[j:j + 3]
                    else:
                        tempArr = candidates[j:]
                    k = 0  # go thru the array check if all matched the prefix
                    invalid = 0
                    while k < len(tempArr):
                        if tempArr[k][:i + 1] != prefix:
                            invalid = 1
                            tempArr = tempArr[:k]
                            break
                        k += 1
                    output[-1] = tempArr
                    candidates = candidates[j:]
                    if invalid == 1:
                        candidates = candidates[:k]
                    break
                j += 1
            i += 1

        return output