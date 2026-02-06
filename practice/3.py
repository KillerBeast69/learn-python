def remove_nonints(nums):
    integers = []
    for element in nums:
        if element == type(int):
            integers.append(element)
    return integers