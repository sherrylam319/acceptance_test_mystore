from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



class DriverFactory:
    @staticmethod
    def get_driver(config):
        if config["config"][0]["browser"] == "chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
            return driver
        elif config["config"][0]["browser"] == "safari":
            driver = webdriver.Safari()
            return driver
        raise Exception("Provide valid driver name")




