from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time
from login_page import Login


class Buildings:
    """
    A class to handle interactions on the Buildings page in the MyGate application.
    """
    def __init__(self,driver):
        """
        Initializes the Buildings page handler
        :param driver: an instance of webdriver.
        """
        self.driver=driver

    def building_list(self, option):
        """
        Filters the dashboard by selecting a building from the dropdown.

        :param option: The name of the building to be selected from the dropdown.

        """
        wait = WebDriverWait(self.driver, 40)

        try:
            # Click on Society link
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Society']"))).click()

            # Click on Buildings link
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/home/society/building']"))).click()

            # Open the building dropdown
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "//div[@class='MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input']"))).click()

            # extract the xpath to select the preferred option
            option_xpath = f"//li[.//span[normalize-space(text())='{option}']]"
            # check the preferred option is located
            wait.until(EC.presence_of_element_located((By.XPATH, option_xpath)))
            # click on the preferred option
            wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath))).click()

            # Fallback to click top-left of the page
            ActionChains(self.driver).move_by_offset(0, 0).click().perform()

            # Click the Submit button
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-outlined mgbutton gradient2 adjustWidth   MuiButton-outlinedPrimary']"))).click()
            time.sleep(10)
            print("Successfully filtered the dashboard using building")

        except Exception as e:
            print(f"Failed to filter buildings: {e}")


if __name__ == "__main__":

    login_page= Login("sekhar481@gmail.com", "Jahnavi@16")
    driver = login_page.launch_browser()
    login_page.login(driver)

    b=Buildings(driver)
    b.building_list("I")








