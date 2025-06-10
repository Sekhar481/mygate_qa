from login_page import Login
from society_flats_and_amenities import Society_Flats_And_Amenities

if __name__ == "__main__":
    login_page = Login("sekhar481@gmail.com", "Jahnavi@16")
    driver = login_page.launch_browser()
    login_page.login(driver)

    #object creation for society_flats & amenities.
    society = Society_Flats_And_Amenities(driver)
    #calling the add_flat fuction
    society.add_flat("1", "122", "+91", "9381991558", "8686479756")
