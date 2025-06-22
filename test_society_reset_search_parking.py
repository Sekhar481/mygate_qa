from login_page import Login
from society_parking_list import Society_Parking

if __name__ == "__main__":
    login_page = Login("sekhar481@gmail.com", "Jahnavi@16")
    driver = login_page.launch_browser()
    login_page.login(driver)

    # object creation for society parking
    parking = Society_Parking(driver)
    # calling the reset search parking function
    parking.reset_search_parking("I","122-FF","I-122-FF")