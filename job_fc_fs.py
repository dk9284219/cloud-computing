n= int(input("Enter number person in job: "))
d = dict()

for i in range(n):
    key = "P"+str(i+1)
    a = int(input("Enter arrival time of job"+str(i+1)+": "))
    l = []
    l.append(a)
    d[key] = l

d = sorted(d.items(), key=lambda item: item[1])


print("Process | Arrival | ")
for i in range(n):
      print("   ",d[i][0],"|   ",d[i][1][0],"|    "  )
