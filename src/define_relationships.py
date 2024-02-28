# we will define relationships between the input and the output nodes here
# die nodes habe die UML_codes als Namen und nicht die Identität

# this is for the desease-symtoms relations
def define_desease_symtoms_between_nodes(df, graph, relation_treshhold):

    relation_tuples =[]
    result_list = []

    for index, row in df.iterrows():

        b = df.at[index,  'umls_code_list']

        diagnose_code = df.at[index, 'icd_code' ]

        symptom_list = eval(b)

        for x in symptom_list:
              relation_tuples.append((diagnose_code, x))
    
    for item in relation_tuples:
        if relation_tuples.count(item) >= relation_treshhold:
            result_list.append(item)
    
    for res in result_list:
          if res[0] in graph and res[1] in graph:
                graph.add_edge(res[0],  res[1], name="Desease-Symptom")
    

    
    

# this is for the patients - desease relatinships

def define_patients_desease_relations(df, graph, relation_treshhold):

    relation_tuples =[]
    result_list = []
    for index, row in df.iterrows():

        subject_id = df.at[index, 'subject_id']

        desease_uml_code = df.at[index, 'icd_code']

        relation_tuples.append((subject_id, desease_uml_code))
        

    for item in relation_tuples:
        if relation_tuples.count(item) >= relation_treshhold:
            result_list.append(item)
    
    for res in result_list:
          if res[0] in graph and res[1] in graph:
                graph.add_edge(res[0], res[1], name="Patient-Desease")
    

# this is for the patient - desease raltionship

def define_patient_symptoms_relations(df, graph, relation_treshhold):

    relation_tuples =[]
    result_list = []

    for index, row in df.iterrows():

        subject_id = df.at[index, 'subject_id']

        b = df.at[index,  'umls_code_list']

        symptom_list = eval(b)

        for x in symptom_list:
            relation_tuples.append((x, subject_id))
    
    for item in relation_tuples:
        if relation_tuples.count(item) >= relation_treshhold:
            result_list.append(item)
    
    for res in result_list:
          if res[0] in graph and res[1] in graph:
                graph.add_edge(res[0],res[1], name="Patient-Symptom")