def contains_repeating_numbers(arr):
    return not sorted(arr) == list(set(arr))

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(contains_repeating_numbers(nums))