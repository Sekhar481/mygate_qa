import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class Buildings:
    def __init__(self,driver):
        self.driver=driver

    def building_list(self):
        wait=WebDriverWait(self.driver,40)
        try:
            # click on society button
            wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@title='Society']"))).click()
            #click on buildings link
            wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@href='/home/society/building']"))).click()
            #


