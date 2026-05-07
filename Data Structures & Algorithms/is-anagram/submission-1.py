class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # hashmap1 = Counter(s)
        # hashmap2 = Counter(t)

        # return hashmap1 == hashmap2
        hashmap1 = {}
        hashmap2 = {}

        for i in range(len(s)):
            hashmap1[s[i]] = hashmap1.get(s[i],0) + 1
        
        for i in range(len(t)):
            hashmap2[t[i]] = hashmap2.get(t[i],0) + 1

        return hashmap1 == hashmap2
            