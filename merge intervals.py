class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
    
        if len(intervals) <= 1:
            return intervals
        
        
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        merged.append(intervals[0])
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            last_end = merged[-1][1]
            
            
            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])
        
        return merged
