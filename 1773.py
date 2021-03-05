class Solution:
    def countMatches(self, items: 'List[List[str]]', ruleKey: str, ruleValue: str) -> int:
        order = 0 if ruleKey == "type" else (1 if ruleKey=="color" else 2)
        return sum (1 if item[order] == ruleValue else 0 for item in items )

