class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [-1*num for num in nums]
        # heapq.heapify(nums)

        # for i in range(k):
        #     if i == k-1:
        #         return -1*heapq.heappop(nums)
        #     heapq.heappop(nums)
        def binary_sort(arr):
            for i in range(1, len(arr)):
                key = arr[i]
                # Find the position where `key` should be inserted using binary search
                left, right = 0, i - 1
                while left <= right:
                    mid = (left + right) // 2
                    if arr[mid] < key:
                        left = mid + 1
                    else:
                        right = mid - 1
                
                # Insert `key` at the correct position in the sorted sequence
                arr.insert(left, key)
                # Remove the original key
                arr.pop(i + 1)
        binary_sort(nums)
        # print(nums)
        return nums[-k]

        