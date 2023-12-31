#    1-----2
#  /  \     \
#  3   \     7
# |  \  \  / |
# 4---5   8  6

#예제5-5 DFS
#1. 시작노드 '1'부터! 스택에 '1' 삽입
#2. '1'과 인접 노드는 '2','3','8'. 이중 가장 작은 노드 '2' 삽입
#3. '2'와 인접한 '7' 삽입
#4. '7'과 인접 노드는 '8','6'. 이중 작은 노드 '6' 삽입
#5. '6'과 인접한 노드 없음. 따라서 '6' 삭제
#6. '7'과 인접 노트 '8' 삽입
#7. '8'과 인접한 노드 없음. 따라서 '8' 삭제
#8. 현재 스택의 최상단 '7', 인접노드 없음. 따라서 '7' 삭제
#9. 현재 스택의 최상단 '2', 인접노드 없음. 따라서 '2' 삭제
#10. 현재 스택의 최상단 '1', 방문하지 않은 인접 노드는 '3', '3' 삽입
#11. '3'과 인접 노드는 '4','5'. 이중 작은 노드 '4' 삽입
#12. '4'와 인접한 노드 '5' 삽입
#13. 남아 있는 노드에 방문하지 않은 인접 노드 없음. 따라서 남아있는 모든 노드를 차례대로 꺼냄. 5,4,3,1

#결론: 노드의 탐색순서(스택에 넣은 순서)
# 1 -> 2 -> 7 -> 6 -> 8 -> 3 -> 4 -> 5

def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

DFS(graph, 1, visited)