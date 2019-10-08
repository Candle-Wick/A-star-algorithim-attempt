The program contains two major features, the class node and the function Astar.
The class node represents a single node in a given graph. When a node is created it expects the name of the node, the x co-ordinate, and the y co-ordinate. It expects x and y to be integers.

The function Astar expects a list of nodes, it will then ask for the names of the starting and end node. Should both be found it will attempt to find the shortest path between Theese nodes. It will output a list containing the names of the nodes it believes is the shortest path.

It is important to remember that each node must be manually conected towards eachother. This is done by calling the addp function under the object, then passing towards it the pointer to the desired node for connection.

Should a path not be found, the function Astar will throw a IndexError.
