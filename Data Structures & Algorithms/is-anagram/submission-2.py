class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashmap1 = Counter(s)
        hashmap2 = Counter(t)

        return hashmap1 == hashmap2
            