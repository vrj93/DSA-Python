# 1234 -> 4321 reverse integer

def reverse_integer(integer):
    reversed_integer = 0

    while integer > 0:
        remainder = integer % 10
        reversed_integer = reversed_integer * 10 + remainder
        integer = integer // 10  # '//' instead of '/' for division returns integer instead of the exact value.

    return reversed_integer


if __name__ == '__main__':
    print(reverse_integer(123456789))
