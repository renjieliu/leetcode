class Solution:
    def mostVisitedPattern(self, username: 'List[str]', timestamp: 'List[int]', website: 'List[str]') -> 'List[str]':
        pack = sorted(list(zip(username, timestamp, website)), key=lambda x: x[1])
        username_wk = []
        website_wk = []
        for p in pack:
            username_wk.append(p[0])
            website_wk.append(p[2])

        hmp_person = {}
        for i, c in enumerate(username_wk):  # websites the person visted
            if c not in hmp_person:
                hmp_person[c] = []
            hmp_person[c].append(website_wk[i])

        hmp_seq = {}
        maxx = -float('inf')
        output = None
        person_seq = {}
        for p, v in hmp_person.items():
            if len(v) >= 3:
                if p not in person_seq:
                    person_seq[p] = []
                for i in range(len(v) + 1 - 3):
                    for j in range(i + 1, len(v) + 1 - 2):
                        for k in range(j + 1, len(v)):
                            seq = (v[i], v[j], v[
                                k])  # current 3 sequence, to check how many times it has been visited tuple(v[i:i+3])
                            if seq not in person_seq[p]:
                                person_seq[p].append(seq)
        hmp_seq = {}
        for k, v in person_seq.items():
            for c in v:
                if c not in hmp_seq:
                    hmp_seq[c] = 0
                hmp_seq[c] += 1

                if hmp_seq[c] > maxx:
                    maxx = hmp_seq[c]
                    output = c

                elif hmp_seq[c] == maxx and c < output:
                    output = c

        # print(pack)
        # print(hmp_seq)
        return list(output)


