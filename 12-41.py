import collections
import heapq
def findCheapestPrice(n,flights, src, dst,K):
    graph = collections.defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    Q = [(0, src, K)]
    vis = [(0, -1)] * n

    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k < 0 or (vis[node][0] <= price and vis[node][1] >= k):
            continue
        vis[node] = (price, k)
        for v, w in graph[node]:
            alt = price + w
            heapq.heappush(Q, (alt, v, k - 1))
    return -1
print(findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0))