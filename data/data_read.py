def criar_lista_de_adjacencia():
    lista_de_adjacencia = []

    with open("data/as-caida20071105.txt", "r") as file:
        lines = file.readlines()

    in_data_section = False

    for line in lines:
        line = line.strip()

        if line.startswith("# FromNodeId"):
            in_data_section = True
            continue

        if not in_data_section:
            continue

        columns = line.split()
        from_node = int(columns[0])
        to_node = int(columns[1])

        while len(lista_de_adjacencia) <= from_node:
            lista_de_adjacencia.append([])

        lista_de_adjacencia[from_node].append(to_node)

    return lista_de_adjacencia
