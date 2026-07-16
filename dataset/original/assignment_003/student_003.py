def binary_search(list1, item):

    start = 0
    end = len(list1) - 1

    while start <= end:

        middle = (start + end) // 2

        if list1[middle] == item:
            return middle

        elif item < list1[middle]:
            end = middle - 1

        else:
            start = middle + 1

    return -1


nums = [10, 20, 30, 40, 50]

result = binary_search(nums, 40)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not present")