import softest


class CustomSoftAssert(softest.TestCase):
    def compare_equal_to(self, exp, actual):
        self.soft_assert(self.assertEqual, exp == actual, f"value not matching, exp {exp} and actual is {actual}")
        print(f"value matching, exp {exp} and actual is {actual}")

    def compare_gte(self, exp, actual):
        self.soft_assert(self.assertTrue, exp >= actual, f"value not matching, exp {exp} and actual is {actual}")
        print(f"value matching, exp {exp} and actual is {actual}")

    def compare_lse_to(self, exp, actual):
        self.soft_assert(self.assertTrue, exp <= actual, f"value not matching, exp {exp} and actual is {actual}")
        print(f"value matching, exp {exp} and actual is {actual}")

