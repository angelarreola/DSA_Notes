class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums_len = len(nums)
        k = 0

        for i in range(nums_len):
            if nums[i] != val:
                nums[k] = nums[i] # We only keep the number that are not equal to the value.
                k += 1
        return k
    

obj = Solution()

nums = [0,1,2,2,3,0,4,2]
val = 2
obj.removeElement(nums=nums, val=val)

print(nums)
        