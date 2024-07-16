import heapq

def dijkstra(graph, start, N):
    distances = [float('inf')] * (N + 1)
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances[node]:
            continue
        
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return distances[2:]

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        U, V, B = map(int, input().split())
        weight = A[U-1] + A[V-1] + B
        graph[U].append((V, weight))
        graph[V].append((U, weight))
    
    distances = dijkstra(graph, 1, N)
    
    return ' '.join(map(str, distances))

if __name__ == "__main__":
    print(solve())