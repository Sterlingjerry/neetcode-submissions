class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num]=0
            freq[num]+=1

        heap = []
        result = []

        for num in freq:
            heapq.heappush(heap, (freq[num], num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        for frequency, number in heap:
            result.append(number)

        return result