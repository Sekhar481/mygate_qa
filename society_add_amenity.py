import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from login_page import Login

class Add_amenity:
    def __init__(self,amenity_name):
        self.amenity_name = amenity_name

    def add_amenity(self,driver):
        wait = WebDriverWait(driver, 40)

        try:
            # Click on Society link
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Society']"))).click()

            # Click on Flats & Amenities link
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@href='/home/view/Flats']"))).click()

            # Switch to main iframe containing 'Add non-member' link
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Flats']")))

            # Click on "+ Add amenity" link
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/society/flat/add?building_type=F&navbar=1&society=707']"))).click()

            # Wait for a second iframe (Add non-member form) and switch if needed
            driver.switch_to.default_content()
            time.sleep(2)
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Flats']")))


            #enter the amenity name
            wait.until(EC.element_to_be_clickable((By.ID, "edit-flatnumber"))).send_keys(self.amenity_name)
            time.sleep(20)

            print("amenity details added successfully")
        except Exception:
            print(False)

if __name__ == "__main__":
    login_page = Login("sekhar481@gmail.com", "Jahnavi@16")
    driver = login_page.launch_browser()
    login_page.login(driver)

    m = Add_amenity("parking")
    m.add_amenity(driver)

