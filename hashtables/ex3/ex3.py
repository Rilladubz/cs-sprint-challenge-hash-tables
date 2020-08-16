def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    nums = {}

    for i in range(len(arrays)):
        for num in arrays[i]:
            if num not in nums:
                nums[num] = 1
            else:
                nums[num] += 1

    section = {}

    for each in nums.items():
        if each[1] > 1:
            section[each[0]] = each[0]

    result = [num for num in section]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
