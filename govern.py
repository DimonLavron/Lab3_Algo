def check(vertex):
    global cnt, dict_items, get_vertex

    if not vertex in dict_items:
        dict_items[vertex] = cnt
        get_vertex.append(vertex)
        cnt += 1;

def dfs(i):
    global used, graph, result

    used[i] = True
    for next in graph[i]:
        if not used[next]:
            dfs(next)

    result.append(i)

maxn = 1000005
get_vertex = []
dict_items = dict()
used = [False] * maxn
graph = [[] for i in range(maxn)]
result = []
with open("govern.in", "r") as f:
    cnt = 0
    lines = f.readlines()

    for line in lines:
        vertex1, vertex2 = line.split()
        check(vertex1)
        check(vertex2)
        graph[dict_items[vertex2]].append(dict_items[vertex1])

    for i in range(cnt):
        if not used[i]:
            dfs(i)

with open("govern.out", "w") as f:
    result.reverse()
    for i in result:
        f.write(get_vertex[i]+"\n")
