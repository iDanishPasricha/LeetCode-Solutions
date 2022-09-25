class Solution(object):
    def distanceK(self, root, target, K):
        def dfs(node, parent = None):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        

        queue = collections.deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == K:
                return [node.val for node, distance in queue]
            node, distance = queue.popleft()
            for nei in (node.left, node.right, node.parent):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, distance+1))

        return []
    
    
    