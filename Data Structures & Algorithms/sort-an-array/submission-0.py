class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def heapify(nums, i, n):
            largest = i
            left = 2*i + 1
            right = 2*i + 2
            if left < n and nums[largest] < nums[left]:
                largest = left
            if right < n and nums[largest] < nums[right]:
                largest = right
            if(largest != i):
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(nums, largest, n)
            
        def heapsort(nums):
            n = len(nums)
            for i in range(n//2 -1, -1, -1):
                heapify(nums, i, n)

            for i in range(n-1, 0, -1):
                nums[i], nums[0] = nums[0], nums[i]
                heapify(nums, 0, i)
        
        heapsort(nums)

        return nums

        