import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class SocietyVehicleList:

    def __init__(self,driver):
        self.driver=driver

    def vehicle_list(self,vehicle_number):
        wait=WebDriverWait(self.driver,40)
        # click on society link
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Society']"))).click()

        # click on parking dropdown
        wait.until(EC.element_to_be_clickable((By.XPATH,"(//div[@class='MuiButtonBase-root MuiListItem-root sidebar_list_item  MuiListItem-gutters MuiListItem-button'])[1]']"))).click()

        # click on vehicle list option
        wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@href='/home/society/vehicleList']")))

        # enter the vehicle number to search
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Vehicle Number']"))).send_keys(vehicle_number)
