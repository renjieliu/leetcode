class Solution:
    def reformatDate(self, date: str) -> str:
        translate = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        return date[-4:] + "-" + translate[date[-8:-5]] + "-" + ("0" if len(date[:-11]) == 1 else "") + date[:-11] 