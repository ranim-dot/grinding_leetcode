class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        dict_s={}
        disct_t={}

        # itirating in the two strings to fill the dics with their chars and the values are the occurence of that char
        for ch in s:
            dict_s[ch]= dict_s.get(ch,0) +1
        for ch in t:
            disct_t[ch]= disct_t.get(ch,0) +1

        
        # If they don't match it's not an anagram
        if dict_s != disct_t:
             return False
        return True

