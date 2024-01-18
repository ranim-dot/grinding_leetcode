class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for str in strs:
            sorted_str = sorted(str) 
            ans[tuple(sorted_str)].append(str)
        
        return ans.values()