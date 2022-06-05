# def palindrome_python(s):
#     reverse_string = s[::-1]
#
#     if s == reverse_string:
#         return True
#
#     return False


def reverse(string):
    data = list(string)
    lower_index = 0
    higher_index = len(data) - 1

    while lower_index < higher_index:
        data[lower_index], data[higher_index] = data[higher_index], data[lower_index]

        lower_index += 1
        higher_index -= 1

    return ''.join(data)


def is_palindrome(string):
    reverse_string = reverse(string)

    if string == reverse_string:
        return True

    return False


if __name__ == '__main__':
    print(is_palindrome('radar'))
