class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += (st +'\t')
        return res
    def decode(self, s: str) -> List[str]:
        lres = []
        lres = s.split('\t')
        lres.pop()
        return lres