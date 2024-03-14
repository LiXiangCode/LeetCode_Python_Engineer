import sys
sys.path.append("/Users/zengxiaowei/STUDY/Github/LeetCode/Python_Coding")

from leetcode_data import nums
from calculate_execute_time import d_calculate_execute_time

@d_calculate_execute_time
def trap(nums):
    left, right = 0, len(nums)-1
    left_max, right_max = 0, 0
    volume = 0
    while left < right:
        if nums[left] < nums[right]:
            if nums[left] >= left_max:
                left_max = nums[left]
            else:
                volume += (left_max - nums[left])
            left += 1
        else:
            if nums[right] >= right_max:
                right_max = nums[right]
            else:
                volume += (right_max - nums[right])
            right -= 1
    return volume


    


#nums = [0,1,0,2,1,0,1,3,2,1,2,1]
#nums = [4,2,0,3,2,5]
# nums = [0, 0, 0, 0, 1, 0, 0, 0]
# nums = [6, 5, 4, 3, 2, 1]
# nums = [1, 2, 3, 4, 5, 6]
# nums = [1, 0, 1]
# nums = [1, 1, 0]
# nums = [0, 0, 1, 1, 0, 1, 0]
# nums = [4, 2, 3]
#nums = [10, 1, 9, 1, 8, 1, 7, 1, 6, 1, 5, 1, 4]
print(trap(nums))
    
        