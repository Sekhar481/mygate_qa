import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from login_page import Login

class Add_flat:
    def __init__(self, floor_no, flat_no, phone_extension, e_intercom, secondary_phone_no):
        self.floor_no = floor_no
        self.flat_no = flat_no
        self.phone_extension = phone_extension
        self.e_intercom = e_intercom
        self.secondary_phone_no = secondary_phone_no

    def add_flat(self, driver):
        wait = WebDriverWait(driver, 40)

        try:
            # Click on Society link
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Society']"))).click()

            # Click on Flats & Amenities link
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@href='/home/view/Flats']"))).click()

            # Optional sleep if iframe takes time to load
            time.sleep(3)

            # Switch to main iframe containing 'Add Flat' button
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Flats']")))

            # Click on "+ Add Flat" button
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-primary form-submit']"))).click()

            # Wait for a second iframe (Add Flat form) and switch if needed
            driver.switch_to.default_content()
            time.sleep(2)
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Flats']")))

            # Select building number
            building = wait.until(EC.element_to_be_clickable((By.ID, "edit-building")))
            Select(building).select_by_visible_text(input("Enter the preferred building: "))

            # Enter floor number
            wait.until(EC.element_to_be_clickable((By.ID, "edit-floor-number"))).send_keys(self.floor_no)

            # Enter flat number
            wait.until(EC.element_to_be_clickable((By.ID, "edit-flatnumber"))).send_keys(self.flat_no)

            # Select flat type
            flat_type = wait.until(EC.element_to_be_clickable((By.ID, "edit-flattype")))
            Select(flat_type).select_by_visible_text(input("Enter the preferred flat type: "))

            # Enter phone extension
            wait.until(EC.element_to_be_clickable((By.ID, "edit-phoneextension"))).send_keys(self.phone_extension)

            # Select occupant type (corrected ID)
            occupant_type = wait.until(EC.element_to_be_clickable((By.ID, "edit-occupanttype")))
            Select(occupant_type).select_by_visible_text(input("Enter the preferred occupant type: "))

            # Enter e-Intercom number
            wait.until(EC.element_to_be_clickable((By.ID, "edit-primary-contact-number"))).send_keys(self.e_intercom)

            # Enter secondary contact number
            wait.until(EC.element_to_be_clickable((By.ID, "edit-secondary-contact-number"))).send_keys(self.secondary_phone_no)

            print("Flat details added successfully.")
        except Exception:
            print(False)

if __name__ == "__main__":
    login_page = Login("sekhar481@gmail.com", "Jahnavi@16")
    driver = login_page.launch_browser()
    login_page.login(driver)

    a = Add_flat("1", "122", "+91", "9381991558", "8686479756")
    a.add_flat(driver)
