class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1

        heap = []
        result = []

        for number, frequency in freq.items():
            heapq.heappush(heap, (frequency, number))

            if len(heap)> k:
                heapq.heappop(heap)

        for freq, num in heap:
            result.append(num)

        return result

        