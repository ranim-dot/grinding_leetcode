# Grinding Leetcode

## December 28, 2023
On Days 2 and 3, I faced some difficulties, but the journey was rewarding as I delved into new concepts. I struggled with [specific concept/problem], but the experience deepened my understanding.

**Reflective Analysis:**
- Learned about Dictionary and Sets.
- Explored new problem-solving techniques.

## December 29, 2023
Day 4 marked a significant milestone as I independently solved a challenging problem. The sense of accomplishment boosted my confidence.

**Code Explanation:**
- Implemented a dictionary to count the frequencies of elements in the input list.
- Utilized a dictionary for efficiency.

**Thought Process:**
- Considered alternative solutions, such as we can use a max heap to efficiently find the k most frequent elements. This alternative approach has a time complexity of O(n log k) instead of O(n log n), which can be more efficient when k is much smaller than n.
  ```python
    import heapq
    from typing import List

    class Solution:
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
          freq = {}
        
          # Count the frequency of each number
          for num in nums:
              freq[num] = freq.get(num, 0) + 1
        
          # Use a max heap to get the k most frequent elements
          max_heap = [(-count, num) for num, count in freq.items()]
          heapq.heapify(max_heap)
        
          # Extract the k most frequent elements from the max heap
          result = []
          for _ in range(k):
              result.append(heapq.heappop(max_heap)[1])
        
          return result
  ```

  **Future Goals:**
- Plan to tackle more problems related to Dictionaries and List in python.
- Explore advanced algorithms such as HeapQueue.

## December 31, 2023
Days 5 and 6 brought about moments of impostor syndrome, but I managed to navigate through the challenges. This experience reinforced the importance of perseverance.

**Thought Process:**
- Faced impostor syndrome; acknowledged and managed it.
- Realized the value of persistence and self-confidence.

**Acknowledgments:**
I faced difficulty with finding the optimal approach, but I'm proud of my efforts in understanding and overcoming it.


