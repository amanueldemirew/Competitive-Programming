class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        display = []
        tindex = -1
        nums.sort()
        for x in nums:
            tindex += 1

            if target == x:
                display.append(tindex)
        return display