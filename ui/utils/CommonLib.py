import datetime
import os
import shutil


class CommonLib:
    timestamp_folder = None
    global_test_results = []

    @staticmethod
    def get_global_test_results():
        return CommonLib.global_test_results

    @staticmethod
    def set_global_test_results(obj):
        CommonLib.global_test_results.append(obj)

    @classmethod
    def set_timestamp_folder(cls):
        if not cls.timestamp_folder:
            current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            cls.timestamp_folder = f"testreport_{current_time}/"

    @classmethod
    def get_timestamp_folder(cls):
        return cls.timestamp_folder

    @staticmethod
    def create_timestamp_folder():
        CommonLib.set_timestamp_folder()
        if not os.path.exists("./testresults/" + CommonLib.get_timestamp_folder()):
            os.makedirs("./testresults/" + CommonLib.get_timestamp_folder())
            os.makedirs("./testresults/" + CommonLib.get_timestamp_folder() + "/screenshots/")
        else:
            raise Exception(f"Folder '{CommonLib.get_timestamp_folder()}' already exists.")

    @staticmethod
    def copy_excel_to_current_test_results_folder(file_name="test_execution_list"):
        existing_file_path = os.path.abspath(os.curdir) + "\\ui\\data\\" + file_name + ".xlsx"
        destination_folder = './testresults/' + CommonLib.get_timestamp_folder()
        shutil.copy(existing_file_path, destination_folder)
