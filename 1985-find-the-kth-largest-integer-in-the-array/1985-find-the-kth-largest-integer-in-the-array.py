class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        n = len(nums)
        output = []
        for x in nums:
            y = int(x)
            output.append(y)
        output.sort()
        
        return str(output[n-k]) 
            