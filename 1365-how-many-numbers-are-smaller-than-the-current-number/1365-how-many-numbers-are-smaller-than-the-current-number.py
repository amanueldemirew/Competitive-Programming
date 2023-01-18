class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        n = len(nums)

        

        count_list = []

        for i in range(n):
            
            count = 0
            
            for j in range(n):
                
                if nums[i] > nums[j]:
                    
                    count+=1

            count_list.append(count)

        return count_list
