# Sort integer array in asc order that has three possible indexes.

def dutch_national_flag(numbers, pivot=1):
    i = 0
    j = 0
    k = len(numbers) - 1

    while j <= k:
        if numbers[j] < pivot:
            swap(numbers, i, j)
            i = i + 1
            j = j + 1
        elif numbers[j] > pivot:
            swap(numbers, j, k)
            k = k - 1
        else:
            j = j + 1

    return numbers


def swap(num_array, index1, index2):
    num_array[index1], num_array[index2] = num_array[index2], num_array[index1]


if __name__ == '__main__':
    nums = [0, 3, 1, 0, 1, 3, 0, 3, 1, 1]
    print(dutch_national_flag(nums))
