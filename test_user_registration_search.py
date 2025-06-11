import time
from login_page import Login
from user_registration_request import Userregistrationresident
def test_user_registration_search():
    """
    Test case for performing a search for an unregistered resident in the People Hub.
    """
    # Initialize and login
    login_page = Login("sekhar481@gmail.com", "Jahnavi@16")
    driver = login_page.launch_browser()
    login_page.login()
    # Perform user registration search
    registration = Userregistrationresident("Nishitha", "9876543210", "test@example.com", "Owner")
    registration.user_registration_search(driver)
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    test_user_registration_search()