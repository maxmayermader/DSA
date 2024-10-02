class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()  # Deque to store indices of potential maximum elements
        l = r = 0  # Left and right pointers of the sliding window
        
        # Iterate through the array
        while r < len(nums):
            # Remove smaller elements from the back of the deque
            # This maintains the deque in decreasing order of element values
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)  # Add current index to the deque
            
            # Remove the leftmost element if it's outside the current window
            if l > q[0]:
                q.popleft()
            
            # If we have a full window, add the maximum to the output
            if (r + 1) >= k:
                output.append(nums[q[0]])  # The front of the deque always has the maximum
                l += 1  # Move the left pointer of the window
            
            r += 1  # Move the right pointer of the window
        
        return output