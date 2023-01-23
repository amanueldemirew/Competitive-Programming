class Solution:
    def pancakeSort(self, a: List[int]) -> List[int]:
        n = len(a)
        out = []
        def flip(e):
            s = 0
            while s < e:
                a[s],a[e] = a[e],a[s]
                s+=1
                e-=1
        for i in range(n-1,-1,-1):
            max = i
            for j in range(i,-1,-1):
                if a[j] > a[max]:
                    max = j
            if max != i:
                flip(max)
                flip(i)
                out.append(max+1)
                out.append(i+1)
        return out
                
        
                
       
            