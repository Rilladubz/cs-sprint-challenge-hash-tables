def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    nums = {}

    for each in a:
        altered_int = abs(each)
        if altered_int not in nums:
            nums[altered_int] = 1
        else:
            nums[altered_int] += 1

    duplicate_nums = [num for num in nums if nums[num] > 1]

    return duplicate_nums


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
