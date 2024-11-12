#**************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9370                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: supporting130870 <boj.kr/u/supporting1308   +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9370                           #+#        #+#      #+#     #
#    Solved: 2024/11/12 11:44:16 by supporting1308###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 다익스트라 알고리즘 함수
def dijkstra(s, n, graph):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        dist, current = heapq.heappop(q)
        if distance[current] < dist:
            continue
        for i in graph[current]:
            cost = dist + i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

# 입력 처리
T = int(input().strip())
results = []
for _ in range(T):
    # 교차로 수, 도로 수, 목적지 후보 수
    n, m, t = map(int, input().split())
    # 출발지, 반드시 지나야 하는 두 교차로
    s, g, h = map(int, input().split())

    # 그래프 초기화
    graph = [[] for _ in range(n + 1)]

    # 도로 정보 입력
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))  # 양방향 도로

    # 목적지 후보 입력
    destinations = []
    for _ in range(t):
        destinations.append(int(input().strip()))

    # 다익스트라로 최단 거리 계산
    dist_from_s = dijkstra(s, n, graph)
    dist_from_g = dijkstra(g, n, graph)
    dist_from_h = dijkstra(h, n, graph)

    # 결과 후보 찾기
    result = []
    for dest in destinations:
        through_g_h = dist_from_s[g] + dist_from_g[h] + dist_from_h[dest]
        through_h_g = dist_from_s[h] + dist_from_h[g] + dist_from_g[dest]
        if dist_from_s[dest] == min(through_g_h, through_h_g):
            result.append(dest)

    # 오름차순 출력
    result.sort()
    results.append(result)

for i in results:
    print(" ".join(map(str, i)))
