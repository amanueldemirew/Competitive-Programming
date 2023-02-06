class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque(list(range(1, n+1)))
        while len(queue) > 1:
            for i in range(k):
                tmp = queue.popleft()
                if i != k-1:
                    queue.append(tmp)
        return queue.popleft()