def twopointers(arr,target):
    left = 0
    right = len(arr)-1

    while left < right:
        sum = arr[left] + arr[right]

        if sum == target:
            print(left,right)
            break
        elif sum < target:
            left += 1
        else:
            right -= 1
arr = [1,2,3,4,5]

target = 7

print(twopointers(arr,target))

