# now we want to retrieve a subgraph for a given dataset

# we have the following input: subject_id (patient_id) und the sysptoms IDS
import networkx as nx
import matplotlib.pyplot as plt
from ed.src.knowledge_graph import build_graph
from ed.src.data import get_data


mimic_data = get_data(number_of_rows=1000)

random_row = mimic_data.sample(n=1)
subject_id = random_row['subject_id']
b = random_row['umls_code_list']
d = random_row['icd_code']

desease = d.values[0]

print(type(subject_id))

print(type(b))

subject_id = subject_id.values[0]


input_list = []

input_list.append(subject_id)
input_list.append(desease)

symptom_list = eval(b.values[0])

for x in symptom_list:
    input_list.append(x)


graph = build_graph()

print("InputList :" + str(input_list) )


sub = graph.subgraph(input_list)

pos = nx.spring_layout(sub)
nx.draw_networkx_nodes(sub, pos)
nx.draw_networkx_edges(sub, pos, edge_color="red")
nx.draw_networkx_labels(sub, pos, labels={node: sub.nodes[node]['name'] for node in sub.nodes()})
plt.show()


