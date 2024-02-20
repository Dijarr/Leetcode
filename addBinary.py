class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bin1 = int(a, 2)
        bin2 = int(b, 2)
        result = bin(bin1 + bin2)[2:]
        return result
