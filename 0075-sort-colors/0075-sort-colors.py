class Solution:
    def sortColors(self, nums: List[int]) -> None:
        r = len(nums) - 1
        i=0
        l = 0
        while i <= r:
            if nums[i]==0:
                nums[i],nums[l]=nums[l],nums[i]
                l+=1
                
            elif nums[i]==2:
                nums[i],nums[r]=nums[r],nums[i]
                i-=1
                r-=1
            i+=1
           
        
            


        

        
        """
        Do not return anything, modify nums in-place instead.
        """