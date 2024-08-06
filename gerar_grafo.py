import matplotlib.pyplot as plt
import networkx as nx

def generate_tsp_graph(tour, mat):
    n = len(mat)
    
    # Criar um grafo para visualização
    G = nx.Graph()

    # Adicionar nós
    for i in range(n):
        G.add_node(i)

    # Adicionar arestas com pesos (distâncias)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=mat[i][j])

    # Posição dos nós (distribuição circular)
    pos = nx.circular_layout(G)

    # Desenhar o grafo
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=16, font_weight='bold')

    # Destacar o tour encontrado
    edges_in_tour = [(tour[i], tour[i+1]) for i in range(len(tour) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges_in_tour, edge_color='r', width=3)

    # Desenhar as arestas com seus pesos (distâncias)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='green', font_size=14, label_pos=0.4)

    # Adicionar o texto do tour no gráfico
    mostrar_tour = True
    if mostrar_tour:
        tour_str = f"Tour: {tour[0]} -> {tour[1]} -> ... -> {tour[-1]}"
        plt.text(0.15, 0.92, tour_str, fontsize=14, ha='center', va='top', transform=plt.gca().transAxes, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

    plt.title(f"Total Distance: {sum(mat[tour[i]][tour[i+1]] for i in range(len(tour) - 1))}", fontsize=16)

    # Exibir o grafo
    plt.show()
