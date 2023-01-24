class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = Counter(nums)
        out = []
        for x in c:
            out.append(c[x])
        out.sort()
        n = len(out)
        fin = []
        for i in range(k):
            for y in c:
                if out[n-i-1] == c[y]:
                    fin.append(y)
        return set(fin)
                    
        
        