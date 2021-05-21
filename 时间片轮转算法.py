PCB = [{"进程名":'P1', "到达时间":1, "运行时间":4, "已用CPU时间":0, "进程状态":'W'},\
        {"进程名":'P2', "到达时间":1, "运行时间":2, "已用CPU时间":0, "进程状态":'W'},\
        {"进程名":'P3', "到达时间":1, "运行时间":3, "已用CPU时间":0, "进程状态":'W'},\
        {"进程名":'P4', "到达时间":1, "运行时间":5, "已用CPU时间":0, "进程状态":'W'},\
        {"进程名":'P5', "到达时间":1, "运行时间":6, "已用CPU时间":0, "进程状态":'W'}]
def key():
    for i in range(len(PCB)):
        PCB[i]["进程状态"] = 'R'
        PCB[i]["已用CPU时间"] += 1
        print("***运行进程***")
        if PCB[i]["进程状态"] == 'R':
            print(PCB[i])
        print("***就绪队列***")
        for j in range(len(PCB)):
            if len(PCB) == 1:
                print("      无")
            if PCB[j]["进程状态"] == 'W':
                print(PCB[j])
        print("***阻塞队列***\n      无\n")
        PCB[i]["进程状态"] = 'W'
    return PCB
print("-----------------------基于时间片轮转调度算法-----------------------\n")
k = [[], [], [], [], []]
for i in range(len(PCB)):
        k[i] = PCB[i]["运行时间"] 
q = k.index(min(k))
for i in range(max(k)):
    key()
    for j in range(len(PCB)):
        if len(PCB) == 1:
            print("**********************所有进程结束**************************")
            break
        if PCB[j]["已用CPU时间"] == min(k):
            del PCB[q]
            k.remove(min(k))
            q = k.index(min(k))
            break
