# Brute Force Solution
# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         count = 0
#         majoriry_element = nums[0]

#         for i in range(len(nums)):
#             reps = 1
#             for j in range(len(nums)):
#                 if nums[j] == nums[i]:
#                     reps += 1
#             if reps > count:
#                 majoriry_element = nums[i]
#                 count = reps
#         return majoriry_element 
            

# # HashMap Solution
# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         myHash = {}
#         for i in range(len(nums)):
#             if myHash.get(nums[i]):
#                 myHash[nums[i]] += 1
#             else:
#                 myHash[nums[i]] = 1

#         majority_reps = 0      
#         for key in myHash:
#             val = myHash.get(key)
#             if val > majority_reps:
#                 majority_reps = val
#                 majority_key = key
#         return majority_key
        
# HashMap Solution ENHANCED
# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         numsHash = {}
#         for i in range(len(nums)):
#             if numsHash.get(nums[i]):
#                 numsHash[nums[i]] += 1
#             else:
#                 numsHash[nums[i]] = 1

#         majority_reps = len(nums) // 2     
#         for key in numsHash:
#             if numsHash[key] > majority_reps:
#                 return key

# MindFuck Solution
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        ans = -1
        count = 0
        for n in nums:
            if count == 0:
                ans = n
            if n == ans:
                count += 1
            else:
                count -= 1
        return ans

        #Time: O(n)
        #Space: O(1)

s = Solution()

nums = [2,2,1,1,1,2,2]
answer = s.majorityElement(nums)

print(answer)
