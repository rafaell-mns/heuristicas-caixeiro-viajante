# Trabalho em Grupo - Heurísticas para o Caixeiro Viajante Simétrico (TSP)

## Descrição do Projeto

Este projeto foi desenvolvido para a disciplina de Teoria e Aplicações em Grafos e tem como objetivo implementar e comparar o tempo de execução de diferentes heurísticas para a solução do problema do Caixeiro Viajante Simétrico (TSP). Além do código-fonte, também foi produzido um relatório técnico e slides para a apresentação.

As heurísticas implementadas incluem:

- Vizinho Mais Próximo
- Inserção Mais Barata
- 2-OPT

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- `gerar_grafo.py`: Contém a função `generate_tsp_graph` para gerar e visualizar o grafo TSP.
- `heuristicas.py`: Contém as implementações das heurísticas de Vizinho Mais Próximo, Inserção Mais Barata e 2-OPT.
- `teste_main.py`: Script principal que inicializa a interface gráfica, permite a escolha da heurística e executa os algoritmos.

## Como Executar

1. **Pré-requisitos**: Certifique-se de ter o Python instalado em sua máquina, juntamente com as bibliotecas `numpy`, `matplotlib`, `networkx`, e `tkinter`.

2. **Clone o Repositório**:
    ```sh
    git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
    cd SEU_REPOSITORIO
    ```

3. **Instale as Dependências**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Execute o Script Principal**:
    ```sh
    python teste_main.py
    ```

## Funcionalidades

- **Vizinho Mais Próximo**: Seleciona um vértice inicial aleatório e constrói o tour escolhendo sempre o vértice mais próximo não visitado.
- **Inserção Mais Barata**: Inicializa um ciclo com três vértices e insere os demais vértices na posição que resulta no menor aumento de custo.
- **2-OPT**: Realiza melhorias no tour trocando arestas de lugar para reduzir a distância total.

## Interface Gráfica

A interface gráfica permite ao usuário:
- Escolher a heurística a ser utilizada.
- Definir o número de vértices do grafo.
- Visualizar o tour e a distância total resultante.
- Comparar o tempo de execução das heurísticas.

## Exemplo de Uso

1. Ao executar o script `teste_main.py`, uma janela gráfica aparecerá solicitando a escolha da heurística.
2. Informe o número de vértices do grafo.
3. O resultado será exibido no console e, para grafos com 10 vértices ou menos, um gráfico visual será gerado mostrando o tour encontrado.

## Autores

- Alex Nunes
- Bernardo Cavalcante
- Francisco Rafael
- Rafael Vaz