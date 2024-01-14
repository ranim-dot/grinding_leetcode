def longestConsecutive(self, nums: List[int]) -> int:
    numsSet = set(nums)
    longest = 1
    maxi =0
    for n in numsSet:
        if n-1 in numsSet:
            continue
        if n-1 not in numsSet:
            while (n+1) in numsSet:
                longest += 1
                n = n+1
        if longest > maxi:
            maxi = longest
        longest = 1
        
    return maxi