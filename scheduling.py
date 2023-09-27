n = int(input())
arr = []
waitt = 0
compt = 0
turnt = 0
res = {}
while(n>0):
    n-=1
    temp = int(input())
    arr.append(temp)
    res[temp] = {}
arr.sort()
for i in range(len(arr)):
    
    res[arr[i]]['turnAroundTime'] = waitt+arr[i]
    res[arr[i]]['waitTime'] = waitt
    res[arr[i]]['completionTime'] = waitt+arr[i]
    waitt += arr[i]
    compt += compt+waitt+arr[i]
    turnt += turnt+waitt+arr[i]
waitt = waitt/len(arr)
compt = compt/len(arr)
turnt = turnt/len(arr)
print(res)
print("avg turn around time = ",waitt)
print("avg completion time = ",compt)
print("avg ait time = ",turnt)
