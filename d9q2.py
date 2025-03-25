#Day9Q18: 
def findClosestElements(arr, k, x):
    left, right = 0, len(arr) - 1
    while right - left >= k:
        if abs(arr[left] - x) > abs(arr[right] - x):
            left += 1
        else:
            right -= 1
    return arr[left:left + k]

print(findClosestElements([1, 2, 3, 4, 5], 4, 3))  
print(findClosestElements([1, 1, 2, 3, 4, 5], 4, -1))