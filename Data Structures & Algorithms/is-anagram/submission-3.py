class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # hashmap1 = Counter(s)
        # hashmap2 = Counter(t)

        # return hashmap1 == hashmap2

        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
        

            