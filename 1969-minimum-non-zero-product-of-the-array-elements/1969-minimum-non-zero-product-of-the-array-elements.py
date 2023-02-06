class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10 ** 9 + 7
        res = pow(pow(2, p, MOD) - 2, pow(2, (p - 1)) - 1, MOD) * (pow(2, p, MOD) - 1)
        return int(res) % MOD