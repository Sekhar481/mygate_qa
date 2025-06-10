import time
from login_page import Login
from residents_list_page import Residentslist

def test_add_resident():
    # Initialize login and launch the browser
    login_page = Login("sekhar481@gmail.com", "Jahnavi@16")
    driver = login_page.launch_browser()
    login_page.login()

    # Create a Resident instance
    resident = Residentslist(
        name="Nishitha",
        mobile="9876543210",
        mail="nishitha@example.com",
        landline="08562-234567",
        address="Pullareddygari Palli, Andhra Pradesh",
        pincode="516269",
        id_no="1234-5678"
    )

    # Call the method to add a resident
    resident.add_resident(driver)

    # Close the browser
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    test_add_resident()