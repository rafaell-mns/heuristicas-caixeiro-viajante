import random
import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox
from heuristicas import *
from gerar_grafo import generate_tsp_graph
import time

def inicializar_matriz(n):
    # Inicializa a matriz de distâncias com valores aleatórios
    mat = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(i + 1, n):
            distance = random.randint(1, 100)
            mat[i][j] = distance
            mat[j][i] = distance
    return mat

# [0,1,3,4]
# [1,0,2,3]
# [3,2,0,5]
# [4,3,5,0]


def print_resultados(mat, tour=None, total_distance=None):
    # Imprime a matriz de distâncias e, se fornecido, o tour e a distância total
    print("Matriz de distâncias:")
    print('\n'.join(['\t'.join([str(int(cell)) for cell in row]) for row in mat]))
    if tour and total_distance:
        print(f"\nVértice inicial: {tour[0]}")
        caminho_formatado = ' -> '.join(map(str, tour))
        print(f"Caminho: {caminho_formatado}")
        print(f"Distância total: {total_distance}")
    print("-" * 43)


def comparar_tempo(mat, num_execucoes):
    # Função para comparar o tempo de execução de cada algoritmo em milissegundos
    tempos = {
        "Vizinho Mais Próximo": [],
        "Inserção Mais Barata": [],
        "2-opt": []
    }

    for _ in range(num_execucoes):
        start_time = time.time_ns()
        tour1, dis1 = vizinho_mais_proximo(mat)
        tempos["Vizinho Mais Próximo"].append((time.time_ns() - start_time) / 1000000 )
          # Convertendo para milissegundos

        start_time = time.time_ns()
        tour2, dis2,sub = algoritmo_insercao_mais_barata(mat)
        tempos["Inserção Mais Barata"].append((time.time_ns() - start_time) / 1000000 )  # Convertendo para milissegundos

        if dis1 < dis2:
            cam = tour1
        else:
            cam = tour2

        start_time = time.time_ns()
        opt_2(mat, cam)  
        tempos["2-opt"].append((time.time_ns() - start_time) / 1000000)  # Convertendo para milissegundos
        
    # Calcula a média dos tempos e imprime os resultados
    print("Comparação de Desempenho (média de tempos em milisegundos):")
    for heuristica, tempos_execucao in tempos.items():
        media_tempo = sum(tempos_execucao) / len(tempos_execucao)
        print(f"{heuristica}: {media_tempo:.4f} milisegundos")
    print("-" * 43)

def main():
    # Função principal que inicializa a interface gráfica e executa as heurísticas
    root = tk.Tk()
    root.withdraw()
    tour = []  # Inicializa o tour como uma lista vazia

    heuristica_opcoes = {
        "0": "Desempenho",
        "1": "Vizinho Mais Próximo",
        "2": "Inserção Mais Barata",
        "3": "2-opt",
        "4": "Sair"
    }
    heuristica_texto = "\n".join([f"{k}. {v}" for k, v in heuristica_opcoes.items()])
    escolha = simpledialog.askinteger("Escolha a Heurística", f"Escolha a opção:\n{heuristica_texto}")

    while escolha != 4:

        n = simpledialog.askinteger("Número de Vértices", "Digite o número de vértices (n > 2):")
        if n is None or n <= 2:
            messagebox.showerror("Erro", "O número de vértices deve ser maior que 2.")
            return
        mat = inicializar_matriz(n)
        if escolha > 4 or escolha <0:
            messagebox.showerror("Erro", "Escolha inválida.")
            return

        if escolha == 0:
            num_execucoes = simpledialog.askinteger("Número de Execuções", "Digite o número de execuções para cálculo da média:")
            if num_execucoes is None or num_execucoes <= 0:
                messagebox.showerror("Erro", "O número de execuções deve ser maior que 0.")
                return
            print(f'Em um grafo com {n} vértices e em {num_execucoes} execuções')
            comparar_tempo(mat, num_execucoes)
            

        elif escolha == 1:
            tour, total_distance = vizinho_mais_proximo(mat)
            print_resultados(mat, tour, total_distance)

        elif escolha == 2:
            tour, total_distance,sub = algoritmo_insercao_mais_barata(mat)
            
            print_resultados(mat, tour, total_distance)
            print("Subrota H: ",sub)
           

        elif escolha == 3:
            tour1, total_distance1 = vizinho_mais_proximo(mat)
            tour2, total_distance2,sub = algoritmo_insercao_mais_barata(mat)

            if total_distance1 < total_distance2:
                menor_tour = tour1
            else:
                menor_tour = tour2

            tour, total_distance = opt_2(mat, menor_tour)
            print_resultados(mat, tour, total_distance)
            print(f'Caminho vizinho mais próximo: {total_distance1}')
            print(f'Caminho inserção mais barata: {total_distance2}')
            print(f'Caminho otimizado com 2-opt: {total_distance}')

        else:
            messagebox.showerror("Erro", "Escolha inválida.")
            return

        if n <= 10 and tour:  # Gera o gráfico apenas se o tour tiver sido definido
            generate_tsp_graph(tour, mat)

        escolha = simpledialog.askinteger("Escolha a Heurística", f"Escolha a heurística:\n{heuristica_texto}")

if __name__ == "__main__":
    main()
