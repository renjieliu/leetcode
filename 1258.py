class Solution:
    def generateSentences(self, synonyms: 'List[List[str]]', text: str) -> 'List[str]':
        def matched(A, B):  # to check if any word of B, exists in A
            for b in B:
                if b in A:
                    return 1
            return 0

        def cartesian(A, B):
            output = []
            for i in A:
                for j in B:
                    output.append((i + " " + j).strip())
            return output

        s_dict = {}  # all the possible words
        bucket = []
        checked = []  # to store of
        for i in range(len(synonyms)):
            if i not in checked:  # current combination has not been checked yet.
                checked.append(i)
                bucket.append([])
                for _ in range(len(synonyms[i])):
                    if synonyms[i][_] not in bucket[-1]:
                        bucket[-1].append(synonyms[i][_])  # add to the current bucket
                        s_dict[synonyms[i][_]] = i  # add the word to the dictionary

                s_dict[synonyms[i][0]] = i
                s_dict[synonyms[i][1]] = i

                for j in range(i + 1, len(synonyms)):  # to find the syn array.
                    if matched(synonyms[i],
                               synonyms[j]) == 1 and j not in checked:  # current target has not been found yet
                        checked.append(j)
                        for _ in range(len(synonyms[j])):
                            if synonyms[j][_] not in bucket[-1]:
                                bucket[-1].append(synonyms[j][_])  # add to the current bucket
                                s_dict[synonyms[j][_]] = i  # add the word to the dictionary

        output = [""]
        tocheck = text.split(" ")
        for i in tocheck:
            if i not in s_dict:  # if not in the dict, just combine it with each one in the current output array
                output = cartesian(output, [i])
            else:  # need to get the all the similar words from the bucket, check the position of them
                pos = s_dict[i]
                output = cartesian(output, bucket[pos])

        output.sort()

        return output
























