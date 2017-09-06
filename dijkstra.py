# Your task is to complete this function
# The function prints V space separated integers where
# the ith integer denote the shortest distance of ith vertex
# from source vertex

def minDist(dist, sptSet, ln):
    mn = 987654321
    mnidx = -1

    for v in range(0, ln):
        if sptSet[v] == False and dist[v] <= mn:
            mn = dist[v]
            mnidx = v
    return mnidx


def dijkstra(graph, ln, s):
    dist = [987654321] * ln
    sptSet = [False] * ln

    dist[s] = 0

    for cnt in range(0, ln - 1):
        u = minDist(dist, sptSet, ln)

        sptSet[cnt] = True

        for v in range(0, ln):
            if not sptSet[v] and graph[u][v] and dist[u] != 987654321 and \
                                    dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    for d in dist:
        print(d, end=' ')