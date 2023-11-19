import pytest

from ui.utils.ExcelUtil import get_tc_list, select_tests_from_excel


def run_selected_tests():
    excel_data = get_tc_list()
    tests_to_execute = select_tests_from_excel(excel_data)

    if tests_to_execute:
        pytest_test_names = [f"{test_name}" for test_name in tests_to_execute]
        pytest.main(pytest_test_names)
    else:
        raise Exception("no tests found....!")


run_selected_tests()
