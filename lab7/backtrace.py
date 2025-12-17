class TaskScheduler:
    def __init__(self, n, k, task_times):
        self.n = n # 任务数 
        self.k = k # 机器数 
        # 记录任务耗时并保留原始编号（从1开始） 
        self.tasks = sorted([(t, i+1) for i, t in enumerate(task_times)], reverse=True)
        self.machines = [0] * k
        self.machine_tasks = [[] for _ in range(k)]
        self.best_time = float('inf')
        self.best_layout = []

    def solve(self):
        self._backtrack(0)
        return self.best_time, self.best_layout

    def _backtrack(self, idx):
        # 剪枝：当前最大负载已超已知最优解，跳出该分支 
        if max(self.machines) >= self.best_time:
            return

        # 递归出口：所有任务分配完毕 
        if idx == self.n:
            self.best_time = max(self.machines)
            self.best_layout = [list(m) for m in self.machine_tasks]
            return

        time, original_id = self.tasks[idx]
        tried_loads = set() # 同层去重剪枝
        
        for i in range(self.k):
            # 剪枝：如果多台机器负载相同，尝试其中一台即可
            if self.machines[i] in tried_loads:
                continue
            tried_loads.add(self.machines[i])
            
            # 尝试分配
            self.machines[i] += time
            self.machine_tasks[i].append(original_id)
            
            self._backtrack(idx + 1)
            
            # 回溯还原
            self.machine_tasks[i].pop()
            self.machines[i] -= time

            if self.machines[i] == 0:
                break