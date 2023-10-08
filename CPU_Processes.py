import copy

class Process:
    # ML

    algorithms = {}
    colET = 3  # default column number of Ending Time
    colTAT = 4  # default column number of Turnaround Time
    QT = None

    prio_check = False
    multi_check = False

    def __init__(self, *algos):
        if len(algos) > 1:
            self.colET += 1
            self.colTAT += 1
            self.multi_check = True
        for idx, algo in enumerate(algos):
            self.algorithms[idx + 1] = algo
            if not self.prio_check and "Priority" in algo:
                self.colET += 1
                self.colTAT += 1
                self.prio_check = True
        # print(f"colET: {self.colET}")
        # print(f"colTAT: {self.colTAT}")

    time = 0
    queue = []

    # processes_list = [
    #     ["P1", 10, 5, 2],
    #     ["P2", 8, 4, 1],
    #     ["P3", 12, 4, 1],
    #     ["P4", 3, 3, 2],
    #     ["P5", 15, 5, 2]
    # ]

    # processes_list = [
    #     ["P1", 3, 6],
    #     ["P2", 8, 4],
    #     ["P3", 0, 7],
    #     ["P4", 12, 3],
    #     ["P5", 16, 5],
    #     ["P6", 5, 2],
    #     ["P7", 18, 7],
    #     ["P8", 10, 8],
    #     ["P9", 2, 1],
    #     ["P10", 14, 9]
    # ]

    # With Priority
    processes_list = [
        ["P1", 3, 4, 2],
        ["P2", 5, 9, 1],
        ["P3", 8, 4, 2],
        ["P4", 0, 7, 1],
        ["P5", 12, 6, 1]
    ]

    # processes_list = [
    #     ["P1", 3, 4, 2, 1],
    #     ["P2", 5, 9, 1, 1],
    #     ["P3", 8, 4, 2, 2],
    #     ["P4", 0, 7, 1, 2],
    #     ["P5", 12, 6, 1, 1]
    # ]

    # processes_list = [
    #     ["P1", 3, 4, 2, 1],
    #     ["P2", 5, 9, 1, 1],
    #     ["P3", 8, 4, 2, 2],
    #     ["P4", 0, 7, 1, 2],
    #     ["P5", 12, 6, 1, 1],
    #     ["P6", 5, 2, 1, 3],
    #     ["P7", 18, 7, 2, 3],
    #     ["P8", 10, 8, 1, 1],
    #     ["P9", 2, 1, 2, 3],
    #     ["P10", 14, 9, 1, 3]
    # ]

    # processes_list = [
    #     ["P1", 3, 4, 1],
    #     ["P2", 5, 9, 1],
    #     ["P3", 8, 4, 2],
    #     ["P4", 0, 7, 2],
    #     ["P5", 12, 6, 1]
    # ]

    # processes_list = [
    #     ["P1", 10, 5],
    #     ["P2", 8, 4],
    #     ["P3", 12, 4],
    #     ["P4", 3, 3],
    #     ["P5", 15, 5]
    # ]

    # processes_list = [
    #     ["P1", 10, 1, 1],
    #     ["P2", 9, 2, 2],
    #     ["P3", 12, 4, 2],
    #     ["P4", 4, 3, 1],
    #     ["P5", 40, 5, 1],
    #     ["P6", 21, 6, 1],
    #     ["P7", 21, 6, 1]
    # ]

    if multi_check and prio_check:
        plist = sorted(copy.deepcopy(processes_list), key=lambda x: (x[1], x[4], x[3], x[2], x[0]))
    elif multi_check or prio_check:
        plist = sorted(copy.deepcopy(processes_list), key=lambda x: (x[1], x[3], x[2], x[0]))
    else:
        plist = sorted(copy.deepcopy(processes_list), key=lambda x: (x[1], x[2], x[0]))

    # for sublist in plist:
    #     print(sublist)

    timestamps = [0]
    orderOfProcesses = []
    min_process = None

    def displayGanttChart(self):
        print("Gantt Chart:")
        print("| ", end="")
        for i in self.orderOfProcesses:
            print(f"{i: >5} | ", end="")
        print()
        for i in self.timestamps:
            print(f"{i: <8}", end="")

    def calculateTable(self):
        for i in range(len(self.processes_list)):
            # Calculating turnaround time
            self.processes_list[i].append(self.processes_list[i][self.colET] - self.processes_list[i][1])
            # Calculating waiting time
            self.processes_list[i].append(self.processes_list[i][self.colTAT] - self.processes_list[i][2])

    def displayTable(self):
        print()
        print("Table:")
        print(f"{'Process': >10} | ", end="")
        print(f"{'Arrival': >10} | ", end="")
        print(f"{'Burst': >10} | ", end="")
        if self.prio_check:
            print(f"{'Priority': >10} | ", end="")
        if self.multi_check:
            print(f"{'Level': >10} | ", end="")
        print(f"{'Ending': >10} | ", end="")
        print(f"{'Turnaround': >10} | ", end="")
        print(f"{'Waiting': >10} | ")
        for sublist in self.processes_list:
            for i in sublist:
                print(f"{i: >10} | ", end="")
            print()

    def displayEfficiency(self):
        print("CPU Utilization: ", end="")
        total = 0
        for i in range(len(self.processes_list)):
            total += self.processes_list[i][2]
        print(f"{round(total / self.timestamps[-1] * 100, 2)}%")

        print("Average Turnaround Time: ", end="")
        total = 0
        for i in range(len(self.processes_list)):
            total += self.processes_list[i][self.colTAT]
        print(total / len(self.processes_list))

        print("Average Waiting Time: ", end="")
        total = 0
        for i in range(len(self.processes_list)):
            total += self.processes_list[i][self.colTAT + 1]
        print(total / len(self.processes_list))

    def displayQueue(self):
        print()
        for sublist in self.queue:
            print(sublist)

