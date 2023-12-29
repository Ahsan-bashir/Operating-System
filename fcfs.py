def fcfs(processes,burst_time):
    n=len(processes)
    waiting_time=[0]*n
    turn_around_time=[0]*n
    waiting_time[0]=0

    for i in range(1,n):
        waiting_time[i]=waiting_time[i-1]+burst_time[i-1]

    for i in range(n):
        turn_around_time

    print("FCFS Scheduling: ")
    print("processes\tburst_time\twaiting_time\tturn_around_time")
    for i in range(n):
        print(f"{processes[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turn_around_time[i]}")

# Implementation
processes=["P1","P2","P3"]
burst_time=[24,3,3]
fcfs(processes,burst_time)