import heapq

# Definindo o grafo com cidades e os custos entre elas
graph = {
    'Arad': [('Sibiu', 140), ('Timisoara', 118), ('Zerind', 75)],
    'Zerind': [('Oradea', 71), ('Arad', 75)],
    'Oradea': [('Sibiu', 151), ('Zerind', 71)],
    'Timisoara': [('Lugoj', 111), ('Arad', 118)],
    'Lugoj': [('Mehadia', 70), ('Timisoara', 111)],
    'Mehadia': [('Drobeta', 75), ('Lugoj', 70)],
    'Drobeta': [('Craiova', 120), ('Mehadia', 75)],
    'Sibiu': [('Fagaras', 99), ('Rimnicu Vilcea', 80), ('Arad', 140), ('Oradea', 151)],
    'Rimnicu Vilcea': [('Pitesti', 97), ('Craiova', 146), ('Sibiu', 80)],
    'Craiova': [('Pitesti', 138), ('Drobeta', 120), ('Rimnicu Vilcea', 146)],
    'Fagaras': [('Bucareste', 211), ('Sibiu', 99)],
    'Pitesti': [('Bucareste', 101), ('Rimnicu Vilcea', 97), ('Craiova', 138)],
    'Bucareste': [('Fagaras', 211), ('Pitesti', 101)]
}

# Função que implementa a Busca de Custo Uniforme
def uniform_cost_search(graph, start, goal):
    # Fila de prioridade (min-heap) para armazenar (custo total, caminho atual)
    queue = [(0, [start])]
    # Conjunto para armazenar cidades já visitadas
    visited = set()

    while queue:
        # Remove o caminho com menor custo total
        cost, path = heapq.heappop(queue)
        city = path[-1]

        # Se a cidade atual for o destino, retorna o caminho e o custo total
        if city == goal:
            return path, cost

        # Se a cidade não foi visitada, explore seus vizinhos
        if city not in visited:
            visited.add(city)

            for neighbor, travel_cost in graph[city]:
                # Se o vizinho ainda não foi visitado, calcule o novo custo e adicione à fila
                if neighbor not in visited:
                    new_cost = cost + travel_cost
                    new_path = path + [neighbor]
                    heapq.heappush(queue, (new_cost, new_path))

    return None, float('inf')  # Retorna None se não houver caminho

start_city = 'Arad'
goal_city = 'Bucareste'

path, cost = uniform_cost_search(graph, start_city, goal_city)

if path:
    print(f"Melhor caminho de {start_city} para {goal_city}: {' → '.join(path)}")
    print(f"Custo total: {cost}")
else:
    print(f"Não foi possível encontrar um caminho de {start_city} para {goal_city}")
