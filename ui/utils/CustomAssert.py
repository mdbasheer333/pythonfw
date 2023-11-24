from ui.utils import logger


class CustomAssert:

    def __init__(self):
        self.loger = logger.logger

    def compare_equal_to(self, exp, actual):
        assert exp == actual, f"value not matching, exp {exp} and actual is {actual}"
        self.loger.info(f"value matching, exp {exp} and actual is {actual}")

    def compare_gte(self, exp, actual):
        assert exp >= actual, f"value not matching, exp {exp} and actual is {actual}"
        self.loger.info(f"value matching, exp {exp} and actual is {actual}")

    def compare_lse_to(self, exp, actual):
        assert exp <= actual, f"value not matching, exp {exp} and actual is {actual}"
        self.loger.info(f"value matching, exp {exp} and actual is {actual}")
