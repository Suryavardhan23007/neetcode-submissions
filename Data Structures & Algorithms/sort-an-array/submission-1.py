class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(nums, left, mid, right):
            n1, n2 = mid-left + 1, right - mid
            list1, list2 = list(), list()

            for i in range(0, n1):
                list1.insert(i, nums[left+i])
            
            for j in range(0, n2):
                list2.insert(j, nums[mid+j+1])

            i,j,t = 0,0,left

            while(i < n1 and j < n2):
                if list1[i] < list2[j]:
                    nums[t] = list1[i]
                    i += 1
                else:
                    nums[t] = list2[j]
                    j += 1
                t += 1
            
            while (i < n1):
                nums[t] = list1[i]
                i += 1
                t += 1
            
            while (j < n2):
                nums[t] = list2[j]
                j += 1
                t += 1


        def mergesort(nums, left, right):
            if(left < right):
                mid = (left + right)//2
                mergesort(nums, left, mid)
                mergesort(nums, mid+1, right)
                merge(nums, left, mid, right)

        mergesort(nums, 0, len(nums)-1)
        return nums