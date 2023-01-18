class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        output = [intervals[0]]
        for x,y in intervals:
            if x > output[-1][1]:
                output.append([x,y])
            elif y > output[-1][1]:
                output[-1][1]= y
        return output

