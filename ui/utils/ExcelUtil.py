import os

import pandas as pd

from ui.utils import CommonLib
from ui.utils.CommonLib import CommonLib


def get_test_data(fileName):
    file_path = os.path.abspath(os.curdir) + "\\ui\\data\\" + fileName + ".xlsx"
    df = pd.read_excel(file_path, sheet_name="testdata")
    filtered_df = df[df['Run'] == 'yes']
    list_of_dicts = filtered_df.to_dict(orient='records')
    return list_of_dicts


def get_tc_list(file_name="test_execution_list"):
    file_path = os.path.abspath(os.curdir) + "\\ui\\data\\" + file_name + ".xlsx"
    df = pd.read_excel(file_path, sheet_name="list")
    return df


def get_test_data_with_flags(data):
    test_data = {}
    for index, row in data.iterrows():
        test_name = row['TC_Name']
        flag = row['Run']
        tc_path = row['TC_path']
        test_data[tc_path + "::" + test_name] = flag.lower() == 'yes'
    return test_data


def select_tests_from_excel(exl_data):
    tests_to_run = []
    test_data = get_test_data_with_flags(exl_data)
    for name, flag in test_data.items():
        if flag:
            tests_to_run.append(name)
    return tests_to_run


def export_to_excel():
    act_test_res = CommonLib.get_global_test_results()
    existing_data = pd.read_excel("./testresults/" + CommonLib.get_timestamp_folder() + 'test_execution_list.xlsx')
    df = pd.DataFrame(existing_data)
    df_dict = df.to_dict(orient='records')
    i = 0
    for each_df_dict in df_dict:
        if str(each_df_dict.get('Run')).lower() == 'no':
            i = i + 1
            continue
        elif str(each_df_dict.get('Run')).lower() == 'yes':
            indices = [index for index, rec in enumerate(act_test_res) if
                       rec.get('TC_Name') == each_df_dict.get("TC_Name") or rec.get('TC_Name').split("[")[
                           0] == each_df_dict.get(
                           "TC_Name")]
            if len(indices) == 0:
                i = i + 1
                continue
            elif len(indices) == 1:
                df_dict[i]['Status'] = act_test_res[indices[0]]['Status']
            else:
                f_indices = [act_test_res[x]['Status'] == 'Failed' for x in indices]
                if len(f_indices) == 0:
                    df_dict[i]['Status'] = 'Passed'
                else:
                    df_dict[i]['Status'] = 'Failed'
        i = i + 1
    df = pd.DataFrame(df_dict)
    df.to_excel("./testresults/" + CommonLib.get_timestamp_folder() + 'test_execution_list.xlsx', index=False)
