class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        count = 1

        for i in range(1, len(nums)):
            num = nums[i]
            if num == nums[i - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[k] = num
                k += 1
        return k
                




s = Solution()
nums = [1,1,1,2,2,3]
len = s.removeDuplicates(nums=nums)
print(len)