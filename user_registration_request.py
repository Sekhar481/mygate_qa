from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class Userregistrationresident:
    """
    Handles user registration search and reset operations for unregistered residents
    in the People Hub section.
    """
    def __init__(self, name, mobile, mail, user_type):
        """

        :param name: str ->Name of the resident.
        :param mobile: str -> Mobile number of the resident.
        :param mail: str -> Email address of the resident.
        :param user_type: str-> Type of the user e.g., Owner, Tenant.
        """
        self.name = name
        self.mobile = mobile
        self.mail = mail
        self.user_type = user_type

    def user_registration_search(self, driver):
        """
        Performs a search for unregistered resident using the provided details.
        :param driver: The Selenium WebDriver
        """
        wait = WebDriverWait(driver, 50)
        try:
            # Click on People Hub
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='People Hub']"))).click()
            # Click on Residents
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='MuiButtonBase-root MuiListItem-root sidebar_list_item  MuiListItem-gutters MuiListItem-button'][1]"))).click()
            # Click on Unregistered residents
            wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='UnRegistered Residents']"))).click()
            # Switch to iframe
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='unifiedDashboardIframe']")))
            # Enter name
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='edit-name']"))).send_keys(self.name)
            # Enter Phone number
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='edit-mobile']"))).send_keys(self.mobile)
            # Enter Email
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='edit-email']"))).send_keys(self.mail)
            # Select User type
            user_dropdown = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='edit-user-type']"))))
            user_dropdown.select_by_visible_text(self.user_type)
            # Click on Search
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='edit-submit']"))).click()
            print("Successfully searched for user registration request")

        except Exception as e:
            print(f"Failed to search user registration request:{e}")

    def reset_search(self, driver):
        """
        Resets the search form for unregistered residents.
        :param driver: Selenium WebDriver
        """
        wait = WebDriverWait(driver, 30)
        try:
            # Click on People Hub
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='People Hub']"))).click()
            # Click on Residents
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "//div[@class='MuiButtonBase-root MuiListItem-root sidebar_list_item  MuiListItem-gutters MuiListItem-button'][1]"))).click()
            # Click on Unregistered residents
            wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='UnRegistered Residents']"))).click()
            #
            WebDriverWait(driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='unifiedDashboardIframe']")))
            # Enter name
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='edit-name']"))).send_keys(self.name)
            # Enter Phone number
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='edit-mobile']"))).send_keys(self.mobile)
            # Enter Email
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='edit-email']"))).send_keys(self.mail)
            # Select User type
            user_dropdown = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='edit-user-type']"))))
            user_dropdown.select_by_visible_text(self.user_type)
            # Click on Reset
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='edit-cancel']"))).click()
            print("Successfully reset the search")

        except Exception as e:
            print(f"Failed to reset search:{e}")

