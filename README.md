# Grinding Leetcode

## Just for clarifation :
**`The folder names represents the number of the problem solved`**

## December 28, 2023
On Days 2 and 3, I faced some difficulties, but the journey was rewarding as I delved into new concepts. I struggled with Sets, Dictionaries, and Slicing, but the experience deepened my understanding.

**Reflective Analysis:**
- Learned about Dictionary and Sets.
- Explored new problem-solving techniques.

## December 29, 2023
Day 4 marked a significant milestone as I independently solved a challenging problem. The sense of accomplishment boosted my confidence.

**Code Explanation:**
- Implemented a dictionary to count the frequencies of elements in the input list.
- Utilized a dictionary for efficiency.

**Thought Process:**
- Considered alternative solutions, such as using a max heap to efficiently find the k most frequent elements. This alternative approach has a time complexity of O(n log k) instead of O(n log n), which can be more efficient when k is much smaller than n.
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

## January 2, 2024
On the first day of the new year, I took on the Sudoku problem, venturing into new territory by using `collections.defaultdict` for the first time. The challenge was significant, testing my understanding of the rules governing a Sudoku board. Although impostor syndrome lurked in the background, I didn't let it deter me.

**Code Explanation:**
- Utilized `collections.defaultdict` to efficiently track numbers in each row, column, and sub-box of the Sudoku board.
- Iterated through each cell, checking for repetitions based on Sudoku rules.

**Thought Process:**
- First encounter with `collections.defaultdict` and its usefulness in efficiently handling the Sudoku problem.
- Successfully navigated through the challenge, demonstrating resilience and problem-solving skills.

**Future Goals:**
- Explore more problems that involve the usage of advanced data structures in Python.
- Build confidence in handling complex problems that demand a deeper understanding of algorithms and data structures.

## *From january 2nd i took a break so i complete my final exams and i'll be back to grinding the 13rd of january*

## 13/14 January, 2024

After a two-week break, I returned to problem-solving, and it felt refreshing to delve back into coding challenges.

**Thought Process:**

Initially, I misunderstood the problem, interpreting it as requiring the identification of consecutive numbers with a consistent difference, such as 100, 200, 300. However, after contemplating the problem and attempting to solve it based on this misunderstanding, I realized that the true definition of consecutive numbers was those with a difference of 1, like 99, 100, 101.

Upon this realization, I adjusted my approach accordingly and successfully solved the problem. It was a valuable learning experience, highlighting the importance of thoroughly understanding the problem statement before attempting to devise a solution.

## 15 Jannuary, 2024

I solved two problems about the concept of Stack that will be shared tomorrow

## 16 jannuary, 2024

**Explanation of Code:**

The MinStack algorithm is designed to create a stack with standard methods such as pop, push, and top, while also incorporating the capability to retrieve the minimum element in the stack. The challenge was to maintain a time complexity of O(1).

The concept of ValidParentheses is akin to one of my recent algorithms.

As for the Evaluation of Reverse Polish Notation, it's a novel concept for me, as I had not encountered it before, but solving it proved to be straightforward.

the concept of RPN :

![Reverse_Polish_Notation_Stack_Example](https://github.com/ranim-dot/grinding_leetcode/assets/69695069/bdff695d-480d-4e7c-a375-dbf9c3f89239)

## January 17, 2024

**Approach:**

Initially, solving this problem proved time-consuming as understanding the conditions took a considerable amount of time. However, the implementation became challenging, prompting me to seek additional resources. It became evident that the solution required the application of a concept called "Backtracking."

**Confusion:**

I had not delved into the realm of backtracking in my studies. Its algorithms prove useful in various scenarios, particularly when dealing with problems that require finding combinations, such as the one I was tackling. Backtracking operates on the principle of recursion.

**Future Goals:**

My upcoming objectives involve acquiring a deeper understanding of backtracking. I aim to explore its algorithms further and grasp its applications, especially in problem-solving scenarios that demand the generation of combinations.

