from login_page import Login
from residents_list_page import Residentslist
import time

def test_upload_resident_data():
    login = Login("sekhar481@gmail.com", "Jahnavi@16")
    driver = login.launch_browser()
    login.login()

    resident = Residentslist()
    resident.upload_resident_data(driver)

    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    test_upload_resident_data()

