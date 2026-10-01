import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.numbers = nums
        self.k = k
        heapq.heapify(self.numbers)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.numbers, val)
        # 7
        # k = 1
        # length = 1
        top_k = heapq.nlargest(self.k, self.numbers) # 1
        return top_k[-1]
        
