class TreeNode:
    def __init__(self,data:str) -> None:
        self.data:str =data
        self.left_child:TreeNode = None
        self.right_child:TreeNode = None
    
def depth_first_Traversal(node: TreeNode) -> list[str]:
    """
    Perform a depth-first traversal on a binary tree and return a list of node data in the order they were visited.

    Parameters:
    node (TreeNode): The root node of the binary tree to perform the depth-first search on.
        The TreeNode class should have the following attributes:
        - data: The data stored in the node.
        - left_child: The left child node.
        - right_child: The right child node.

    Returns:
    list[str]: A list of node data in the order they were visited during the depth-first search.
    """
    if node is not None:
        left_values: list[str] = depth_first_Traversal(node.left_child)
        right_values: list[str] = depth_first_Traversal(node.right_child)
        return [node.data] + left_values + right_values
    return []


# res:list[str]=depth_first_Traversal(a)
# print(res) # ['A', 'B', 'D', 'E', 'C', 'F']

def breadth_first_Traversal(node: TreeNode) -> list[str]:
    """
    Perform a breadth-first search on a binary tree and return a list of node data in the order they were visited.

    Parameters:
    node (TreeNode): The root node of the binary tree to perform the breadth-first search on.
        The TreeNode class should have the following attributes:
        - data: The data stored in the node.
        - left_child: The left child node.
        - right_child: The right child node.

    Returns:
    list[str]: A list of node data in the order they were visited during the breadth-first search.
    """
    queue: list[TreeNode] = []
    result: list[str] = []
    queue.append(node)
    while len(queue) > 0:
        newNode: TreeNode = queue.pop(0)
        result.append(newNode.data)
        if newNode.left_child is not None:
            queue.append(newNode.left_child)
        if newNode.right_child is not None:
            queue.append(newNode.right_child)
    return result

# res:list[str]=breadth_first_Traversal(a)
# print(res)# A B C D E F

def depth_first_search(root:TreeNode,target_value:str)->bool:
    """
    Perform a depth-first search on a binary tree to find a target value.

    Parameters:
    root (TreeNode): The root node of the binary tree to perform the depth-first search on.
        The TreeNode class should have the following attributes:
        - data: The data stored in the node.
        - left_child: The left child node.
        - right_child: The right child node.
    target_value (str): The value to search for in the binary tree.

    Returns:
    bool: A boolean value indicating whether the target value was found in the binary tree.
    """
    if root is not None:
        if root.data==target_value:
            return True
        left_search:bool=depth_first_search(root.left_child,target_value)
        if left_search:return True
        right_search:bool=depth_first_search(root.right_child,target_value)
        return left_search or right_search
    return False

# print(depth_first_search(a, "J")) # True

def breadth_first_search(root:TreeNode,target_value:str)->bool:
    """
    Perform a breadth-first search on a binary tree to find a target value.

    Parameters:
    root (TreeNode): The root node of the binary tree to perform the breadth-first search on.
        The TreeNode class should have the following attributes:
        - data: The data stored in the node.
        - left_child: The left child node.
        - right_child: The right child node.
    target_value (str): The value to search for in the binary tree.

    Returns:
    bool: A boolean value indicating whether the target value was found in the binary tree.
    """
    if root:
        queue:list[TreeNode]=[]
        queue.append(root)
        while len(queue)>0:
            current_node:TreeNode=queue.pop(0)
            if current_node.data==target_value:return True
            if current_node.left_child:queue.append(current_node.left_child)
            if current_node.right_child:queue.append(current_node.right_child)
    return False

# print(breadth_first_search(a, "E")) # False

def tree_sum(root:TreeNode)->int:
    """
    Calculate the sum of all the nodes in a binary tree.

    Parameters:
    root (TreeNode): The root node of the binary tree to calculate the sum of.
        The TreeNode class should have the following attributes:
        - data: The data stored in the node.
        - left_child: The left child node.
        - right_child: The right child node.

    Returns:
    int: The sum of all the nodes in the binary tree.
    """
    if root is not None:
        left_sum:int=tree_sum(root.left_child)
        right_sum:int=tree_sum(root.right_child)
        return int(ord(root.data)-64)+left_sum+right_sum
    return 0


def tree_inorder_traversal(root: TreeNode) -> list[str]:
    """
    Perform an in-order traversal on a binary tree and return a list of node data in the order they were visited.

    Parameters:
    root (TreeNode): The root node of the binary tree to perform the in-order traversal on.
        The TreeNode class should have the following attributes:
        - data: The data stored in the node.
        - left_child: The left child node.
        - right_child: The right child node.

    Returns:
    list[str]: A list of node data in the order they were visited during the in-order traversal.
    If the root node is None, an empty list is returned.
    """
    if root:
        return tree_inorder_traversal(root.left_child) + [root.data] + tree_inorder_traversal(root.right_child)
    return []


def tree_post_order_traversal(root: TreeNode) -> list[str]:
    """
    Perform a post-order traversal on a binary tree and return a list of node data in the order they were visited.

    Parameters:
    root (TreeNode): The root node of the binary tree to perform the post-order traversal on.
        The TreeNode class should have the following attributes:
        - data: The data stored in the node.
        - left_child: The left child node.
        - right_child: The right child node.

    Returns:
    list[str]: A list of node data in the order they were visited during the post-order traversal.
    If the root node is None, an empty list is returned.
    """
    if root:
        return tree_post_order_traversal(root.left_child) + tree_post_order_traversal(root.right_child) + [root.data]
    return []

def tree_pre_order_traversal(root: TreeNode) -> list[str]:
    """
    Perform a pre-order traversal on a binary tree and return a list of node data in the order they were visited.

    Parameters:
    root (TreeNode): The root node of the binary tree to perform the pre-order traversal on.
        The TreeNode class should have the following attributes:
        - data: The data stored in the node.
        - left_child: The left child node.
        - right_child: The right child node.

    Returns:
    list[str]: A list of node data in the order they were visited during the pre-order traversal.
    """
    if root:
        return [root.data] + tree_pre_order_traversal(root.left_child) + tree_pre_order_traversal(root.right_child)
    return []


def main():
    # Intializing the tree nodes    
    a:TreeNode=TreeNode("A")
    b:TreeNode=TreeNode("B")
    c:TreeNode=TreeNode("C")
    d:TreeNode=TreeNode("D")
    e:TreeNode=TreeNode("E")
    f:TreeNode=TreeNode("F")
    
    # Creating the tree structure
    a.left_child=b     #            a
    a.right_child=c    #           / \
    b.left_child=d     #          b   c
    b.right_child=e    #         / \   \    
    c.right_child=f    #        d   e   f
    
    print(f'Depth First Traversal: {depth_first_Traversal(a)}')
    print(f'Breadth First Traversal: {breadth_first_Traversal(a)}')
    print(f'Depth First Search of J in Tree: {depth_first_search(a,"J")}')
    print(f'Breadth First Search of E in Tree: {breadth_first_search(a,"E")}')
    print(f'Tree Sum of Tree: {tree_sum(a)}')
    print(f'Inorder Traversal: {tree_inorder_traversal(a)}')
    print(f'Postorder Traversal: {tree_post_order_traversal(a)}')
    print(f'Preorder Traversal: {tree_pre_order_traversal(a)}')
    


if __name__ == "__main__":
    main()
    





