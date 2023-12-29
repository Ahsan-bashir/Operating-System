from collections import deque
def round_robin(processes, burst_time,time_quantum):
    n=len(processes)
    remaining_burst_time=burst_time.copy()
    queue=deque()
    total_time=0

    waiting_time = [0] * n
    while True:
        flag = True
        for i in range(n):
            if remaining_burst_time[i] > 0:
                flag = False
                if remaining_burst_time[i] > time_quantum:
                    total_time += time_quantum
                    remaining_burst_time[i] -= time_quantum
                    queue.append(processes[i])
                else:
                    total_time += remaining_burst_time[i]
                    waiting_time[i] = total_time - burst_time[i]
                    remaining_burst_time[i] = 0
                    queue.append(processes[i])
        if flag:
            break
    print("Round Robin Scheduling: ")
    print("processes\tburst_time\twaiting_time\tturn_around_time")
    for i in range(n):
        print(f"{queue[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{waiting_time[i]+burst_time[i]}")
processes=["P1","P2","P3"]
burst_time=[11,5,8]
time_quantum=2
waiting_time=[0]* len(processes)
round_robin(processes,burst_time,time_quantum)
