arr = [92,79,93,97,94]

prefix_sum = []
current_sum = 0

for i in range(len(arr)):
    current_sum = arr[i] + current_sum
    prefix_sum.append(current_sum)
print(prefix_sum)