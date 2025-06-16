# Contains Duplicate. -->"Does this list have any number appearing more than once?"

def contains_duplicate(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] == 2:
            return True
        pass
    
    return False  # no duplicates found


print(contains_duplicate([1, 2, 3, 4, 5]))  # False