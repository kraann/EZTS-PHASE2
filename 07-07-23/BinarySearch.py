def binarySearch(array, key, start, end):

    while start <= end:
        mid = start + (end - start)//2
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1

array = [4,7,1,3,2,5,6,8,9]

key = 8

result = binarySearch(array, key, 0, len(array)-1)
if result != -1:
    print("Element is present at index:" + str(result))
else:
    print("Not found")
