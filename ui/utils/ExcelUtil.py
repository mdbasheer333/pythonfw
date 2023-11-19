import pandas as pd
import os

import pytest


# Read the Excel file and extract the data into a dictionary
def get_test_data(fileName):
    file_path = os.path.abspath(os.curdir) + "\\ui\\data\\" + fileName + ".xlsx"
    df = pd.read_excel(file_path, sheet_name="testdata")
    filtered_df = df[df['Run'] == 'yes']
    list_of_dicts = filtered_df.to_dict(orient='records')
    return list_of_dicts


def get_tc_list(file_name="test_execution_list"):
    file_path = os.path.abspath(os.curdir) + "\\ui\\data\\" + file_name + ".xlsx"
    df = pd.read_excel(file_path, sheet_name="list")  # Assuming the data is in the first sheet
    return df


def get_test_data_with_flags(data):
    test_data = {}
    for index, row in data.iterrows():
        test_name = row['TC_Name']
        flag = row['Run']
        tc_path = row['TC_path']
        test_data[tc_path+"::"+test_name] = flag.lower() == 'yes'  # Store test names with their corresponding flags
    return test_data


def select_tests_from_excel(exl_data):
    tests_to_run = []
    test_data = get_test_data_with_flags(exl_data)

    for name, flag in test_data.items():
        if flag:
            tests_to_run.append(name)

    return tests_to_run



