class MyCalendarThree:

    def __init__(self):
        self.cal = []
        self.busiest = 0

    def book(self, start: int, end: int) -> int:
        self.cal.append([start, end - 1])
        self.cal.sort()
        scan  = []
        cnt = 0
        for i in self.cal:
            if i[0] > end-1:
                break
            elif i[0] <= start <= i[1] or i[0] <= end-1 <= i[1] or (  start <=i[0] and end -1 >= i[1]  ):
                scan.append(i[0])
                scan.append(i[1])

        for s in scan:
            cnt = 0
            for i in self.cal:
                curr = i
                if curr[0] > s:
                    break
                elif curr[1] < s:
                    continue
                elif curr[0] <= s <= curr[1]:
                    cnt += 1
            self.busiest = max(cnt, self.busiest)

        return self.busiest


# Your MyCalendarThree object will be instantiated and called as such:
obj = MyCalendarThree()
a = []
a.append(obj.book(6177, 6227))
a.append(obj.book(8480, 8525))
a.append(obj.book(7442, 7491))
a.append(obj.book(5740, 5780))
a.append(obj.book(1885, 1939))
a.append(obj.book(3374, 3411))
a.append(obj.book(2670, 2722))
a.append(obj.book(4505, 4537))
a.append(obj.book(6177, 6209))
a.append(obj.book(4316, 4346))
a.append(obj.book(4821, 4861))
a.append(obj.book(3330, 3383))
a.append(obj.book(8196, 8233))
a.append(obj.book(5027, 5079))
a.append(obj.book(6944, 6985))
a.append(obj.book(1915, 1964))
a.append(obj.book(5485, 5519))
a.append(obj.book(1474, 1513))
a.append(obj.book(3084, 3134))
a.append(obj.book(5582, 5614))
a.append(obj.book(6146, 6185))
a.append(obj.book(3531, 3579))
a.append(obj.book(8758, 8803))
a.append(obj.book(7386, 7419))
a.append(obj.book(6473, 6514))
a.append(obj.book(1468, 1520))
a.append(obj.book(8305, 8358))
a.append(obj.book(3575, 3617))
a.append(obj.book(1088, 1143))
a.append(obj.book(5025, 5071))
a.append(obj.book(5666, 5699))
a.append(obj.book(3128, 3161))
a.append(obj.book(2560, 2590))
a.append(obj.book(8262, 8303))
a.append(obj.book(6316, 6363))
a.append(obj.book(8051, 8108))
a.append(obj.book(6077, 6125))
a.append(obj.book(8735, 8769))
a.append(obj.book(9853, 9906))
a.append(obj.book(3186, 3218))
a.append(obj.book(5455, 5501))
a.append(obj.book(1843, 1885))
a.append(obj.book(9464, 9514))
a.append(obj.book(2176, 2207))
a.append(obj.book(998, 1035))
a.append(obj.book(1035, 1080))
a.append(obj.book(8525, 8557))
a.append(obj.book(3008, 3057))
a.append(obj.book(2037, 2093))
a.append(obj.book(6553, 6600))
a.append(obj.book(9186, 9231))
a.append(obj.book(9397, 9432))
a.append(obj.book(1137, 1178))
a.append(obj.book(7841, 7880))
a.append(obj.book(9283, 9317))
a.append(obj.book(4666, 4700))
a.append(obj.book(442, 498))
a.append(obj.book(4355, 4409))
a.append(obj.book(7237, 7281))
a.append(obj.book(1092, 1127))
a.append(obj.book(1469, 1511))
a.append(obj.book(3885, 3929))
a.append(obj.book(8760, 8816))
a.append(obj.book(7927, 7974))
a.append(obj.book(2536, 2594))
a.append(obj.book(8332, 8378))
a.append(obj.book(8656, 8712))
a.append(obj.book(1793, 1824))
a.append(obj.book(7411, 7443))
a.append(obj.book(9621, 9655))
a.append(obj.book(7281, 7314))
a.append(obj.book(5218, 5266))
a.append(obj.book(5781, 5825))
a.append(obj.book(5691, 5746))
a.append(obj.book(8843, 8899))
a.append(obj.book(9903, 9947))
a.append(obj.book(3997, 4034))
a.append(obj.book(1772, 1820))
a.append(obj.book(3315, 3358))
a.append(obj.book(3863, 3915))
a.append(obj.book(6708, 6746))
a.append(obj.book(7201, 7241))
a.append(obj.book(2416, 2464))
a.append(obj.book(9245, 9279))
a.append(obj.book(4003, 4039))
a.append(obj.book(1230, 1271))
a.append(obj.book(629, 680))
a.append(obj.book(4141, 4173))
a.append(obj.book(521, 556))
a.append(obj.book(9279, 9312))
a.append(obj.book(3227, 3282))
a.append(obj.book(6288, 6336))
a.append(obj.book(8647, 8695))
a.append(obj.book(3271, 3301))
a.append(obj.book(4032, 4065))
a.append(obj.book(4868, 4899))
a.append(obj.book(4151, 4194))
a.append(obj.book(5244, 5280))
a.append(obj.book(665, 706))
a.append(obj.book(5083, 5140))
a.append(obj.book(1286, 1329))
a.append(obj.book(8648, 8682))
a.append(obj.book(1826, 1867))
a.append(obj.book(3427, 3477))
a.append(obj.book(1478, 1523))
a.append(obj.book(7327, 7370))
a.append(obj.book(4419, 4459))
a.append(obj.book(8226, 8261))
a.append(obj.book(5167, 5215))
a.append(obj.book(3687, 3727))
a.append(obj.book(3206, 3260))
a.append(obj.book(2137, 2174))
a.append(obj.book(3562, 3618))
a.append(obj.book(9113, 9153))
a.append(obj.book(141, 196))
a.append(obj.book(1155, 1209))
a.append(obj.book(6043, 6078))
a.append(obj.book(3036, 3082))
a.append(obj.book(475, 516))
a.append(obj.book(1665, 1723))
a.append(obj.book(9817, 9869))
a.append(obj.book(7453, 7486))
a.append(obj.book(9272, 9324))
a.append(obj.book(2238, 2283))
a.append(obj.book(2266, 2309))
a.append(obj.book(6671, 6704))
a.append(obj.book(7042, 7091))
a.append(obj.book(5149, 5185))
a.append(obj.book(6404, 6457))
a.append(obj.book(9743, 9787))
a.append(obj.book(3417, 3451))
a.append(obj.book(335, 377))
a.append(obj.book(4835, 4893))
a.append(obj.book(8723, 8776))
a.append(obj.book(3241, 3277))
a.append(obj.book(4126, 4161))
a.append(obj.book(1183, 1217))
a.append(obj.book(8318, 8377))
a.append(obj.book(6610, 6656))
a.append(obj.book(1882, 1917))
a.append(obj.book(9925, 9964))
a.append(obj.book(4285, 4316))
a.append(obj.book(9982, 10000))
a.append(obj.book(4415, 4468))
a.append(obj.book(24, 59))
a.append(obj.book(6311, 6345))
a.append(obj.book(2250, 2291))
a.append(obj.book(9501, 9547))
a.append(obj.book(4766, 4811))
a.append(obj.book(3362, 3409))
a.append(obj.book(9486, 9522))
a.append(obj.book(1349, 1398))
a.append(obj.book(3963, 4014))
a.append(obj.book(4799, 4847))
a.append(obj.book(3608, 3664))
a.append(obj.book(511, 542))
a.append(obj.book(3501, 3534))
a.append(obj.book(7609, 7643))
a.append(obj.book(215, 263))
a.append(obj.book(8716, 8750))
a.append(obj.book(9419, 9463))
a.append(obj.book(260, 290))
a.append(obj.book(5987, 6029))
a.append(obj.book(4069, 4119))
a.append(obj.book(3418, 3463))
a.append(obj.book(755, 810))
a.append(obj.book(6039, 6089))
a.append(obj.book(9153, 9211))
a.append(obj.book(9865, 9919))
a.append(obj.book(3770, 3804))
a.append(obj.book(4577, 4615))
a.append(obj.book(7557, 7597))
a.append(obj.book(629, 667))
a.append(obj.book(7688, 7720))
a.append(obj.book(8003, 8034))
a.append(obj.book(2899, 2936))
a.append(obj.book(1970, 2011))
a.append(obj.book(9039, 9075))
a.append(obj.book(4107, 4141))
a.append(obj.book(3163, 3193))
a.append(obj.book(9224, 9275))
a.append(obj.book(9827, 9863))
a.append(obj.book(8078, 8133))
a.append(obj.book(6783, 6821))
a.append(obj.book(9815, 9866))
a.append(obj.book(3088, 3134))
a.append(obj.book(1168, 1217))
a.append(obj.book(4510, 4563))
a.append(obj.book(4539, 4580))
a.append(obj.book(2124, 2181))
a.append(obj.book(2794, 2842))
a.append(obj.book(6232, 6269))
a.append(obj.book(9361, 9408))
a.append(obj.book(9882, 9923))
a.append(obj.book(6229, 6275))
a.append(obj.book(1685, 1733))
a.append(obj.book(7594, 7637))
a.append(obj.book(4720, 4768))
a.append(obj.book(8739, 8776))
a.append(obj.book(8993, 9032))
a.append(obj.book(2756, 2809))
a.append(obj.book(8415, 8449))
a.append(obj.book(8887, 8924))
a.append(obj.book(2478, 2524))
a.append(obj.book(757, 815))
a.append(obj.book(3836, 3879))
a.append(obj.book(1885, 1929))
a.append(obj.book(3121, 3167))
a.append(obj.book(4142, 4196))
a.append(obj.book(5296, 5330))
a.append(obj.book(38, 85))
a.append(obj.book(6027, 6062))
a.append(obj.book(6738, 6769))
a.append(obj.book(2449, 2480))
a.append(obj.book(9236, 9274))
a.append(obj.book(7474, 7533))
a.append(obj.book(7478, 7519))
a.append(obj.book(8679, 8735))
a.append(obj.book(2225, 2256))
a.append(obj.book(2168, 2224))
a.append(obj.book(9056, 9093))
a.append(obj.book(2577, 2632))
a.append(obj.book(6644, 6680))
a.append(obj.book(6975, 7011))
a.append(obj.book(7256, 7305))
a.append(obj.book(524, 571))
a.append(obj.book(1662, 1719))
a.append(obj.book(9275, 9332))
a.append(obj.book(4958, 5007))
a.append(obj.book(2637, 2673))
a.append(obj.book(4037, 4069))
a.append(obj.book(8537, 8583))
a.append(obj.book(5912, 5949))
a.append(obj.book(2978, 3018))
a.append(obj.book(3003, 3047))
a.append(obj.book(5778, 5817))
a.append(obj.book(839, 887))
a.append(obj.book(836, 872))
a.append(obj.book(735, 790))
a.append(obj.book(4383, 4441))
a.append(obj.book(5622, 5675))
a.append(obj.book(8617, 8669))
a.append(obj.book(2219, 2257))
a.append(obj.book(2841, 2879))
a.append(obj.book(12, 49))
a.append(obj.book(248, 278))
a.append(obj.book(7951, 7981))
a.append(obj.book(1189, 1234))
a.append(obj.book(9149, 9196))
a.append(obj.book(6984, 7039))
a.append(obj.book(7142, 7177))
a.append(obj.book(8092, 8151))
a.append(obj.book(5439, 5490))
a.append(obj.book(2991, 3030))
a.append(obj.book(1532, 1589))
a.append(obj.book(5054, 5091))
a.append(obj.book(6019, 6055))
a.append(obj.book(9372, 9426))
a.append(obj.book(3112, 3148))
a.append(obj.book(6196, 6253))
a.append(obj.book(25, 72))
a.append(obj.book(9726, 9781))
a.append(obj.book(1365, 1418))
a.append(obj.book(6112, 6154))
a.append(obj.book(8215, 8256))
a.append(obj.book(5258, 5292))
a.append(obj.book(1182, 1215))
a.append(obj.book(5348, 5406))
a.append(obj.book(2619, 2666))
a.append(obj.book(805, 852))
a.append(obj.book(6896, 6951))
a.append(obj.book(5461, 5518))
a.append(obj.book(6732, 6773))
a.append(obj.book(74, 132))
a.append(obj.book(1262, 1315))
a.append(obj.book(6646, 6702))
a.append(obj.book(5111, 5147))
a.append(obj.book(6200, 6233))
a.append(obj.book(7718, 7748))
a.append(obj.book(1298, 1328))
a.append(obj.book(7478, 7523))
a.append(obj.book(9845, 9875))
a.append(obj.book(7221, 7268))
a.append(obj.book(8930, 8965))
a.append(obj.book(3047, 3101))
a.append(obj.book(9305, 9363))
a.append(obj.book(1732, 1781))
a.append(obj.book(6386, 6435))
a.append(obj.book(4305, 4353))
a.append(obj.book(7028, 7061))
a.append(obj.book(9256, 9303))
a.append(obj.book(954, 990))
a.append(obj.book(691, 731))
a.append(obj.book(7386, 7418))
a.append(obj.book(6903, 6947))
a.append(obj.book(7116, 7162))
a.append(obj.book(8884, 8936))
a.append(obj.book(3501, 3536))
a.append(obj.book(441, 499))
a.append(obj.book(8040, 8074))
a.append(obj.book(1101, 1153))
a.append(obj.book(9438, 9496))
a.append(obj.book(7857, 7910))
a.append(obj.book(3991, 4044))
a.append(obj.book(3694, 3746))
a.append(obj.book(5582, 5619))
a.append(obj.book(1439, 1473))
a.append(obj.book(5140, 5185))
a.append(obj.book(8170, 8228))
a.append(obj.book(9053, 9108))
a.append(obj.book(9018, 9076))
a.append(obj.book(5934, 5981))
a.append(obj.book(7902, 7958))
a.append(obj.book(2736, 2788))
a.append(obj.book(2270, 2311))
a.append(obj.book(3557, 3597))
a.append(obj.book(8809, 8859))
a.append(obj.book(3234, 3287))
a.append(obj.book(9972, 10000))
a.append(obj.book(842, 872))
a.append(obj.book(9442, 9484))
a.append(obj.book(8159, 8193))
a.append(obj.book(7451, 7507))
a.append(obj.book(1296, 1343))
a.append(obj.book(6866, 6916))
a.append(obj.book(9122, 9159))
a.append(obj.book(1740, 1793))
a.append(obj.book(6616, 6673))
a.append(obj.book(5815, 5851))
a.append(obj.book(8935, 8993))
a.append(obj.book(3462, 3520))
a.append(obj.book(4503, 4534))
a.append(obj.book(8623, 8669))
a.append(obj.book(222, 255))
a.append(obj.book(5073, 5125))
a.append(obj.book(5604, 5653))
a.append(obj.book(4359, 4403))
a.append(obj.book(5188, 5226))
a.append(obj.book(9363, 9403))
a.append(obj.book(5416, 5468))
a.append(obj.book(640, 673))
a.append(obj.book(1704, 1734))
a.append(obj.book(3627, 3683))
a.append(obj.book(6610, 6660))
a.append(obj.book(2938, 2978))
a.append(obj.book(2596, 2653))
a.append(obj.book(6497, 6530))
a.append(obj.book(4862, 4920))
a.append(obj.book(3534, 3579))
a.append(obj.book(5517, 5561))
a.append(obj.book(9983, 10000))
a.append(obj.book(6270, 6305))
a.append(obj.book(7248, 7300))
a.append(obj.book(9100, 9157))
a.append(obj.book(4728, 4763))
a.append(obj.book(5249, 5288))
a.append(obj.book(1729, 1771))
a.append(obj.book(3407, 3452))
a.append(obj.book(6440, 6475))
a.append(obj.book(4145, 4176))
a.append(obj.book(1968, 2026))
a.append(obj.book(4322, 4352))
a.append(obj.book(2121, 2180))
a.append(obj.book(7900, 7934))
a.append(obj.book(7859, 7899))
a.append(obj.book(517, 552))
a.append(obj.book(5944, 5984))
a.append(obj.book(7641, 7683))
a.append(obj.book(7466, 7517))
a.append(obj.book(8849, 8894))
a.append(obj.book(6960, 7004))
a.append(obj.book(9996, 10000))
a.append(obj.book(2381, 2429))
a.append(obj.book(1752, 1804))
a.append(obj.book(1831, 1867))
a.append(obj.book(8115, 8156))
a.append(obj.book(8404, 8440))
a.append(obj.book(3000, 3051))
a.append(obj.book(9867, 9921))
a.append(obj.book(7800, 7830))
a.append(obj.book(3787, 3818))
a.append(obj.book(8938, 8977))
a.append(obj.book(3881, 3925))
a.append(obj.book(857, 901))
a.append(obj.book(7665, 7696))
a.append(obj.book(3519, 3561))
a.append(obj.book(4640, 4677))
a.append(obj.book(4705, 4760))
a.append(obj.book(2387, 2427))
a.append(obj.book(4002, 4035))
a.append(obj.book(4555, 4586))
a.append(obj.book(9830, 9860))
a.append(obj.book(7124, 7164))
a.append(obj.book(4874, 4923))
a.append(obj.book(3305, 3336))
a.append(obj.book(598, 653))
a.append(obj.book(2690, 2744))
a.append(obj.book(1531, 1589))
a.append(obj.book(6101, 6144))
print(obj.cal)
print(a)