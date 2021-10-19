import decimal


class Solution:
    def maxPoints(points: 'List[List[int]]') -> int:
        def formula(p1, p2):
            if p1[0] == p2[0]:
                return str('0-0-') + str(p1[0])  # p1[0] shows the x axis value
            elif p1[1] == p2[1]:
                return str('0-' + str(p1[1]))  # p1[1] shows the y axis value
            else:
                x1 = decimal.Decimal(p1[0])
                x2 = decimal.Decimal(p2[0])
                y1 = decimal.Decimal(p1[1])
                y2 = decimal.Decimal(p2[1])
                k = (y1 - y2) / (x1 - x2)  # python return -0.0 for 0/-1
                if p1[0] == p1[1] == 0:
                    b = p2[1] - p2[0] * k
                else:
                    b = p1[1] - p1[0] * k
                return str(k) + '-' + str(b)

        if len(points) < 2:
            return len(points)

        else:
            f_dict = {}  # to store the points on the same line
            points_cnt = {}
            uq_points = []
            for p in points:
                x = '-'.join([str(_) for _ in p])
                if x not in points_cnt:
                    points_cnt[x] = -1  # just to record how many dups in the original array
                    uq_points.append(p)
                points_cnt[x] += 1
            if len(uq_points) == 1:
                return list(points_cnt.values())[0] + 1  # There should be only one value in the points_cnt

            i, output = 0, 2
            while i < len(uq_points):
                j = i + 1
                while j < len(uq_points):
                    f = formula(uq_points[i], uq_points[j])
                    if f not in f_dict:  # it's a new formula
                        p_k = '-'.join([str(_) for _ in uq_points[i]])
                        f_dict[f] = [1 + points_cnt[p_k], [uq_points[i]]]  # to add uq_points[i]

                    if uq_points[j] not in f_dict[f][1]:
                        p_k = '-'.join(
                            [str(_) for _ in uq_points[j]])  # generate the hash key to find how many dups for it
                        f_dict[f][0] += 1 + points_cnt[p_k]
                        f_dict[f][1].append(uq_points[j])

                    output = max(output, f_dict[f][0])

                    j += 1
                i += 1

            return output


