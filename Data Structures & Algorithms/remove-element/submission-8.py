class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr1 = 0
        count = 0
        for num in nums:
            if num != val:
                nums[ptr1] = num
                ptr1 += 1
                count += 1
        return count
        