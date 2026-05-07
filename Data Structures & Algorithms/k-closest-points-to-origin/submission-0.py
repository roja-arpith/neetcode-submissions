class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # hashmap = {}
        # dist = []

        # for i in range(len(points)):
        #     dist[i] =  sqrt((points[i][0] - 0)^2 - (points[i][1] - 0)^2 )
        #     hashmap[dist[i]] = points[i]

        # heapq.heapify(dist)

        # while len(dist) > k:
        #     heapq.heapop(dist)
        
        # res = []

        # for d in dist:
        #     res.append(hashmap[d])
        
        # return res

        heap = []
        res = []

        for x,y in points:
            dist = x*x + y*y
            heap.append((dist,[x,y]))
        
        heapq.heapify(heap)

        for _ in range(k):
            val = heapq.heappop(heap)[1]
            res.append(val)
        
        return res