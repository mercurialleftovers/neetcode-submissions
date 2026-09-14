class Solution:
    SEPARATOR: str = "THISISASEPARATOR"
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return " "
        return Solution.SEPARATOR.join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]

        if s == " ":
            return []
        return s.split(sep=Solution.SEPARATOR)

