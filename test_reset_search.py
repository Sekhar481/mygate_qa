import time
from login_page import Login
from user_registration_request import Userregistrationresident

def test_reset_search():
    """
    Test case for resetting the search form on the UnRegistered Residents page.
    """
    # Initialize and login
    login_page = Login("sekhar481@gmail.com", "Jahnavi@16")
    driver = login_page.launch_browser()
    login_page.login()
    # Fill and reset the search form
    registration = Userregistrationresident("Nishitha", "9876543210", "test@example.com", "Owner")
    registration.reset_search(driver)
    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    test_reset_search()
