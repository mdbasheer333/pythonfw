import pandas as pd
import os


# Read the Excel file and extract the data into a dictionary
def read_excel_data(sheet_name):
    file_path = os.path.abspath(os.curdir) + "\\ui\\data\\testdata.xlsx"
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    filtered_df = df[df['Flag'] == 'yes']
    list_of_dicts = filtered_df.to_dict(orient='records')
    return list_of_dicts
