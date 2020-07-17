"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
        

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # pass 
        # make a queue
        q = Queue()
        # enqueue our starting node
        q.enqueue(starting_vertex)

        #make a set to track if we'vebeen here before. don't want go to there twice
        visited = set()

        # result = []

        # while our queue isn't empty, 
        while q.size() > 0:
        # dequeue whatevers at the front of the line, this is our current_node
            current_node = q.dequeue()
        ## if we havent visited this node yet
            if current_node not in visited:
        ### mark as visited
                visited.add(current_node)
        ###print the vertex
                print(current_node)
                # result.append(current_node)
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### add neighbors to queue (for each of the neighbors, add to queue)
                for neighbor in neighbors:
                    ## add to queue
                    q.enqueue(neighbor)
        # print(",".join(str(x) for x in result))
        #which goes in first?  1 
        # q = Queue()
        # visited = set(1,2,3,4,5,6,7)
        #which goes in first?
        # current_node = 6

        # neighbors = [1,6]
        # 1 --> 2 --> 3 <--> 5
        #  \    |
        #   \   4
        #    7  

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #stack
        s = Stack()
        #push on our starting node
        s.push(starting_vertex)

        #make a set to track if we've been here before
        visited = set()

        # results = []
        #while our stack isn't empty
        while s.size() > 0:
        ## pop off whatevers on top, this is the current_node
            current_node = s.pop()
        ## if we haven't visited this vertex before
            if current_node not in visited:
        ###print
                print(current_node)
        ### mark as visited
                visited.add(current_node)
                # results.append(current_node)
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### for each of the neighbors
                for neighbor in neighbors:
        ### add to our stack
                    s.push(neighbor)
        # print(",".join(str(x) for x in results))
        # s = Stack(
        #     5,
        #     1,
        #     6,
        #     3,
        # )

        # visted = set(1,2,4,7,6,3) #5

        # current_node = 3

        # neighbors = [5]

    # def dft_recursive(self, starting_vertex, visited = {}):
    #     """
    #     Print each vertex in depth-first order
    #     beginning from starting_vertex.

    #     This should be done using recursion.
    #     """
    #     visited = set()
    #     results = []
    #     self.recursiveDFSHelper(starting_vertex, visited, results)
    #     # print(",".join(str(x) for x in results))

    # def recursiveDFSHelper(self, starting_vertex, visited,results):
    #     if starting_vertex not in visited:
    #         visited.add(starting_vertex)
    #         results.append(starting_vertex)
    #         print(starting_vertex)
    #         for neighbor in self.get_neighbors(starting_vertex):
    #             self.recursiveDFSHelper(neighbor, visited, results)

    def dft_recursive(self, starting_vertex, visited = set()):
         """
         if visited is None:
            visited = set() 
            ----or --- you can just use a param called visited = set()
         """
         # mark this vertex as visited
         visited.add(starting_vertex)
         print(starting_vertex)
         ## for each neighbor
         neighbors = self.get_neighbors(starting_vertex)
         for neighbor in neighbors:
         #if its not visited
            if neighbor not in visited:
         ##recurse through the neighbor
                self.dft_recursive(neighbor, visited)

        #dont need to return None, will automatically return none


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #make a queue
        # queue =[(starting_vertex, [])]
        #make a set to track nodes we've visited
        visited = set()



        # while len(queue) > 0:
        #     node, path = queue.pop(0)
        #     path.append(node)
        #     visited.add(node)
        #     if node == destination_vertex:
        #         return path
            
        #     for neighbor in self.get_neighbors(node):
        #         if neighbor not in visited:
        #             queue.append((neighbor, path[:]))
        
        # return None
        q = Queue()
        path = [starting_vertex]
        q.enqueue(path)
        #while queue isn't empty
        while q.size() > 0:
        #dequeue the node at the front of the line
            current_path = q.dequeue()
            current_node = current_path[-1]
        ###if this node is our target node
            if current_node == destination_vertex:
        ##return it! return true
                return current_path
        ###if not visited
            if current_node not in visited:
        ###mark as visited
                visited.add(current_node)
        ###get its neighbors
                neighbors = self.get_neighbors(current_node)
        ##for each neighbor
                for neighbor in neighbors:
        ##add to our queue
                    path_copy = current_path[:]
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack =[(starting_vertex, [])]
        visited = set()

        while len(stack) > 0:
            node, path = stack.pop()
            path.append(node)
            visited.add(node)
            if node == destination_vertex:
                return path
            
            for neighbor in self.get_neighbors(node):
                if neighbor not in visited:
                    stack.append((neighbor, path[:]))
        
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()
        result = []
        def dfs_recursive_helper(start, path, visited, results):
            if start not in visited:
                visited.add(start)
                path.append(start)
                if start == destination_vertex:
                    results.extend(path)
                for neighbor in self.get_neighbors(start):
                    dfs_recursive_helper(neighbor, path[:], visited, results)
        dfs_recursive_helper(starting_vertex, [], visited, result)
        return result
    def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=set()):
        
        visited.add(vertex)

        if vertex == destination_vertex:
            return path

        if len(path) == 0:
            path.append(vertex)

    # def dfs_recursive(self, vertex, visited=set()):
    #     if vertex not in visited:
    #         visited.add(vertex)
    #         neighbors = self.get_neighbors(vertex)
    #         for neighbor in neighbors:
    #             self.dfs_recursive(neighbor, visited)
    #     return visited


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
