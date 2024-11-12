from collections import deque

n,k=map(int,input().split())
limit=100001
cnt=[0]*limit
visited=[False]*limit

def bfs(n,k):
    queue = deque()
    queue.append(n)

    while queue:
        n = queue.popleft()
        if n == k:
            return cnt[n]
        if -1 < n*2 < limit and visited[n*2] == False:
            queue.appendleft(n*2)
            cnt[n*2 ]=cnt[n]
            visited[n*2 ] = True
        if -1< n-1 < limit and visited[n-1] == False:
            queue.append(n-1)
            cnt[n-1] = cnt[n] +1
            visited[n-1] = True
        if -1< n+1 < limit and visited[n+1] == False:
            queue.append(n+1)
            cnt[n+1] = cnt[n] +1
            visited[n+1] = True

def bfs2(n, k):
    queue= deque()
    queue.append(n)
    
    while queue:
        
        n = queue.popleft()

        if n == k:
            return cnt[n]
        list = [n*2, n+1, n-1]
        for i in list:
            if(0<= i < limit and visited[i] != True):
                
                if i == list[0]:
                    queue.appendleft(i)
                    cnt[i] = cnt[n]
                else:
                    queue.append(i)
                    cnt[i] = cnt[n] +1
                visited[i] = True
    

print(bfs2(n,k))