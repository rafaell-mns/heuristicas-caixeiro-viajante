import random

def vizinho_mais_proximo(mat):
    n = len(mat) # número de linhas matriz = número vértices

    # escolhendo um vértice inicial aleatório
    start = random.randint(0, n - 1)
    tour = [start]
    total_distance = 0

    # Algoritmo do Vizinho Mais Próximo
    for i in range(n-1):
        # Inicializar m com um valor padrão (None) que será substituído
        m = None
        # m representa o vértice mais próximo do vértice atual (start)

        # Iterar sobre todos os vértices possíveis
        for x in range(0, n):
            # Verificar se o vértice x ainda não foi visitado
            if x not in tour:
                # Atribuir o vértice não visitado a m
                m = x
                # Sair do loop após encontrar o primeiro vértice não visitado
                break

        for j in range(n):
            if j not in tour:
                if mat[start][j] < mat[start][m]:
                    m = j

        total_distance += mat[start][m]
        tour.append(m)
        start = m

    # Retornar ao ponto inicial
    tour.append(tour[0])
    total_distance += mat[start][tour[0]]

    return tour, total_distance


# Calcula a distância entre dois vértices
def distancia(v1, v2, mat):
    return mat[v1][v2]

# Função que insere um vértice na posição mais barata da subrota H
def inserir_mais_barato(tour, mat):
    melhor_custo = float('inf')
    melhor_posicao = None
    melhor_vertice = None
    n = len(mat)

    # Para cada vértice fora da subrota H
    for k in range(n):
        if k in tour:
            continue
        
        # Tenta inserir o vértice k entre cada par de vértices consecutivos do tour
        for i in range(len(tour) - 1):
            j = i + 1
            custo_atual = distancia(tour[i], k, mat) + distancia(k, tour[j], mat) - distancia(tour[i], tour[j], mat)

            if custo_atual < melhor_custo:
                melhor_custo = custo_atual
                melhor_posicao = j
                melhor_vertice = k

    # Insere o vértice na posição mais barata encontrada
    tour.insert(melhor_posicao, melhor_vertice) # tudo antes de j + k + j + tudo depois de j
    

# Algoritmo principal da inserção mais barata
def algoritmo_insercao_mais_barata(mat):
    n = len(mat)
    # Escolhe aleatoriamente três vértices para formar o ciclo inicial
    vertices_iniciais = random.sample(range(n), 3)
    subrota = vertices_iniciais
    tour = vertices_iniciais + [vertices_iniciais[0]]  # Fechando o ciclo
    # fecha o ciclo adicionando o primeiro vértice ao final da lista de vértices

    # Enquanto o ciclo não incluir todos os vértices
    while len(tour) < len(mat) + 1:
        inserir_mais_barato(tour, mat)
    # enquanto tour nao tiver todos os vertices mais o inicial, que fecha o ciclo, o 
    # laço continua

    #calculando a distancia total
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += mat[tour[i]][tour[i + 1]]

    
    return tour, total_distance, subrota


def opt_2(mat, tour):
    def calculate_total_distance(tour):
        return sum(mat[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

    n = len(tour) 
    best_distance = calculate_total_distance(tour)
    
    while True:
        improved = False
        for i in range(1, n - 2): # fixa o vértice i
            for j in range(i + 2, n): # fixa o vértice j
                # caminho antes de i + inverter sub-rota entre i e j + caminho depois de j
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_distance = calculate_total_distance(new_tour)

                if new_distance < best_distance:
                    tour = new_tour                 # atualiza o caminho
                    best_distance = new_distance    # atualiza a distância total
                    improved = True                 # marca que houve melhoria

        if not improved:
            break # encerra o loop porque não houve melhoria e já analisou tudo que era possível

    return tour, best_distance
