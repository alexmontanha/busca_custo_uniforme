# Uniform Cost Search (UCS) - Busca de Custo Uniforme

Este exemplo demonstra a aplicação do algoritmo **Uniform Cost Search (UCS)** para encontrar o caminho de menor custo entre duas cidades em um grafo. O algoritmo é utilizado para encontrar o caminho mais curto em um grafo ponderado, onde o custo de cada aresta é diferente.

## Requisitos

- Python 3.x

## Explicação

- O grafo é representado por um dicionário, onde as chaves são as cidades e os valores são listas de tuplas contendo cidades vizinhas e o custo da rota.
- O algoritmo **Uniform Cost Search (UCS)** utiliza uma fila de prioridade (min-heap) para explorar sempre o caminho de menor custo até encontrar o destino.
- A função `uniform_cost_search` tenta encontrar o caminho com o menor custo total, considerando todos os possíveis caminhos e simulando diferentes rotas.
- O código imprime o melhor caminho de Arad a Bucareste, incluindo o custo total.

Este exemplo mostra como a busca simula diversas rotas até encontrar a melhor solução, conforme discutido no slide. Se você quiser testar com outras cidades e modificar o grafo, a estrutura é facilmente adaptável.
