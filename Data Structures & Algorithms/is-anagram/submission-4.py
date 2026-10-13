class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap1 = Counter(s)
        hashmap2 = Counter(t)

        if hashmap1 == hashmap2 :
            return True
        
        return False
        