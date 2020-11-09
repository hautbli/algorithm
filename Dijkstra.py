import heapq


def dijkstra(start, graph):
    n = len(graph)
    heap = []
    distances = [float('inf')] * n

    heapq.heappush(heap, (0, start))

    print(heapq.heappop(heap))
    #
    # for i in range(n):
    #     heapq.heappush(heap, graph[i][0])
    #     heapq.heappush(heap, graph[i][1])

    heapq.heappush(heap, graph[0][0])
    heapq.heappush(heap, graph[0][1])

    print(heapq.heappop(heap))
    print(heap)



graph = [[(2, 5), (3, 2)],  # (인접노드, 가중치)
         [(3, 5), (4, 3)],
         [(0, 3), (4, 9)],
         [(0, 10), (4, 2)],
         [(2, 13), (1, 3)]]

print(dijkstra(0, graph))

