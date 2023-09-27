def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if wt[n - 1] > W:
        return knapSack(W, wt, val, n - 1)
    else:
        return max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1), knapSack(W, wt, val, n - 1))


n = int(input("Enter the number of items:"))
W = int(input("Enter the weight of Knapsack: "))
val = []
wt = []
print("Enter the values of {} items".format(n))
for i in range(n):
    item = int(input())
    val.append(item)
for i in range(n):
    weg = int(input())
    wt.append(weg)
print(knapSack(W, wt, val, n))
