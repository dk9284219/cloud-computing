class Process:
    def __init__(self, process_id, arrival_time, burst_time, price):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.price = price


# def decimal_binary(num, nbit):
#     res = ""
#     while num != 0:
#         res = string(num % 2) + res
#         num = num/2
#     while len(res) < nbit:
#         res = "0"+res
#     return res


processList = []
maximum = 0
process_selected = 0
# Assumed arrival time = 0
n = int(input("Enter the number of process: "))
for i in range(n):
    b = int(input("Enter the burst time of process {} :".format(i)))
    p = int(input("Enter the price of process {} :".format(i)))
    processList.append(Process(i, 0, b, p))
deadline = int(input("Enter the deadline: "))
for i in range(0, pow(2, n)):
    temp=i
    s = ""
    while i != 0:
        s = str(i % 2) + s
        i = i // 2
    while len(s) < n:
        s = "0" + s
    total_price = 0
    total_burst_time = 0
    for j in range(len(s)):
        if s[j] == "1":
            total_price = total_price + processList[j].price
            total_burst_time = total_burst_time + processList[j].burst_time
            if total_burst_time > deadline:
                break
    if total_price > maximum and total_burst_time <= deadline:
        maximum = total_price
        process_selected = temp
res = ""
while process_selected != 0:
    res = str(process_selected % 2) + res
    process_selected = process_selected//2
while len(res) < n:
    res = "0"+res
print("Processes Selected with maximum profit {}".format(res))


