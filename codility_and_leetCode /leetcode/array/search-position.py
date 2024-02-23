# Search insert position
from typing import List

class Solution:
  def searchInsert(nums:List[int], target:int) -> int:
    left, right = 0, len(nums) - 1 # set values for left and right
    while left <= right:
      mid = (left + right) // 2
      if nums[mid] == target:
        return mid
      elif nums[mid] < target:
        left = mid + 1
      else:
        right = mid - 1
    return left
  
## exampple 1
  # nums [1,3,5,6], target = 5

  # left = 0
  # right = 3

  # mid in first iteration 0 + 3 // 2 = 1  --> find the midle index
  # nums[1] = 3 < 5 --> look at index 1  = 3
  # left = 1 + 1 = 2

  # mid in second iteration 2 + 3 // 2 = 2
  # nums[2] = 5 == 5
  # return 2

## example 2
  # nums = [1,3,5,6], target = 2

  # left = 0
  # right = 3

  # first iteration
  # mid = 0 + 3 // 2 = 1
  # nums[1] = 3 < 5
  # left = 1 + 1 = 2

  # return 1
  

## example 3
  # nums [1,3,5,6], target = 7
 
  # left = 0
  # right = 3

  # first iteration
  # mid = 0 + 3 // 2 = 1
  # nums[1] = 3 < 7
  # left = 1 + 1 = 2

  # second iteration
  # mid = 2 + 3 // 2 = 2
  # nums[2] = 5 < 7
  # left = 2 + 1 = 3

  # third iteration
  # mid = 3 + 3 // 2 = 3
  # nums[3] = 6 < 7
  # left = 3 + 1 = 4 

  # return 4 --> 4 is the index where 7 should be inserted


## example 1
    # nums [1,3,5,6], target = 5
    # low = 0 
    # high = 4 
  
    # first iteration
    # mid = 0 + 4 // 2 = 2
    # nums[2] = 5 == 5
    # return 2
  
## example 2
    # nums [1,3,5,6], target = 2
    # low = 0
    # high = 4
  
    # first iteration
    # mid = 0 + 4 // 2 = 2
    # nums[2] = 2 > 5
    # high = mid
    # high = 2
  
    # second iteration
    # mid = 0 + 2 // 2 = 1
    # nums[3] = 2 > 6
    # high = mid
    # high = 1

    # third iteration
    # mid = 0 + 1 // 2 = 0
    # nums[0] = 2 > 1
    # low = 1 , high = 1

    # low is no longer less than or equal to high. 

  
