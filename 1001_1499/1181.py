class Solution:
    def beforeAndAfterPuzzles(self, phrases: 'List[str]') -> 'List[str]':
        def stitch(pre, post):
            output = []
            for a in pre:
                for b in post:
                    if a[0] != b[0]:
                        output.append((a[1] + ' ' + b[1]).strip())
            return output

        hmp_pre = {}
        hmp_post = {}
        for i in range(len(phrases)):
            p = phrases[i]
            curr = p.split(' ')
            pre = curr[-1]  # for pre, to add all the words, except for the last
            post = curr[0]  # for post, to add all the words
            if pre not in hmp_pre:
                hmp_pre[pre] = []
            hmp_pre[pre].append([i, ' '.join(curr[:-1])])  # add the full sentence, except for the last word
            if post not in hmp_post:
                hmp_post[post] = []
            hmp_post[post].append([i, ' '.join(curr)])  # add the full sentence
            output = []
        # print(hmp_pre, hmp_post)
        for k, v in hmp_pre.items():
            if k in hmp_post:
                output += stitch(v, hmp_post[k])

        return sorted(list(set(output)))





