def sjf(processes,burst_time):
    n=len(processes)
    waiting_time=[0]*n
    turn_around_time=[0]*n
    burst_remaining=burst_time.copy()
    time=0

    while sum(burst_remaining)>0:
        shortest_idx=-1
        smallest=max(burst_time)+1

        for i in range(n):
            if 0< burst_remaining[i]<smallest:
                smallest=burst_remaining[i]
                shortest_idx=i

            if shortest_idx!= -1:
                time+= burst_remaining[shortest_idx]
                burst_remaining[shortest_idx]=0
                waiting_time[shortest_idx]=time-burst_time[shortest_idx]
                turn_around_time[shortest_idx]=time

    print("SJF Scheduling: ")
    print("processes\tburst_time\twaiting_time\tturn_around_time")

    for i in range(n):
        print(f"{processes[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turn_around_time[i]}")

# Implementation
processes=["P1","P2","P3"]
burst_time=[2,10,7]
sjf(processes,burst_time)