class Solution:
    # Detect loop: check if we are revisiting a node
    # If all nodes were visited, the graph is connected
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: # empty graph still valid tree -> []
            return True
        visited = set()
        nodes = [[] for i in range(len(edges) + 10)]

        for e in edges:
            a, b = e
            nodes[a].append(b)
            nodes[b].append(a)
        
        ans = True
        def dfs(current, prev): # prev is going to be the last visited node before current
            if current in visited:
                return False
            
            visited.add(current)
            for node in nodes[current]:
                if node != prev:
                    res = dfs(node, current) # at the end of the recursive call we check if we detected a loop
                    if not res: # if we detected a previous False on recursive calls, we return False
                        return False
            return True

        ans = dfs(0, 0)
        return ans and len(visited) == n 
        