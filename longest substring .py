class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = "abcabcbb"
        substring = {}
        curr_sub_start = 0
        curr_len = 0
        longest = 0
        
        for i, letter in enumerate(s):
            if letter in substring and substring[letter] >= curr_sub_start:
                curr_sub_start = substring[letter] + 1
                curr_len = i - substring[letter]
                substring[letter] = i
            else:
                substring[letter] = i
                curr_len += 1
                if curr_len > longest:
                    longest = curr_len
        return longest