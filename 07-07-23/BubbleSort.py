arr=[2,3,4,5,6,7,8,9,0]
n=len(arr)
for i in range(n-1):
    swap=False
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            swap=True
            arr[j],arr[j+1]=arr[j+1],arr[j]
    if swap==False:
        break
print(arr)
