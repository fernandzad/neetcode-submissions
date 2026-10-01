import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.numbers = nums
        self.k = k
        heapq.heapify(self.numbers)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.numbers, val)
        # 1,2,3,4,5,6
        # k = 5
        # length = 6
        top_k = heapq.nlargest(self.k, self.numbers) # 6,5,4,3,2
        return top_k[-1]
        
