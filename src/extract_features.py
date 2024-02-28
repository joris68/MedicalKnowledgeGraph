import networkx as nx
import pandas as pd
import os
import openpyxl
import ast



# importing the csv file
#current_directory = os.getcwd()

#file_path = current_directory + '\\MimicIV_Version_18.06.23 (1).xlxs'

#mimic_data = pd.read_excel( 'MimicIV_Version_18.06.23 (1).xlsx' , nrows= 1000)


# returns a tuple list of input nodes
def extract_input_nodes_as_tuples(df):


    # (code, description)
    uml_tuples = []
    uml_descriptions = []
    uml_codes = []


    for index, row in df.iterrows():

        a = df.at[index,  'umls_canonical_name_list']
        b = df.at[index,  'umls_code_list']

        a_list = eval(a)
        b_list = eval(b)

        for x in range(len(a_list)):
            if a_list[x] not in uml_descriptions and b_list[x] not in uml_codes:
                uml_descriptions.append(a_list[x])
                uml_codes.append(b_list[x])

                uml_tuples.append((b_list[x], a_list[x]))

    return uml_tuples

# returns a tuple-list of output nodes
def extract_output_nodes_as_tuples(df):

    uml_tuples = []
    uml_description = []
    uml_code =[]

    df['Diagnose_Combined'] = list(zip(df['icd_code'], df['icd_title']))

    for index, row in df.iterrows():

        tuple = df.at[index,  'Diagnose_Combined']
        

        if tuple[0] not in uml_code and tuple[1] not in uml_description:

            uml_code.append(tuple[0])
            uml_description.append(tuple[1])

            uml_tuples.append(tuple)
    
    return uml_tuples

def define_patient_tuples(df):

    patient_ids= []

    for index, row in df.iterrows():

        subject_id = df.at[index,  'subject_id']

        patient_ids.append(subject_id)
    
    return patient_ids


