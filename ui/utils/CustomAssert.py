# import logging
from ui.utils.AllureStepLog import log_step


class CustomAssert:

    def __init__(self):
        pass

    def compare_equal_to(self, exp, actual):
        assert exp == actual, f"value not matching, exp {exp} and actual is {actual}"
        log_step(f"value matching, exp {exp} and actual is {actual}")

    def compare_gte(self, exp, actual):
        assert exp >= actual, f"value not matching, exp {exp} and actual is {actual}"
        log_step(f"value matching, exp {exp} and actual is {actual}")

    def compare_lse_to(self, exp, actual):
        assert exp <= actual, f"value not matching, exp {exp} and actual is {actual}"
        log_step(f"value matching, exp {exp} and actual is {actual}")
