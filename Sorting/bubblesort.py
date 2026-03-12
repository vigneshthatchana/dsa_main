def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)
arr = [5,4,3,2,1]
bubblesort(arr)
print("sorted array:",arr)