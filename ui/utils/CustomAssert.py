import logging


class CustomAssert:

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)

    def compare_equal_to(self, exp, actual):
        assert exp == actual, f"value not matching, exp {exp} and actual is {actual}"
        self.logger.info(f"value matching, exp {exp} and actual is {actual}")

    def compare_gte(self, exp, actual):
        assert exp >= actual, f"value not matching, exp {exp} and actual is {actual}"
        self.logger.info(f"value matching, exp {exp} and actual is {actual}")

    def compare_lse_to(self, exp, actual):
        assert exp <= actual, f"value not matching, exp {exp} and actual is {actual}"
        self.logger.info(f"value matching, exp {exp} and actual is {actual}")
