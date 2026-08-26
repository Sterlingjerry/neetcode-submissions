class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        longest=0

        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] +=1
            else:
                count[s[right]] = 1

            

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]]-=1
                left+=1
            longest = max(longest, right - left + 1)
        return longest



        