class Solution:
    def maxWater(self, arr):
        n = len(arr)
        
        
        if n < 3:
            return 0
        
        left, right = 0, n - 1
        max_left, max_right = arr[left], arr[right]
        water = 0
        
        while left <= right:
            if max_left <= max_right:
                
                water += max(0, max_left - arr[left])
                max_left = max(max_left, arr[left])
                left += 1
            else:
                
                water += max(0, max_right - arr[right])
                max_right = max(max_right, arr[right])
                right -= 1
        
        return water
