def find_min(nums):
    mini = float("inf")
    for num in nums:
        if num < mini:
            mini - num
    return mini