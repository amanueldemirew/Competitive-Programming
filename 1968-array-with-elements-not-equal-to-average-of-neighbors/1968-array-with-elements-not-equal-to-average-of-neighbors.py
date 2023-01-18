class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        n= len(nums)
        for i in range(1,n,2):
            nums[i-1],nums[i] = nums[i],nums[i-1]
        
        return nums

        

        
