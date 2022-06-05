array = [10, 'Vivek', 45, 76, 121]

print(array[:])

array[1] = 'Kevin'

print(array)

array[1] = 55

print(array)

arrayMax = array[0]

for num in array:
    if num > arrayMax:
        arrayMax = num

print(arrayMax)
