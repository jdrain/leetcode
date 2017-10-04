# https://leetcode.com/problems/minimum-genetic-mutation/description/
# second Solution

def findMutationDistance(start, end, bank):

    # helper method
    def isChild(potential_child, parent):
        if editDistance(potential_child, parent) == 1: # add to the tree/hashmap
            return True
        else:
            return False

    # helper
    def editDistance(node1, node2):
        edit_dist = 0
        for i in range(0,len(node1)):
            if node1[i] != node2[i]:
                edit_dist += 1
        return edit_dist

    # main algorithm
    depth = 0
    current_nodes = [start]
    next_nodes = []
    while True:
        for n in current_nodes:
            if n == end:
                return depth+1
            for b in bank:
                if isChild(b, n):
                    next_nodes.append(b)
                    bank.remove(b)
        if not next_nodes:
            break
        else:
            current_nodes = next_nodes[:]
            next_nodes = []
            depth += 1
    return -1
