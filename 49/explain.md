# Problem

49. Group Anagrams

    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Example 

    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


# Approach

Although the solution appeared straightforward, I found it somewhat challenging. However, this challenge proved to be a valuable learning experience as it deepened my understanding of dictionaries and introduced me to alternative approaches and thought processes.

The code groups anagrams from a list of strings. It uses a dictionary to store anagrams, where the keys are the sorted characters of each string, and the values are lists of strings that are anagrams. The result is a list of lists, where each inner list contains anagrams.

# Code 
 ```python
    class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            ans = defaultdict(list)
            for str in strs:
                sorted_str = sorted(str) 
                ans[tuple(sorted_str)].append(str)
            
            return ans.values()
 ```
# How it works

Let's go through an example to illustrate how the sorting works in the provided code. Consider the following input list of strings:


    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


The goal is to group anagrams from this list. The code achieves this by sorting the characters of each string and using the sorted representation as a key in a dictionary. Let's step through the process:

1. Initialize an empty dictionary (`ans`) with a default value of an empty list:

   ```python
   ans = defaultdict(list)
   ```

2. Loop through each string in the input list (`strs`):

   ```python
   for str in strs:
   ```

3. Sort the characters of the current string:

   ```python
   sorted_str = sorted(str)
   ```

   For the first iteration with `str = "eat"`, `sorted_str` becomes `['a', 'e', 't']`.

4. Use the sorted string as a key in the dictionary. Convert the sorted string to a tuple since lists cannot be used as dictionary keys:

   ```python
   ans[tuple(sorted_str)].append(str)
   ```

   In the first iteration, this adds an entry to the dictionary with the key `('a', 'e', 't')` and value `["eat"]`.

5. Repeat the process for each string in the input list.

   After processing all strings, the `ans` dictionary would look like this:

   ```python
   {
       ('a', 'e', 't'): ['eat', 'tea', 'ate'],
       ('a', 'n', 't'): ['tan', 'nat'],
       ('b', 'a', 't'): ['bat']
   }
   ```

6. Finally, return the values of the dictionary as a list:

   ```python
   return ans.values()
   ```

   The result is a list of lists, where each inner list contains strings that are anagrams of each other:

   ```python
   [
       ['eat', 'tea', 'ate'],
       ['tan', 'nat'],
       ['bat']
   ]
   ```

In summary, the sorting step ensures that anagrams have the same sorted representation, making it easy to identify and group them together using a dictionary.

