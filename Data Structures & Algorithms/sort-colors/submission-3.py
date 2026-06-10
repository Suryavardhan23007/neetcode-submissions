class Solution:
    def sortColors(self, nums: List[int]) -> None:
        ptr0, ptr2, index = 0, len(nums)-1, 0
        while(index <= ptr2):
            if nums[index] == 0:
                nums[ptr0], nums[index] = nums[index], nums[ptr0]
                ptr0 += 1
                index += 1
            elif nums[index] == 2:
                nums[ptr2], nums[index] = nums[index], nums[ptr2]
                ptr2 -= 1
            else:
                index += 1
            
        