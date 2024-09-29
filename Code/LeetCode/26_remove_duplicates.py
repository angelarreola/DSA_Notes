# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         myHash = {}
#         nums_len = len(nums)
#         for i in range(nums_len):
#             if myHash.get(nums[i]):
#                 nums[i] = '_'
#             else:
#                 myHash[nums[i]] = True;
        
#         j = 0
#         while nums[j]:
#             if nums[j] == '_':
#                 nums.pop(j)
#             j += 1
            
#         print(nums)
#         print(myHash)

#         return len(myHash)



# s = Solution()
# nums = [1,1,2]

# len = s.removeDuplicates(nums=nums)
# print(len)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        n = 0
        for i in range(1, len(nums)):
            n = nums[i]
            if nums[i - 1] != n:
                nums[k] = n
                k += 1
        print(nums)
        return k
            
        




s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
len = s.removeDuplicates(nums=nums)
print(len)