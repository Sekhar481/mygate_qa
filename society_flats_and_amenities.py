import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class Society_Flats_And_Amenities:
    """
     Automates the 'Flats & Amenities' section in the MyGate dashboard.
    """
    def __init__(self,driver):
        self.driver=driver


    def add_flat(self,floor_no, flat_no, phone_extension, e_intercom, secondary_phone_no):
        """
        Fills and submits the 'Add Flat' form on the MyGate dashboard.
            :param floor_no: The floor number of the flat.
            :param flat_no: The flat number.
            :param phone_extension: The phone extension number.
            :param e_intercom: The primary e-intercom number.
            :param secondary_phone_no: The secondary contact number.
        """
        wait = WebDriverWait(self.driver, 40)

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
            self.driver.switch_to.default_content()
            time.sleep(2)
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Flats']")))

            # Select building number
            building = wait.until(EC.element_to_be_clickable((By.ID, "edit-building")))
            Select(building).select_by_visible_text(input("Enter the preferred building: "))

            # Enter floor number
            wait.until(EC.element_to_be_clickable((By.ID, "edit-floor-number"))).send_keys(floor_no)

            # Enter flat number
            wait.until(EC.element_to_be_clickable((By.ID, "edit-flatnumber"))).send_keys(flat_no)

            # Select flat type
            flat_type = wait.until(EC.element_to_be_clickable((By.ID, "edit-flattype")))
            Select(flat_type).select_by_visible_text(input("Enter the preferred flat type: "))

            # Enter phone extension
            wait.until(EC.element_to_be_clickable((By.ID, "edit-phoneextension"))).send_keys(phone_extension)

            # Select occupant type (corrected ID)
            occupant_type = wait.until(EC.element_to_be_clickable((By.ID, "edit-occupanttype")))
            Select(occupant_type).select_by_visible_text(input("Enter the preferred occupant type: "))

            # Enter e-Intercom number
            wait.until(EC.element_to_be_clickable((By.ID, "edit-primary-contact-number"))).send_keys(e_intercom)

            # Enter secondary contact number
            wait.until(EC.element_to_be_clickable((By.ID, "edit-secondary-contact-number"))).send_keys(secondary_phone_no)

            print("Flat details added successfully.")
        except Exception as e:
            print(print("Failed to add flat:", str(e)))


    def add_non_member(self,non_member_name):
        """
        Adds a non-member in the Flats & Amenities section.

        :param non_member_name: The name of the non-member to be added.
        """
        wait = WebDriverWait(self.driver, 40)

        try:
            # Click on Society link
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Society']"))).click()

            # Click on Flats & Amenities link
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@href='/home/view/Flats']"))).click()

            # Switch to main iframe containing 'Add non-member' link
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Flats']")))

            # Click on "+ Add non-member" link
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/society/flat/add?building_type=N&navbar=1&society=707']"))).click()

            # Wait for a second iframe (Add non-member form) and switch if needed
            self.driver.switch_to.default_content()
            time.sleep(2)
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Flats']")))

            # Select building name
            building_name = wait.until(EC.element_to_be_clickable((By.ID, "edit-building")))
            Select(building_name).select_by_visible_text("Non Members")

            #enter the non-member name
            wait.until(EC.element_to_be_clickable((By.ID, "edit-flatnumber"))).send_keys(non_member_name)

            print("non-member details added successfully")
        except Exception as e:
            print("Failed to add non-member:", str(e))

    def add_amenity(self,amenity_name):
        """
        Adds an amenity in the Flats & Amenities section.

        :param amenity_name: The name of the amenity to be added.
        """
        wait = WebDriverWait(self.driver, 40)

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
            self.driver.switch_to.default_content()
            time.sleep(2)
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Flats']")))


            #enter the amenity name
            wait.until(EC.element_to_be_clickable((By.ID, "edit-flatnumber"))).send_keys(amenity_name)
            time.sleep(3)

            print("amenity details added successfully")
        except Exception as e:
            print("Failed to add amenity:", str(e))

    def flat_search(self, building,flat,flat_type,occupant_type,flat_status,quarantine_status ):
        """
               Searches for a flat based on the provided filters.

               :param building:The building number.
               :param flat: The specific flat identifier.
               :param flat_type: The type of flat.
               :param occupant_type: The type of occupant.
               :param flat_status: The status of the flat.
               :param quarantine_status: The quarantine status of the flat.
        """
        wait = WebDriverWait(self.driver, 40)
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
            building_number= wait.until(EC.element_to_be_clickable((By.ID, "edit-building")))
            Select(building_number).select_by_visible_text(building)
            time.sleep(10)

            # Enter flat
            flat_number= wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='edit-flat--2']")))
            Select(flat_number).select_by_visible_text(flat)

            # Select flat type
            flat_types = wait.until(EC.element_to_be_clickable((By.ID, "edit-type")))
            Select(flat_types).select_by_visible_text(flat_type)

            # Select occupant type
            occupant_types = wait.until(EC.element_to_be_clickable((By.ID, "edit-occupant")))
            Select(occupant_types).select_by_visible_text(occupant_type)

            # select flat status
            flat_status1 = wait.until(
                EC.element_to_be_clickable((By.XPATH, "(//select[@class='select form-control form-select'])[3]")))
            Select(flat_status1).select_by_visible_text(flat_status)

            # select quarantine status
            quarantine_status1= wait.until(EC.element_to_be_clickable((By.ID, "edit-quarantine-status")))
            Select(quarantine_status1).select_by_visible_text(quarantine_status)

            # click on search button
            wait.until(EC.element_to_be_clickable((By.ID, "edit-submit"))).click()
            print("search successful.")
            time.sleep(3)

        except Exception as e:
            print("Search failed:", str(e))

    def flat_reset_search(self, building,flat,flat_type,occupant_type,flat_status,quarantine_status ):
        """
               Resets the flat search form.

               :param building:The building number.
               :param flat: The specific flat identifier.
               :param flat_type: The type of flat.
               :param occupant_type: The type of occupant.
               :param flat_status: The status of the flat.
               :param quarantine_status: The quarantine status of the flat.
        """
        wait = WebDriverWait(self.driver, 40)
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
            building_number= wait.until(EC.element_to_be_clickable((By.ID, "edit-building")))
            Select(building_number).select_by_visible_text(building)
            time.sleep(10)

            # Enter flat
            flat_number= wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='edit-flat--2']")))
            Select(flat_number).select_by_visible_text(flat)

            # Select flat type
            flat_types = wait.until(EC.element_to_be_clickable((By.ID, "edit-type")))
            Select(flat_types).select_by_visible_text(flat_type)

            # Select occupant type
            occupant_types = wait.until(EC.element_to_be_clickable((By.ID, "edit-occupant")))
            Select(occupant_types).select_by_visible_text(occupant_type)

            # select flat status
            flat_status1 = wait.until(
                EC.element_to_be_clickable((By.XPATH, "(//select[@class='select form-control form-select'])[3]")))
            Select(flat_status1).select_by_visible_text(flat_status)

            # select quarantine status
            quarantine_status1= wait.until(EC.element_to_be_clickable((By.ID, "edit-quarantine-status")))
            Select(quarantine_status1).select_by_visible_text(quarantine_status)

            # click on reset search button
            wait.until(EC.element_to_be_clickable((By.ID, "edit-cancel"))).click()
            time.sleep(3)

            print("reset search is successful")

        except Exception as e:
            print("Reset failed:", str(e))


