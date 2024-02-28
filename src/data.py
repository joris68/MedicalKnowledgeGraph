import os
import pandas as pd

# importing the csv file

def get_data(number_of_rows):
    current_directory = os.getcwd()

    file_path = current_directory + '\\MimicIV_Version_18.06.23 (1).xlxs'
    print(file_path)

    mimic_data = pd.read_excel( 'MimicIV_Version_18.06.23 (1).xlsx' , nrows=  number_of_rows)

    return mimic_data