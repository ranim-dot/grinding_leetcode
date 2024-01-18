# The Problem 

242.Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Examples:
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false

# The approach 

I figured out that to be an anagram it needs to have the same chars with the same Frequency so like :
    dict_s={"a":3,"n":1,"g":1,"r":1,"m":1}

So to have an anagram the Dict for string t have to match the dict_s

# Code 

```
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        dict_s={}
        disct_t={}

        # itirating in the two strings to fill the dics with their chars and the values are the occurence of that char
        for ch in s:
            # This means that by default the value of the ch takes 0 else add 1
            dict_s[ch]= dict_s.get(ch,0) +1
        for ch in t:
            disct_t[ch]= disct_t.get(ch,0) +1

        
        # If they don't match it's not an anagram
        if dict_s != disct_t:
             return False
        return True

```

# Let's Track what we doing 

# Example usage:
s = "listen"
t = "silent"

1-Initialization:
    dict_s = {}
    dict_t = {}

2- Counting Characters in String s ("listen"):

    Iterating through characters: "l", "i", "s", "t", "e", "n"
    dict_s = {'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1}

3- Counting Characters in String t ("silent"):

    Iterating through characters: "s", "i", "l", "e", "n", "t"
    dict_t = {'s': 1, 'i': 1, 'l': 1, 'e': 1, 'n': 1, 't': 1}
    Comparison of Dictionaries:

4- dict_s is equal to dict_t, so the function returns True.

