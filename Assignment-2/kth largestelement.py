def KthLargestElement(arr, n, k):
    arr.sort()
    return arr[n-k]

arr = [4,2,9,7,5,6,7,1,3]
n = len(arr)
k = 4
x = KthLargestElement(arr, n, k)
print("Kth largest element is ",x)