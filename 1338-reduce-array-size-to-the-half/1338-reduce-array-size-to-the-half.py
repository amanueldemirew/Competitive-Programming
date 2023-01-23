class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        freq = list(c.values())
        freq.sort()
        
        ans, removed, half = 0, 0, len(arr) // 2
        while removed < half:
            ans += 1
            removed += freq.pop()
        return ans
        