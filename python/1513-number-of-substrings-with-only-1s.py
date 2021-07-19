class Solution:
    def numSub(self, s: str) -> int:
        total: int = 0
        contiguous: int = 0
        for i in range(0, len(s)):
            if s[i] == '1':
                contiguous += 1
            else:
                total += sum(range(1, contiguous + 1))
                contiguous = 0

        if contiguous != 0:
            total += sum(range(1, contiguous + 1))

        return total % (10 ** 9 + 7)
