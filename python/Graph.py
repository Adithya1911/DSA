import random
class Node:
    def __init__(self, data:int)->None:
        self.data:int=data
        self.visited=False
        self.neighbors=[]


class Graph:
    def __init__(self)->None:
        self.nodes:list[Node]=[]
        self.nodesCount:int=0
        

    def add_node(self, node: Node) -> None:
        """
        Adds a new node to the graph.

        Parameters:
        node (Node): The node to be added to the graph. The node must be an instance of the Node class.

        Returns:
        None: This function does not return any value. It modifies the graph by adding the given node.
        """
        self.nodes.append(node)
        self.nodesCount += 1
    
    def add_edge(self, node1: Node, node2: Node) -> None:
        """
        Adds an edge between two nodes in the graph.

        Parameters:
        node1 (Node): The first node to connect. The node must be an instance of the Node class and exist in the graph.
        node2 (Node): The second node to connect. The node must be an instance of the Node class and exist in the graph.

        Returns:
        None: This function does not return any value. It modifies the graph by adding an edge between the given nodes.

        Raises:
        ValueError: If either of the nodes does not exist in the graph.
        """
        if node1 in self.nodes and node2 in self.nodes:
            node1.neighbors.append(node2)
            node2.neighbors.append(node1)
        else:
            raise ValueError("Both nodes must exist in the graph.")

    
    def create_graph(self) -> None:
        """
        Creates a fully connected graph with nodes and edges based on a random probability.

        This function initializes a list of nodes, creates instances of the Node class, and adds them to the graph.
        It then connects each node to every other node with a probability of 0.5 using the add_edge method.
        The function prints a message indicating the creation of each edge.

        Parameters:
        self (Graph): The instance of the Graph class.

        Returns:
        None: This function does not return any value. It modifies the graph by adding nodes and edges.
        """
        count = self.nodesCount
        Nodes = ['Node' + str(i) for i in range(count)]
        for i in range(count):
            Nodes[i] = Node(i)
            self.nodes.append(Nodes[i])
        for i in range(count):
            for j in range(i + 1, count):
                if random.random() < 0.5:
                    self.add_edge(Nodes[i], Nodes[j])
                    print(f'Added edge between {i} and {j}')

    
    
    def print_nodes(self) -> None:
        """
        Prints all nodes in the graph along with their connected neighbors.

        This function iterates through each node in the graph and prints its data,
        followed by the data of its neighboring nodes.

        Parameters:
        self (Graph): The instance of the Graph class.

        Returns:
        None: This function does not return any value. It only prints the graph's nodes and neighbors.
        """
        for node in self.nodes:
            print(node.data, end=' : ')
            for neighbor in node.neighbors:
                print(neighbor.data, end=' ')
            print()

    

    def depth_first_travesal(self, node: Node) -> None:
        """
        Performs a depth-first traversal of the graph starting from a given node.

        This function uses a stack to explore the graph in a depth-first manner.
        It marks each visited node and prints its data.

        Parameters:
        self (Graph): The instance of the Graph class.
        node (Node): The starting node for the depth-first traversal. The node must be an instance of the Node class and exist in the graph.

        Returns:
        None: This function does not return any value. It only prints the data of the visited nodes during the traversal.
        """
        if node is not None:
            stack: list[Node] = []
            stack.append(node)
            while len(stack) > 0:
                currentNode = stack.pop()
                if not currentNode.visited:
                    print(currentNode.data, end='->')
                    currentNode.visited = True
                    for neighbor in currentNode.neighbors:
                        if neighbor.visited == False:
                            stack.append(neighbor)
                            
            self.reset_nodes()

                            
    def reset_nodes(self) -> None:
        """
        Resets the visited status of all nodes in the graph to False.

        This function iterates through each node in the graph and sets the 'visited' attribute to False.
        This is used to prepare the graph for a new traversal, ensuring that all nodes are considered unvisited.

        Parameters:
        self (Graph): The instance of the Graph class.

        Returns:
        None: This function does not return any value. It modifies the 'visited' attribute of each node in the graph.
        """
        for node in self.nodes:
            node.visited = False
        
def main():
    graph=Graph()
    n=int(input('Enter the number of nodes to be created: '))
    graph.nodesCount=n
    graph.create_graph()
    graph.print_nodes()
   
    print('Depth First Traversal:')  # Example: 0->1->3->2->4
    Nodes=random.sample(graph.nodes,k=graph.nodesCount//2)
    for node in Nodes:
        print(node.data)
        graph.depth_first_travesal(node)
        print()
    


if __name__=='__main__':
    main()