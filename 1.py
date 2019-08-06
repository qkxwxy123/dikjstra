# -*-coding:utf-8-*-
# 从左上开始，先行后列，按顺序将点编号

while True:
    rows = int(input())
    lines = int(input())
    if rows == 0 and lines == 0:
        break

    # getValue用来存储读取所得每个格子的值
    # parents存储父亲节点
    # processed表示已处理过的点，costs为start到当前点的路径长度
    getValue = []
    parents = {}
    processed = []
    costs = {}

    # graph表示图及各点间的路长
    graph = {}

    for i in range((rows + 1) * (lines + 1) + 1):
        graph[i] = {}

    # 起点是(rows + 1) * lines + 1
    graph[rows * (lines + 1) + 1] = {}
    for i in range(rows):
        gets = []
        for j in range(lines):
            value = int(input())
            gets.append(value)
        getValue.append(gets)

    for i in range(rows):
        for j in range(lines):
            if i >= 1 and j >= 1:
                graph[i * lines + j + 1][i * lines + j + 2] = min(getValue[i][j], getValue[i - 1][j])                   #往右走
                graph[i * lines + j + 1][(i - 1) * lines + j + 1] = min(getValue[i - 1][j], getValue[i - 1][j - 1])     #往上走
                graph[i * lines + j + 1][i * lines + j + 1 - rows] = getValue[i - 1][j]                                 #往右上走
            else:
                graph[i * lines + j + 1][i * lines + j + 2] = getValue[i][j]
                if i >= 1:
                    graph[i * lines + j + 1][(i - 1) * lines + j + 1] = getValue[i - 1][j]
            """if j >= 1:
                graph[(i + 1) * (j + 1)][(i + 1) * (j + 1) + rows + 1] = min(getValue[i][j], getValue[i][j - 1])
            else:
                graph[(i + 1) * (j + 1)][(i + 1) * (j + 1) + rows + 1] = getValue[i][j]"""
            graph[i * lines + j + 1][i * lines + j + 1 + rows + 2] = getValue[i][j]

    for i in range(1, rows + 1, 1):
        graph[(i + 1) * (lines + 1)][i * (lines + 1)] = getValue[rows - 1][lines - 1]

    for j in range(lines):
        graph[rows * (lines + 1) + j + 1][rows * (lines + 1) + j + 2] = getValue[rows - 1][j]
        if j >= 1:
            graph[rows * (lines + 1) + j + 1][rows * (lines + 1) + j - lines] = min(getValue[rows - 1][j],
                                                                                    getValue[rows - 1][j - 1])
        else:
            graph[rows * (lines + 1) + j + 1][rows * (lines + 1) + j - lines] = getValue[rows - 1][j]

    infinity = 999999999
    for i in range(1, (rows + 1) * (lines + 1) + 1, 1):
        costs[i] = int(infinity)
    costs[rows * (lines + 1) - lines] = getValue[rows - 1][0]
    costs[rows * (lines + 1) + 2] = getValue[rows - 1][0]
    costs[rows * (lines + 1) - lines + 1] = getValue[rows - 1][0]
    costs[rows * (lines + 1) + 1] = 0

    for i in range(1, (rows + 1) * (lines + 1) + 1, 1):
        parents[i] = None

    parents[rows * (lines + 1) - lines] = rows * (lines + 1) + 1
    parents[rows * (lines + 1) + 2] = rows * (lines + 1) + 1
    parents[rows * (lines + 1) - lines + 2] = rows * (lines + 1) + 1


    def find_lowest_cost_node(costs):
        lowest_cost = infinity
        lowest_cost_node = None
        # 遍历所有节点
        for node in costs:
            # 该节点没有被处理
            if not node in processed:
                # 如果当前节点的开销比已经存在的开销小，则更新该节点为开销最小的节点
                if costs[node] < lowest_cost:
                    lowest_cost = costs[node]
                lowest_cost_node = node
        return lowest_cost_node


    def dijkstra():
        node = find_lowest_cost_node(costs)
        # 只要有开销最小的节点就循环
        while node is not None:
            # 获取该节点当前开销
            cost = costs[node]
            # 获取该节点相邻的节点
            neighbors = graph[node]
            # 遍历这些相邻节点
            for n in neighbors:
                # 计算经过当前节点到达相邻结点的开销,即当前节点的开销加上当前节点到相邻节点的开销
                new_cost = cost + neighbors[n]
                # 如果计算获得的开销比原本该节点的开销小，更新该节点的开销和父节点
                if new_cost < costs[n]:
                    costs[n] = new_cost
                    parents[n] = node
            # 遍历完毕该节点的所有相邻节点，说明该节点已经处理完毕
            processed.append(node)
            # 去查找下一个开销最小的节点，若存在则继续执行循环，若不存在结束循环
            node = find_lowest_cost_node(costs)
        print(costs[lines + 1])

    dijkstra()
