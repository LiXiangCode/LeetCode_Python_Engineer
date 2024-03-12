def counter_sort(nums):
    max_value, min_value = max(nums), min(nums)
    counter_nums = [0 for _ in range(max_value - min_value + 1)]
    for value in nums:
        counter_nums[value - min_value] += 1
           
    new_num = 0 
    for j in range(len(counter_nums)):
        if counter_nums[j] > 0:
            for k in range(counter_nums[j]):
                nums[new_num] = j + min_value
                new_num += 1
    return nums
    
def three_sum_zero(nums) :
    nums = counter_sort(nums)
    result = []
    if nums[0] > 0:
        return result
    for t in range(len(nums) - 2):
        if t > 0 and nums[t] == nums[t - 1]:
            continue
        start, end = t + 1, len(nums) - 1
        two_sums = double_pointer(nums, start, end, nums[t])
        for two_sum in two_sums:
            result.append([nums[t]] + two_sum)
    return result

def double_pointer(nums, start, end, target):
    result = []
    while start < end:
        if target + nums[start] + nums[end] < 0:
            start += 1
        elif target + nums[start] + nums[end] == 0:
            result.append([nums[start], nums[end]])
            while start < end and nums[start] == nums[start + 1]:
                start += 1
            while start < end and nums[end] == nums[end - 1]:
                end -= 1
            start += 1
            end -= 1
        else:
            end -= 1    
    return result   
    
#nums = [-1, 0, 1, 2, -1, -4]
#nums = [0, 1, 1]
nums = [0, 0, 0]
print(three_sum_zero(nums))
        