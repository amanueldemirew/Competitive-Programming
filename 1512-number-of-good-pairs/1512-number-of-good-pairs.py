class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        nums.sort()
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    count += 1
                    #nums.pop(nums[i])
        return count

