'''
Erik Lopez

Here is the code to show that my I/O and graph function modules are working.

'''
import funks_utils
import io_utils

def main():
    '''
    All tests are here
    '''
    # undirected graph with weights
    nodes, edges, weights = io_utils.cgraph("parseme.txt", True)
    print(nodes,'\n',edges,'\n', weights)
    print(io_utils.adj_ls(nodes, edges))
    print(io_utils.adj_matrix(nodes, edges))
    degreedict = funks_utils.create_deg(nodes, edges)
    print(degreedict)
    # Testing for directed graph
    print(funks_utils.create_deg(nodes, edges, True))
    # Testing to see what biggest degree of undirected graph is
    print(funks_utils.biggest_deg(degreedict))
    # Testing to check remove loops works
    print(funks_utils.rm_selfloop(edges))
    return


if __name__ == "__main__":
    main()
