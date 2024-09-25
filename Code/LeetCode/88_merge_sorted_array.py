class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
         
        nums_result = [] # Empty list on the beginning

        for i in range(m):
            nums_result.append(nums1[i])
        nums_result += nums2

        #nums_result.sort() Easy way, but what's behind this method?

        self.merge_sort(nums_result) # Merge Sort implemented

        # Copy the elements direct on nums1
        for i in range(len(nums_result)):
            nums1[i] = nums_result[i]

        
    
    def merge_sort(self, arr):
        if len(arr) > 1:
            left_arr = arr[:len(arr) // 2]
            right_arr = arr[len(arr) // 2:]

            # Recursion
            self.merge_sort(left_arr)
            self.merge_sort(right_arr)

            # Merge
            i = 0 # Left arr index
            j = 0 # Right arr index
            k = 0 # Merged arr index
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                k += 1
            #--------------------------------------------------------------
            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1
            #--------------------------------------------------------------
            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1


solution = Solution()
myNums1 = [1,2,3,0,0,0];
myNums2 = [2,5,6];


solution.merge(myNums1, 3 , myNums2, 3)
print(myNums1)