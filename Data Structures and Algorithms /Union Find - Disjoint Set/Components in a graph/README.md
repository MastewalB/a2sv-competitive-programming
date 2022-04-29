# Components in a graph

After setting each edge of the graph as its own parent, it's possible to connect each edge to a larger set when two nodes with common sets meet.

The **Union** function connects the sets of two nodes by migrating the smaller set to the larger one i.e. setting its parent as the larger one. The rank of the smaller is changed to zero to indicate that it's a subset of another bigger parent. This will help us to obtain the *smallest* and *largest* parents.
