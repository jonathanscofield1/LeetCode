class Solution:
    def isMatch(self, s: str, p: str) -> bool:
            return re.fullmatch(re.sub("[\*]+", "*", p), s) if "**" in p else re.fullmatch(p, s)

        