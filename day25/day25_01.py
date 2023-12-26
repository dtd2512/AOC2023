import day25_lib as lib
import networkx as nx

INPUT_FILENAME = "input_25.txt"

def minimum_cut(G: nx.Graph):
    G.remove_edges_from(nx.minimum_edge_cut(G))
    return nx.connected_components(G)

def main():
    G = lib.parse_input(INPUT_FILENAME)
    G1, G2 = minimum_cut(G)
    print("Result: ", len(G1)*len(G2))
    # lib.draw_graph(G)

if __name__ == "__main__":
    main()