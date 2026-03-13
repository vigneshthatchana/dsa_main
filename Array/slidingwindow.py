arr = [1,2,3,4,5,6,7,8]

k = 3

window_sum = sum(arr[0:3])
max_sum = window_sum

for i in range(k,len(arr):
  window_sum = window_sum - arr[i-k] + arr[i]
  max_sum = max_sum(window_sum,max_sum)
print(max_sum)
