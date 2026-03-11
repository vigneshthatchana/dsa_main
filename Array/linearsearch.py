def linearsearch(array,target):
    for i in range(0, len(array)):
        if array[i] == target:
            print(f"Target found at the index: {i}")
            break
    else:
        print("Target doesn't exist in the list")

array = [1,2,3,4,5,6,7,8,9,10]
target = 10

print(linearsearch(array,target))
