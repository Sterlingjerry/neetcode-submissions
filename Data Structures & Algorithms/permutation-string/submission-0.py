class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        window = {}

        for char in s1:
            if char in need:
                need[char] += 1
            else:
                need[char] = 1

        left = 0

        for right in range(len(s2)):
            char = s2[right]

            if char in window:
                window[char] += 1
            else:
                window[char] = 1

            if right - left + 1 > len(s1):
                left_char = s2[left]

                window[left_char] -= 1

                if window[left_char] == 0:
                    del window[left_char]

                left += 1

            if window == need:
                return True

        return False

        