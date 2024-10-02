class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        result = []
        window = deque()
        
        for i in range(len(nums)):
            # Remove indices that are out of the current window
            if window and window[0] == i - k:
                window.popleft()
            
            # Remove all indices with smaller values than the current element
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            
            window.append(i)
            
            # Start adding to result when we have our first k-sized window
            if i >= k - 1:
                result.append(nums[window[0]])
        
        return result