import networkx as nx
import matplotlib.pyplot as plt
from ed.src.data import get_data
from ed.src.extract_features import extract_input_nodes_as_tuples, extract_output_nodes_as_tuples, define_patient_tuples
from ed.src.define_relationships import define_desease_symtoms_between_nodes, define_patient_symptoms_relations, define_patients_desease_relations



mimic_data = get_data(number_of_rows= 1000)

def define_nodes(input_nodes, output_nodes, patient_nodes, graph):

    for node in input_nodes:

        graph.add_node( node[0] , name = node[1] )
    

    for node in output_nodes:

        graph.add_node( node[0], name = node[1] )

    for node in patient_nodes:
    # hier ist kein tuple drin
        graph.add_node(node, name = "Patient")


def build_graph(  threshhold_desease_symtoms= 10, threshhold_patient_symtoms=1, threshhold_patieent_desease=1 ):
    graph = nx.Graph()

    input_nodes = extract_input_nodes_as_tuples(mimic_data)

    output_nodes = extract_output_nodes_as_tuples(mimic_data)

    patient_nodes = define_patient_tuples(mimic_data)

    define_nodes(input_nodes, output_nodes, patient_nodes, graph)


    define_desease_symtoms_between_nodes(mimic_data, graph, threshhold_desease_symtoms)

    define_patient_symptoms_relations(mimic_data, graph, threshhold_patient_symtoms)

    define_patients_desease_relations(mimic_data, graph, threshhold_patieent_desease)

    return graph

#graph = build_graph()
#pos = nx.circular_layout(graph)
#nx.draw(graph,pos, with_labels=True, node_color='lightblue', edge_color='gray')

# Display the graph
#plt.savefig("graph_visualization.png")






