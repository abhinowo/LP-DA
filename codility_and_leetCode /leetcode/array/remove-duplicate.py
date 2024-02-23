from typing import List
# remove duplicates from sorted array

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    if not nums:
      return 0
    else:
      i = 0
      for j in range(1, len(nums)): # iterate through indices of the `nums`
        if nums[j] != nums[i]: # check condition of the element
          i += 1 # increment i if new unique element is found
          nums[i] = nums[j] # update i match index j, remove duplicates
      return i+1
    

    # nums [0,0,1,1,1,2,2,3,3,4]
    # iteration
    # i = 0, j = 1 . condition false (nums[j] != nums[i]) -> update j (j=2) + no change in nums
    # i = 0, j = 2 . condition true (nums[j] != nums[i]) -> update i (i=1) + nums becomes [0, 1, 1, 1, 2, 2, 3, 3, 4, 4]
    # i = 1, j = 3 . condition false (nums[j] != nums[i]) -> update j (j=4) + no change in nums
    # i = 1, j = 4 . condition false (nums[j] != nums[i]) -> update j (j=5) + no change in nums
    # i = 1, j = 5 . condition true (nums[j] != nums[i]) -> update i (i=2) + nums becomes [0, 1, 2, 1, 2, 2, 3, 3, 4, 4]
    # i = 2, j = 6 . condition false (nums[j] != nums[i]) -> update j (j=7) + no change in nums
    # i = 2, j = 7 . condition true (nums[j] != nums[i]) -> update i (i=3) + nums becomes [0, 1, 2, 3, 2, 2, 3, 3, 4, 4]
    # i = 3, j = 8 . condition false (nums[j] != nums[i]) -> update j (j=9) + no change in nums
    # i = 3, j = 9 . condition true (nums[j] != nums[i]) -> update i (i=4) + nums becomes [0, 1, 2, 3, 4, 2, 3, 3, 4, 4]
    # considered the first i elements of the list as the new list
    # [0, 1, 2, 3, 4]
    # end.    
