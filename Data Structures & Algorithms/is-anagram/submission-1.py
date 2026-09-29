class Solution:
    # The idea here is sort the words
    # After sorting we compare them
    # This O (n log n) but we can improve

    # We can count the total or letters and check if
    # The amount of each letter is the same for the two words
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for c in s:
            if s_dict.get(c) == None:
                s_dict[c] = 1
            else:
                s_dict[c] = s_dict.get(c) + 1
        for c in t:
            if t_dict.get(c) == None:
                t_dict[c] = 1
            else:
                t_dict[c] = t_dict.get(c) + 1
        result = True
        for c in s:
            if s_dict.get(c) != t_dict.get(c):
                result = False
                break
        return result
        