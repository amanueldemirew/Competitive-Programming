class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        tsum = 0
        p = {0:1}
        for n in nums:
            tsum += n
            diff = tsum - k
            ans += p.get(diff,0)
            p[tsum] = 1 + p.get(tsum,0)
        return ans

        