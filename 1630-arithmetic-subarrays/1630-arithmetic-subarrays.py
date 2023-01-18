class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(nums)
        def good(l,r):
            k = list(sorted(nums[l:r+1]))
            if len(k) == 1:
                return True
            dif = k[1] - k[0]
            for x,y in zip(k,k[1:]):
                if y-x != dif:
                    return False
            return True
        res = []
        for a,b in zip(l,r):
            res += [good(a,b)]
        return res

                

       