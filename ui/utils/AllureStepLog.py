import allure


def log_step(text):
    with allure.step(text):
        pass
