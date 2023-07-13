def linearSearch(arr, num, key):

    for i in range(0, num):
        if (arr[i] == key):
            return i
    return -1

arr = [2, 4, 0, 1, 9, 5, 7, 8, 4]
key = 1
num = len(arr)
result = linearSearch(arr, num, key)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index:",result)
