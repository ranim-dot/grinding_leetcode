class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = list()
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0) +1
        
        for i in range(k):
            max_key , max_value = max(freq.items(), key=lambda x:x[1])
            numbers.append(max_key)
            freq.pop(max_key)
        
        return numbers