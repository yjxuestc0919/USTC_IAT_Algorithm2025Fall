from backtrace import TaskScheduler

files = ["test1.txt", "test2.txt", "test3.txt"]
for file_name in files:
    with open(file_name, 'r') as f:
        content = f.read().split()
        
        n = int(content[0]) # 任务数 
        k = int(content[1]) # 机器个数 
        task_times = list(map(int, content[2:2+n])) # 各任务时间

    scheduler = TaskScheduler(n, k, task_times)
    best_time, best_layout = scheduler.solve()

    print(f"--- 案例 {file_name} ---")
    print(f"耗费的总时间为：{best_time}") 
    print("调度方案为：", end="\n")
    for i, m_tasks in enumerate(best_layout):
        tasks_str = " ".join(map(str, sorted(m_tasks)))
        print(f"机器{i+1} 分配 {tasks_str}", end="\n") 
    print("\n" + "="*40)
