def twopointers(arr,target):
    left = 0
    right = len(arr)

    while left < right:
        sum = arr[left] + arr[right]

        if sum == target:
            print(left,right)
            break
        elif sum < target:
            left += 1
        else:
            right -= 1

