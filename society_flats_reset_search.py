import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from login_page import Login

class Reset:
    def __init__(self,building,flat,flat_type,occupant_type,flat_status,quarantine_status):
        self.building=building
        self.flat=flat
        self.flat_type=flat_type
        self.occupant_type=occupant_type
        self.flat_status=flat_status
        self.quarantine_status=quarantine_status

    def reset_search(self, driver):
        wait = WebDriverWait(driver, 40)
        try:

            # Click on Society link
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Society']"))).click()

            # Click on Flats & Amenities link
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@href='/home/view/Flats']"))).click()

            # Optional sleep if iframe takes time to load
            time.sleep(3)

            # Switch to main iframe containing 'search'
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Flats']")))

            # Select building number
            building = wait.until(EC.element_to_be_clickable((By.ID, "edit-building")))
            Select(building).select_by_visible_text(self.building)
            time.sleep(10)

            # Enter flat
            flat = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='edit-flat--2']")))
            Select(flat).select_by_visible_text(self.flat)

            # Select flat type
            flat_type = wait.until(EC.element_to_be_clickable((By.ID, "edit-type")))
            Select(flat_type).select_by_visible_text(self.flat_type)

            # Select occupant type
            occupant_type = wait.until(EC.element_to_be_clickable((By.ID, "edit-occupant")))
            Select(occupant_type).select_by_visible_text(self.occupant_type)

            # select flat status
            flat_status = wait.until( EC.element_to_be_clickable((By.XPATH, "(//select[@class='select form-control form-select'])[3]")))
            Select(flat_status).select_by_visible_text(self.flat_status)

            # select quarantine status
            quarantine_status = wait.until(EC.element_to_be_clickable((By.ID, "edit-quarantine-status")))
            Select(quarantine_status).select_by_visible_text(self.quarantine_status)

            #click on reset search button
            wait.until(EC.element_to_be_clickable((By.ID,"edit-cancel"))).click()
            time.sleep(3)

            print("reset search is successful")

        except Exception:
            print(False)

if __name__ == "__main__":
    login_page = Login("sekhar481@gmail.com", "Jahnavi@16")
    driver = login_page.launch_browser()
    login_page.login(driver)

    a = Reset("I","122-FF","Residential","Owner","Active","None")
    a.reset_search(driver)