import datetime
import os


class TimestampFolder:
    timestamp_folder = None

    @classmethod
    def set_timestamp_folder(cls):
        if not cls.timestamp_folder:
            current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            cls.timestamp_folder = f"./testresults/testreport_{current_time}/"

    @classmethod
    def get_timestamp_folder(cls):
        return cls.timestamp_folder

    @staticmethod
    def create_timestamp_folder():
        TimestampFolder.set_timestamp_folder()
        if not os.path.exists(TimestampFolder.get_timestamp_folder()):
            os.makedirs(TimestampFolder.get_timestamp_folder())
        else:
            raise Exception(f"Folder '{TimestampFolder.get_timestamp_folder()}' already exists.")
