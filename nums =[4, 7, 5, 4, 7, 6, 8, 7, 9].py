nums =[4, 7, 5, 4, 7, 6, 8, 7, 9]

def sum_recursive(nums):
    if len(nums) == 0:
        return 0

    last_num = nums.pop()
    return last_num + sum_recursive(nums)