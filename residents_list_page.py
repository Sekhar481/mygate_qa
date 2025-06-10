from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


class Residentslist:
    """
    Represents a resident with personal and contact information.
    Provides functionality to add a resident using a web interface.
    """
    def __init__(self, name='', mobile='', mail='', landline='', address='', pincode='', id_no=''):
        """
        Initializes a Residents instance.
        :param name: str -> Name of the resident
        :param mobile: str -> Mobile number
        :param mail: str -> Email address
        :param landline: str -> Landline number
        :param address: str -> Address of the resident
        :param pincode: str -> Area pincode
        :param id_no: str -> ID number
        """
        self.name = name
        self.mobile = mobile
        self.mail = mail
        self.landline = landline
        self.address = address
        self.pincode = pincode
        self.id_no = id_no

    def add_resident(self, driver):
        """
        Automates the process of adding a resident using Selenium WebDriver.
        Navigates through the interface, fills out the form, and uploads documents.
        :param driver: A Selenium WebDriver.
        """

        wait = WebDriverWait(driver, 50)
        try:
            # Click on People Hub
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='People Hub']"))).click()
            # Click on Residents
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='MuiButtonBase-root MuiListItem-root sidebar_list_item  MuiListItem-gutters MuiListItem-button'][1]"))).click()
            # Click on Resident List
            wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Resident List']"))).click()
            time.sleep(10)

            # Switch to iframe and click on Add Resident button
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Residents_ResidentList']")))

            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-primary form-submit']"))).click()
            time.sleep(5)
            # Switch back to default content and again into iframe
            driver.switch_to.default_content()
            WebDriverWait(driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Residents_ResidentList']")))
            # Fill Resident Form
            # Select building name
            building = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@name='building']"))))
            building.select_by_visible_text("I")
            # Select flat number
            flat = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='edit-flat-number--2']"))))
            flat.select_by_visible_text("122-FF")
            # Select User type
            user = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='edit-user-type']"))))
            user.select_by_visible_text("Owner")
            # Enter name
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='edit-name']"))).send_keys(self.name)
            # Enter Phone number
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='edit-mobile']"))).send_keys(self.mobile)
            # Enter Email
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='edit-email']"))).send_keys(self.mail)
            # Enter landline
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='edit-landline']"))).send_keys(self.landline)
            #
            status = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//Select[@id='edit-status--2']"))))
            status.select_by_visible_text("Residing")
            # Address
            wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@id='edit-address']"))).send_keys(self.address)
            # Country
            country = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='edit-country']"))))
            country.select_by_visible_text("India")
            # State
            state = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[ @ id = 'edit-state--2']"))))
            state.select_by_visible_text("Andhra Pradesh")
            # City
            city = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='edit-city--2']"))))
            city.select_by_visible_text("Kadapa")
            # pincode
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='edit-pincode']"))).send_keys(self.pincode)
            # photograph
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='edit-upload-photograph']"))).send_keys(r"C:\Users\nishithasetipalli\Downloads\Nishitha.jpg")
            time.sleep(5)
            # id type
            id = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='edit-id-type']"))))
            id.select_by_visible_text("Aadhar Card")
            # id number
            wait.until(EC.presence_of_element_located((By.ID, "edit-id-number"))).send_keys(self.id_no)
            # attachment
            wait.until(EC.presence_of_element_located((By.ID, "edit-doc-attachment"))).send_keys(r"C:\Users\nishithasetipalli\Downloads\Nishitha_Y.pdf")
            time.sleep(10)
            print("Resident added successfully")

        except Exception as e:
            print(f"Failed to add resident: {e}")

    def search_resident(self, driver):
        """
        Automates the search for a resident.
        Navigates through the UI, fills in the search form with the resident's data,
        and performs a search and then resets the form.
        :param driver: An instance of Selenium WebDriver.
        """

        wait = WebDriverWait(driver, 50)
        try:
            # Click on People Hub
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='People Hub']"))).click()
            # Click on Residents
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "//div[@class='MuiButtonBase-root MuiListItem-root sidebar_list_item  MuiListItem-gutters MuiListItem-button'][1]"))).click()
            # Click on Residents list
            wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Resident List']"))).click()
            time.sleep(10)

            # Wait until the iframe is available
            WebDriverWait(driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Residents_ResidentList']")))
            # Select building
            building = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='edit-building']"))))
            building.select_by_visible_text("I")
            #  Select flat
            flat = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='edit-flat--2']"))))
            flat.select_by_visible_text("122-FF")
            # Select on status
            status = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='edit-status']"))))
            status.select_by_visible_text("Active")
            # Select user type
            user = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='edit-occupant']"))))
            user.select_by_visible_text("Owner")
            # Enter name
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='edit-name']"))).send_keys(self.name)
            # Enter mobile
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='edit-mobile']"))).send_keys(self.mobile)
            # Enter email
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='edit-email']"))).send_keys(self.mail)
            # Click on Search
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='edit-submit']"))).click()

            # reset search
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='edit-cancel']"))).click()

            print("Resident search completed successfully.")

        except Exception as e:
            print(f"An error occured while searching resident: {e}")

    def upload_resident_data(self, driver):
        """
        Automates the process of uploading resident data from an Excel file
        by interacting with the web interface through Selenium.
        :param driver: The Selenium WebDriver
        """

        wait = WebDriverWait(driver, 50)
        try:
            # Click on People Hub
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='People Hub']"))).click()
            # Click on Residents
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "//div[@class='MuiButtonBase-root MuiListItem-root sidebar_list_item  MuiListItem-gutters MuiListItem-button'][1]"))).click()
            # Click on Resident list
            wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Resident List']"))).click()
            time.sleep(10)

            # Switch to iframe and click on Add Resident button
            WebDriverWait(driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Residents_ResidentList']")))

            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-success']"))).click()
            time.sleep(5)

            driver.switch_to.default_content()

            WebDriverWait(driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Residents_ResidentList']")))

            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='edit-sub-file']"))).send_keys(r"C:\Users\nishithasetipalli\Downloads\Data.xlsx")
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='edit-submit']"))).click()
            time.sleep(10)
            print("Successfully uploaded resident data")

        except Exception as e:
            print(f"Failed to upload resident data: {e}")
