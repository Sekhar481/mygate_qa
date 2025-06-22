import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class Society_Parking:
    """
    Class to interact with the Society Parking section of the application.
    """

    def __init__(self,driver):
        """

        :param driver: an instance of webdriver.
        """
        self.driver=driver

    def search_parking(self,building_number,flat_number,parking_name):
        """
        Searches for a parking entry based on building, flat, and parking name.

        :param building_number: Building number to filter the parking list.
        :param flat_number: Flat number to filter the parking list.
        :param parking_name: Name of the parking to search for.
        """
        wait=WebDriverWait(self.driver,40)

        try:
            # click on society link
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Society']"))).click()

            # click on parking dropdown
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "(//div[@class='MuiButtonBase-root MuiListItem-root sidebar_list_item  MuiListItem-gutters MuiListItem-button'])[1]']"))).click()

            # click on parking list option
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/home/view/Parking_List']"))).click()

            # Switch to main iframe containing 'Add parking' button
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Parking_List']")))

            time.sleep(10)

            # select the preferred option from the building dropdown
            building = wait.until(EC.element_to_be_clickable((By.ID, "edit-building")))
            Select(building).select_by_visible_text(building_number)

            # select the preferred option from the flat dropdown
            flat = wait.until(EC.element_to_be_clickable((By.ID, "edit-flat--2")))
            Select(flat).select_by_visible_text(flat_number)

            # enter the parking name
            wait.until(EC.element_to_be_clickable((By.ID, "edit-parkingname"))).send_keys(parking_name)

            # click on search button
            wait.until(EC.element_to_be_clickable((By.ID, "edit-submit"))).click()
            print("search is successful")

        except Exception as e:
            print(f"failed to search : {e}")




    def reset_search_parking(self,building_number,flat_number,parking_name):
        """
         Resets the search filters used to find parking entries.

         :param building_number: Building number used in search.
         :param flat_number: Flat number used in search.
         :param parking_name: Parking name used in search.
         """

        wait = WebDriverWait(self.driver, 40)

        try:
            # click on society link
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Society']"))).click()

            # click on parking dropdown
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "(//div[@class='MuiButtonBase-root MuiListItem-root sidebar_list_item  MuiListItem-gutters MuiListItem-button'])[1]"))).click()

            # click on parking list option
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/home/view/Parking_List']"))).click()

            # Switch to main iframe containing 'Add parking' button
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Parking_List']")))

            time.sleep(10)

            # select the preferred option from the building dropdown
            building = wait.until(EC.element_to_be_clickable((By.ID, "edit-building")))
            Select(building).select_by_visible_text(building_number)

            # select the preferred option from the flat dropdown
            flat = wait.until(EC.element_to_be_clickable((By.ID, "edit-flat--2")))
            Select(flat).select_by_visible_text(flat_number)

            # enter the parking name
            wait.until(EC.element_to_be_clickable((By.ID, "edit-parkingname"))).send_keys(parking_name)

            # click on reset search button
            wait.until(EC.element_to_be_clickable((By.ID, "edit-cancel"))).click()
            print("reset search is successful")

        except Exception as e:
            print(f"failed to reset the search : {e}")

    def add_parking(self, parking_name,building_number, flat_number, cars_allowed, two_wheelers_allowed, remarks):
        """
        Adds a new parking entry with the provided details.

        :param parking_name: Name of the parking slot.
        :param building_number: Building number where the parking belongs.
        :param flat_number: Flat number associated with the parking.
        :param cars_allowed: Number of cars allowed.
        :param two_wheelers_allowed: Number of two-wheelers allowed.
        :param remarks: Additional remarks or information.
        """
        wait = WebDriverWait(self.driver, 40)

        try:
            # click on society link
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Society']"))).click()

            # click on parking dropdown
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "(//div[@class='MuiButtonBase-root MuiListItem-root sidebar_list_item  MuiListItem-gutters MuiListItem-button'])[1]"))).click()

            # click on parking list option
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/home/view/Parking_List']"))).click()

            # Switch to main iframe containing 'Add parking' button
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Parking_List']")))

            # click on add parking button
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@href='/society/add/parking?navbar=1&society=707']"))).click()
            time.sleep(3)

            # switch the driver focus to the main page
            self.driver.switch_to.default_content()
            time.sleep(10)
            # again shift the driver focus to add parking page
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Parking_List']")))

            # enter the parking name
            wait.until(EC.element_to_be_clickable((By.ID, "edit-parkingname"))).send_keys(parking_name)

            # select the preferred option from the building dropdown
            building = wait.until(EC.element_to_be_clickable((By.ID, "edit-building")))
            Select(building).select_by_visible_text(building_number)

            # select the preferred option from the flat dropdown
            flat = wait.until(EC.element_to_be_clickable((By.ID, "edit-flat--2")))
            Select(flat).select_by_visible_text(flat_number)

            # enter the no.of cars allowed in the parking area
            wait.until(EC.element_to_be_clickable((By.ID, "edit-cars-allowed"))).send_keys(cars_allowed)

            # enter the no.of two_wheelers allowed in the parking area
            wait.until(EC.element_to_be_clickable((By.ID, "edit-two-wheelers-allowed"))).send_keys(two_wheelers_allowed)

            # enter the remarks
            wait.until(EC.element_to_be_clickable((By.ID, "edit-additionalinfo"))).send_keys(remarks)
            print("successfully added parking details")

        except Exception as e:
            print(f"failed to add parking details {e}")






        











