# https://leetcode.com/problems/minimum-genetic-mutation/description/

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """

        # construct tree one layer at a time
        # after we get the children for a layer, remove that layer from the bank
        def constructTree(root, nodes, tree_dict):
            # init
            if root in nodes:
                nodes.remove(root)
            parents = [start]
            next_parents = []

            while parents != []:
                for i in parents:
                    for j in getChildren(i, nodes):
                        tree_dict[i].append(j)
                        nodes.remove(j)
                        next_parents.append(j)
                parents = next_parents
                next_parents[:] = []

        # bfs
        def BFS(head, tree, target):
            children = tree[head]
            cchildren = []
            depth = 0

            while True:
                for i in children:
                    if i == target:
                        return depth + 1
                    else:
                        for j in tree[i]:
                            cchildren.append(j)
                if cchildren == []:
                    return -1
                depth += 1
                children = cchildren
                cchildren = []

        def getChildren(parent, potential_children):
            children = []
            for i in potential_children:
                if isChild(i, parent):
                    children.append(i)
            return children

        def isChild(potential_child, parent):
            edit_dist = 0
            for i in range(0,len(potential_child)):
                if potential_child[i] != parent[i]:
                    edit_dist += 1
            if edit_dist == 1: # add to the tree/hashmap
                return True
            else:
                return False

        # tree/hashmap init
        d = {i:[] for i in bank}
        d[start] = []
        constructTree(start, bank, d)

        # do a BFS from the start to find the shortest path
        return BFS(start, d, end)
