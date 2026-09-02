class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.heap, num)

            if len(self.heap) > self.k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        # If we have more than k numbers,
        # throw away the smallest
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # Smallest of the k largest = kth largest
        return self.heap[0]

       
