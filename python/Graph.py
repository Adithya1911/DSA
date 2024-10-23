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
        
    def add_node(self,node:Node)->None:
        self.nodes.append(node)
        self.nodesCount+=1
    
    def add_edge(self,node1:Node,node2:Node)->None:
        if node1 in self.nodes and node2 in self.nodes:
            node1.neighbors.append(node2)
            node2.neighbors.append(node1)
        else:
            raise ValueError("Both nodes must exist in the graph.")
    
    def create_graph(self)->None:
        count=self.nodesCount
        Nodes=['Node'+str(i) for i in range(count)]
        for i in range(count):
            Nodes[i]=Node(i)
            self.nodes.append(Nodes[i])
        for i in range(count):
            for j in range(i+1,count):
                if random.random()<0.5:
                    self.add_edge(Nodes[i],Nodes[j])
                    print(f'Added edge between {i} and {j}')
    
    
    def print_nodes(self)->None:
        for node in self.nodes:
            print(node.data,end=' : ')
            for neighbor in node.neighbors:
                print(neighbor.data,end=' ')
            print()
    

    def depth_first_travesal(self,node:Node):
        
        if node is not None:
            stack:list[Node]=[]
            stack.append(node)
            while len(stack)>0:
                currentNode=stack.pop()
                if not currentNode.visited:
                    print(currentNode.data,end='->')
                    currentNode.visited=True
                    for neighbor in currentNode.neighbors:
                        if neighbor.visited==False:
                            stack.append(neighbor)
                            
    def reset_nodes(self)->None:
        for node in self.nodes:
            node.visited=False
    
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
        graph.reset_nodes()
        print()
    


if __name__=='__main__':
    main()