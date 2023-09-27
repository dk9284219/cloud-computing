def knapsack_approximation(W, wt, val, n, ratio, arr):
    w_sum = 0
    profit = 0
    low = 0
    high = n-1
    for i in range(n-1,0,-1):
        if w_sum <= W:
            key = ratio[i]
            pos = binary_search(arr, low, high, key)
            w_sum = w_sum + wt[pos]
            if w_sum >= W:
                continue
            else:
                profit = profit + val[pos]
    return profit


def binary_search(arr, low, high, key):
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid] == key:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > key:
            return binary_search(arr, low, mid - 1, key)
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, key)
    else:
        # Element is not present in the array
        return -1


def merge_sort(ratio):
    if len(ratio) > 1:
        # Finding the mid of the array
        mid = len(ratio) // 2
        # Dividing the array elements
        L = ratio[:mid]
        # into 2 halves
        R = ratio[mid:]
        # Sorting the first half
        merge_sort(L)
        # Sorting the second half
        merge_sort(R)
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                ratio[k] = L[i]
                i += 1
            else:
                ratio[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            ratio[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            ratio[k] = R[j]
            j += 1
            k += 1


n = int(input("Enter the number of items:"))
W = int(input("Enter the weight of Knapsack: "))
val = []
wt = []
ratio = []
print("Enter the values of {} items".format(n))
for i in range(n):
    item = int(input())
    val.append(item)
print("Enter the weight of {} items".format(n))
for i in range(n):
    weg = int(input())
    wt.append(weg)
for i in range(n):
    r = val[i] // wt[i]
    ratio.append(r)
arr = ratio.copy()
merge_sort(ratio)
print(val)
print(wt)
print(ratio)
print(arr)
res = knapsack_approximation(W, wt, val, n, ratio, arr)
print(res)