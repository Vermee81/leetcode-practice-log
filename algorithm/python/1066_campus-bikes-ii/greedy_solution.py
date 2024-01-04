class Solution:
    visited = [False] * 10
    min_dist = 10**10

    def get_distance(self, p1: List[int], p2: List[int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def calc_minimum(
        self,
        current_dist: int,
        worker_idx: int,
        workers: List[List[int]],
        bikes: List[List[int]],
    ):
        if worker_idx >= len(workers):
            self.min_dist = min(self.min_dist, current_dist)
            return

        if current_dist >= self.min_dist:
            return

        for i in range(len(bikes)):
            if not self.visited[i]:
                self.visited[i] = True
                self.calc_minimum(
                    current_dist + self.get_distance(workers[worker_idx], bikes[i]),
                    worker_idx + 1,
                    workers,
                    bikes,
                )
                self.visited[i] = False

    def assign_bikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        self.calc_minimum(0, 0, workers, bikes)
        return self.min_dist
