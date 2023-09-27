# Operating System First Come First Serve Problems Solution Code


print("Write Down the Name Of Process as po, p1, p2... with space separated")
process_list = list(map(str, input().split()))
# print (process_list)
print("Write down the values of Arrival Time with space separated")
arrival_time = list(map(float, input().split()))
print("Write down the values of Execution Time/Burst Time with space separated")
execution_time = list(map(float, input().split()))
dict1 = list(zip(process_list, arrival_time, execution_time))
# sorting the main list
# print (dict1)
l = len(dict1)
for i in range(0, l):
    for j in range(0, l-i-1):
        if(dict1[j][1] > dict1[j+1][1]):

            tempo = dict1[j]
            dict1[j] = dict1[j+1]
            dict1[j+1] = tempo
# print (dict1)
completion_time1 = []
completion_time = []
k = 0

for i, j, k in dict1:
    # print(k)
    completion_time1.append(k)
completion_time.append(completion_time1[0])
for i in range(0, len(completion_time1)-1):
    if(i == 0):
        k = completion_time1[i]+completion_time1[i+1]
        completion_time.append(k)
    else:
        k = completion_time1[i+1]+k
        completion_time.append(k)

arrival_time1 = []
execution_time1 = []
for i, j, k in dict1:
    arrival_time1.append(j)
    execution_time1.append(k)
print("Completion_Time")
print(completion_time)
turn_around_time = []

zip_turn = zip(completion_time, arrival_time1)
for i, j in zip_turn:
    turn_around_time.append(i-j)
print("Turn_Around_Time")
print(turn_around_time)
waiting_time = []
zip_turn = zip(turn_around_time, execution_time1)
for i, j in zip_turn:
    waiting_time.append(i-j)
print("Waiting_Time")
print(waiting_time)
average_waiting_time=sum(waiting_time)/len(waiting_time)
print("Average_Waiting_Time ,average_waiting_time")