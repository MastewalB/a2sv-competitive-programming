func minimumDiameterAfterMerge(edges1 [][]int, edges2 [][]int) int {
    m, n := len(edges1), len(edges2)
    d1, d2 := getDiameter(edges1), getDiameter(edges2)
    
    halfD1, halfD2 := (d1 + 1) / 2, (d2 + 1) / 2
    
    if m == 0 || n == 0 {
        if m == 0 && n == 0 { return 1 }
        return max(halfD1 + 1, halfD2 + 1) 
    }
    return max(d1, d2,  halfD1 + halfD2 + 1)
}

func getDiameter(edges [][]int) int {
    var dfs func(int) int
    graph := make(map[int][]int)
    visited := make(map[int]bool)

    for _, edge := range edges {
        k, v := edge[0], edge[1]
        graph[k] = append(graph[k], v)
        graph[v] = append(graph[v], k)
    }

    cornerNode := getCornerNode(graph)

    dfs = func(node int) int {
        D := 0
        visited[node] = true
        for _, v := range graph[node] {
            if !visited[v] {
                D = max(D, dfs(v) + 1)
            }
        }
        return D
    }
    diameter := dfs(cornerNode)
    return diameter
}

func getCornerNode(graph map[int][]int) int {
    var dfs func(int, int)
    visited := make(map[int]bool)
    cornerNode, maxCount := 0, 0

    dfs = func(node, count int) {
        count++
        if count > maxCount {
            maxCount = count
            cornerNode = node
        }
        visited[node] = true
        for _, v := range graph[node] {
            if !visited[v] {
                dfs(v, count)
            }
        }
    }
    dfs(cornerNode, 0)
    return cornerNode
}