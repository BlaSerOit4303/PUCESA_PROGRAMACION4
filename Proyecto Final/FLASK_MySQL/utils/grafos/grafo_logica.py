import networkx as nx
import matplotlib
from flask import current_app
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import random


def generar_ruta_grafico(origen, destino, edges, costa=False):
    G = nx.DiGraph()
    G.add_weighted_edges_from(edges)

    pos = nx.circular_layout(G)
    ciudades_costeras = {'Manta', 'Portoviejo', 'Guayaquil'}

    try:
        ruta_final = nx.dijkstra_path(G, origen, destino)
        costo = nx.dijkstra_path_length(G, origen, destino)

        if costa and not any(c in ruta_final for c in ciudades_costeras):
            for intermedia in ciudades_costeras:
                try:
                    ruta1 = nx.dijkstra_path(G, origen, intermedia)
                    ruta2 = nx.dijkstra_path(G, intermedia, destino)
                    ruta_final = ruta1[:-1] + ruta2
                    costo = nx.dijkstra_path_length(G, origen, intermedia) + nx.dijkstra_path_length(G, intermedia, destino)
                    break
                except:
                    continue

        plt.figure(figsize=(10, 6))
        nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=1500)
        nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
        nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowstyle='-|>', width=2)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

        if ruta_final:
            edge_list = [(ruta_final[i], ruta_final[i+1]) for i in range(len(ruta_final)-1)]
            nx.draw_networkx_edges(G, pos, edgelist=edge_list, edge_color='red', width=3, arrows=True, arrowstyle='-|>')
            nx.draw_networkx_nodes(G, pos, nodelist=ruta_final, node_color='orange', node_size=1800)

        plt.title(f"Ruta óptima de {origen} a {destino}", fontsize=14)
        plt.tight_layout()

        # ✅ Generar nombre y ruta segura
        nombre_archivo = f"resultado_{origen}_{destino}_{random.randint(1000,9999)}.png"
        img_path = os.path.join(current_app.root_path, 'static', 'img', nombre_archivo)
        os.makedirs(os.path.dirname(img_path), exist_ok=True)
        plt.savefig(img_path)
        plt.close()

        return ruta_final, costo, "✅ Ruta generada con éxito", nombre_archivo

    except nx.NetworkXNoPath:
        return None, None, f"❌ No existe ruta entre {origen} y {destino}", None
