from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import Login
class Society_Gates:
    """
    Class to interact with the Society Gates section of the application.
    """

    def __init__(self,driver):
        """

        :param driver: an instance of webdriver.
        """
        self.driver=driver

    def gate_list(self):
        """
          Navigates to the Society Gates section and verifies that the gate details are displayed correctly.
        """
        wait=WebDriverWait(self.driver,40)

        try:
            # click on society link
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Society']"))).click()

            # click on gates link
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/home/society/gates']"))).click()

            # get the text from the table
            text = wait.until(EC.presence_of_element_located((By.XPATH, "//td[@title='MAIN GATE']"))).text

            if text == "MAIN GATE":
                print("successfully displayed the correct gate details")


        except Exception as e:
            print(f"Error while accessing gate list: {e}")


if __name__ == "__main__":

    login_page= Login("sekhar481@gmail.com", "Jahnavi@16")
    driver = login_page.launch_browser()
    login_page.login(driver)

    s=Society_Gates(driver)
    s.gate_list()