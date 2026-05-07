class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for i in range(len(strs)):
            value = tuple(sorted(strs[i]))

            if value not in hashmap:
                hashmap[value] = []
            
            hashmap[value].append(strs[i])
        
        return list(hashmap.values())