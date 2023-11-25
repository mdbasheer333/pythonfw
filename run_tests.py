import pytest
import argparse

from ui.utils.CommonLib import TimestampFolder
from ui.utils.ExcelUtil import get_tc_list, select_tests_from_excel


def run_selected_tests():
    TimestampFolder.create_timestamp_folder()
    parser = argparse.ArgumentParser()
    parser.add_argument("--browser", help="browser on which execution should take on", default="chrome")
    parser.add_argument("--env", help="environment on execution should take on", default="qa")
    args = parser.parse_args()

    excel_data = get_tc_list()
    tests_to_execute = select_tests_from_excel(excel_data)

    if tests_to_execute:
        pytest_test_names = [f"{test_name}" for test_name in tests_to_execute]
        lst = ['--html', f'./testresults/{TimestampFolder.get_timestamp_folder()}/testresults.html',
               '--self-contained-html',
               '--junitxml', f'./testresults/{TimestampFolder.get_timestamp_folder()}/testresults.xml',
               '--browser', f'{args.browser}', '--env', f'{args.env}'] + pytest_test_names
        pytest.main(lst)
    else:
        raise Exception("no tests found....!")


run_selected_tests()
