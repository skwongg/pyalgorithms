def depthfirst(graph, start):
    seen, collected = set(), [start]
    while collected:
        vertex = collected.pop()
        if vertex not in seen:
            seen.add(vertex)
            collected.extend(graph[vertex] - seen)
    return seen




graph = {'E':{'D','C'},
        'A': {'B'},
        'B': {'C'},
        'C' : {'E'}
}


depthfirst(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}
