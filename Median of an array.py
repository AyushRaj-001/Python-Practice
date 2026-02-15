class Solution:
    def findMedian(self, arr):
        
        n = len(arr)
        
        
        arr.sort()
        
        
        if n % 2 != 0:
            return arr[n // 2]
        
        
        else:
            return (arr[n // 2 - 1] + arr[n // 2]) / 2
