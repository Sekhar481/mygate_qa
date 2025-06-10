from login_page import Login
from residents_list_page import Residentslist
import time

def test_search_resident():
    login = Login("sekhar481@gmail.com", "Jahnavi@16")
    driver = login.launch_browser()
    login.login()

    resident = Residentslist(name="Sekhar Reddy", mobile="8897201383", mail="sekhar481@gmail.com")
    resident.search_resident(driver)
    time.sleep(5)

if __name__ == "__main__":
    test_search_resident()