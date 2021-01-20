edge_tuple_list = []

def read_from_file(file):
    with open(file) as f:

        reader = next(f)

        no_cities = int(reader.split()[0])
        no_edges = int(reader.split()[1])

        for _ in range(no_edges):
            reader = next(f)
            o1 = reader.split()[0]
            o2 = reader.split()[1]
            dist = int(reader.split()[2])
            edge_tuple_list.append((o1, o2, dist))

read_from_file("data.txt")

def get_neighbours(city):

    tuple_list = []
    for edge_tuple in edge_tuple_list:
        if edge_tuple[0] == city:
            tuple_list.append((edge_tuple[1], edge_tuple[2]))

        if edge_tuple[1] == city:
            tuple_list.append((edge_tuple[0], edge_tuple[2]))

    return tuple_list

def bfs (start, stop):

    #"breadth-first search"
    already_visited_dict = {}
    already_visited_dict[start] = 1
    current = start
    queue = []
    path = [current]
    iters = 0
    while current != stop:
        iters += 1
        neighbours = get_neighbours(current)

        for city_distance in neighbours:
            if (city_distance[0] not in already_visited_dict):
                already_visited_dict[city_distance[0]] = 1
                queue.append((city_distance, path))
        nxt = queue.pop(0)
        current = (nxt[0])[0]
        path = nxt[1].copy()
        path.append(current)

    print(f"BFS: {path} number of iterations {iters}")

def dfs(start, stop):

    already_visited_dict = {}
    already_visited_dict[start] = 1
    current = start
    path = [current]
    iters = 0
    while current != stop:
        iters +=1
        nxt = current
        neighbours = get_neighbours(current)

        for city_distance in neighbours:
            if(city_distance[0] not in already_visited_dict):
                already_visited_dict[city_distance[0]] = 1
                nxt = city_distance[0]
                break
        if nxt == current:
            path.pop()
            current = path[-1]
            continue
        current = nxt
        path.append(current)
    print(f"DFS: {path} number of iterations {iters}")


def mcs(start, stop):

    "minimum-cost search"
    
    already_visited_dict = {}
    already_visited_dict[start] = 1
    current = start
    path = [current]
    iters = 0
    while (current != stop):
        cost = 9999
        iters += 1
        nxt = current
        neighbours = get_neighbours(current)
        for city_distance in neighbours:
            if (city_distance[0] not in already_visited_dict and city_distance[1] < cost):
                nxt = city_distance[0]
                cost = city_distance[1]

        if nxt == current:
            path.pop()
            current = path[-1]
            continue

        already_visited_dict[nxt] = 1
        current = nxt
        path.append(current)
    print(f"MCS: {path}, number of iterations: {iters}")

bfs('Oradea', 'Craiova')
dfs('Oradea', 'Craiova')
mcs('Oradea', 'Craiova')