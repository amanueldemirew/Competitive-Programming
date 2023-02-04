class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)       
        l = 0
        r = sum(nums[1:n])
        for i in range(n-1):
            piv = i
            if l == r:
                return piv
            l += nums[i]
            r -= nums[i+1]
        if l == r:
            return n-1
        return -1
            
        

        
            
        