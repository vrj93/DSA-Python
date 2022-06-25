# Trapped Rain water problem

def trapped_rain_water_problem(height):

    if len(height) < 3:
        return 0

    left_max = [0 for _ in range(len(height))]
    right_max = [0 for _ in range(len(height))]

    # left max value
    for i in range(1, len(height)):
        left_max[i] = max(left_max[i - 1], height[i - 1])

    # right max value
    for i in range(len(height) - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i + 1])

    # calculating the trapped water
    trapped = 0

    for i in range(1, len(height) - 1):
        if min(left_max[i], right_max[i]) > height[i]:
            trapped += min(left_max[i], right_max[i]) - height[i]

    return trapped


if __name__ == '__main__':
    print(trapped_rain_water_problem([1, 0, 2, 1, 3, 1, 2, 0, 3]))

