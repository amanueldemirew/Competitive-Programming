class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        output = []
        n = len(changed)
        changed.sort()
        count = Counter(changed)
        if n % 2:
            return []
        for x in changed:
            if x == 0 and count[x] >= 2:
                count[x]-=2
                output.append(x)
            elif x > 0 and count[x] and count[2*x]:
                count[x]-=1
                count[2*x]-=1
                output.append(x)
        if len(output) == n // 2:
            return output
        else:
            return []