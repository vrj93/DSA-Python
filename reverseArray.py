def reverse(nums):
    lower_index = 0
    higher_index = len(nums) - 1

    while lower_index < higher_index:
        nums[lower_index], nums[higher_index] = nums[higher_index], nums[lower_index]

        lower_index += 1
        higher_index -= 1


if __name__ == '__main__':
    n = [1, 3, 5, 8, 11]

    print(n)

    reverse(n)  # reversing the array index

    print(n)

