# Remove Element
from typing import List

class Solution:
  def removeElement(self, nums:List[int], val: int) -> int:
    i = 0
    for j in range(len(nums)):
      if nums[j] != val:  #if the element is not equal to val, it assigns the value of that element to the index i in the list
        nums[i] = nums[j] # update i match index j, remove element 
        i += 1 # increment i if new unique element is found
    return i
 
#  nums = [3,2,2,3], val = 3
# iteration
# i = 0, j = 0 . condition false (nums[j] != val) -> update j (j=1) + no change in nums
# i = 0, j = 1 . condition true (nums[j] != val) -> update i (i=1) and j (j=2)+ nums becomes [2, 2, 2, 3]
# i = 1, j = 2 . condition true (nums[j] != val) -> update i (i=2) and j (j=3 )+ nums becomes [2, 2, 2, 3]
# i = 2, j = 3 . condition false (nums[j] != val) -> update j (j=4) + no change in nums

# considered the first i elements of the list as the new list
# [2,2]
    
# the [2,2,2,3 ] first part of 2 is not considered as the new list, rather its the element that we want to remove


## test the solution
## s = Solution()
## print(s.removeElement([3,2,2,3], 3)) # 2