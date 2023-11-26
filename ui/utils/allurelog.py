import allure


def log_step(text):
    with allure.step(str(text)):
        pass
