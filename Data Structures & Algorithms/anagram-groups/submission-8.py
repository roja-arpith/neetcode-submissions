class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for str in strs:
            key = "".join(sorted(str))

            if key not in hashmap:
                hashmap[key] = []
            
            hashmap[key].append(str)
        
        return list(hashmap.values())

        #sorted() - time complexity - O(k log k)
        #for loop - O(log n)
        #total time complexity - O(n * klog k)