class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, len(nums)-1
        out = []
        while i < j:
            
            out.append(nums[i]+nums[j])
            i+=1
            j-=1
        x = max(*out)
        return x
            
            
            
        