from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import Login

class Society_Societydetails:
    """
    Class to interact with the Society Details page in the application.
    """

    def __init__(self,driver):
        """

        :param driver: an instance of webdriver.
        """
        self.driver=driver

    def society_list(self):
        """
         Navigates to the 'Society List' section and verifies its details.
        """
        wait=WebDriverWait(self.driver,40)

        try:
            # click on society link
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Society']"))).click()

            # click on society details
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/home/view/Society_Details']"))).click()

            # Switch to main iframe containing society details
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Society_Details']")))

            # get the text from the header
            text = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@class='page-header']"))).text

            if text == "Society List":
                print("successfully displayed the correct society details")

        except Exception as e:
            print(f"Error while accessing society list: {e}")



if __name__ == "__main__":

    login_page= Login("sekhar481@gmail.com", "Jahnavi@16")
    driver = login_page.launch_browser()
    login_page.login(driver)

    s=Society_Societydetails(driver)
    s.society_list()






