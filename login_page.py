from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class Login:
    """
    A class to handle login functionality for the MyGate dashboard.
    """
    def __init__(self,email_id,password):
        """

        :param email_id: User's email address.
        :param password: User's password.
        """
        self.email_id=email_id
        self.password=password

    def launch_browser(self):
        """
        Launches a Chrome browser in incognito mode, navigates to the login page.
        :return: An instance of Chrome WebDriver.
        """
        options = Options()
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://dashboard.mygate.com/login")
        return driver

    def login(self,driver):
        """
        Logs in to the MyGate dashboard using provided credentials and OTP.
        :param driver: An instance of Chrome WebDriver.
        """
        wait = WebDriverWait(driver, 40)
        try:
            #enter the email_id
            driver.find_element(By.ID, "email").send_keys(self.email_id)
            #enter the password
            driver.find_element(By.ID, "password").send_keys(self.password)
            #click on sign_in button
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

            #wait for 1minute to enter the otp in the prompt
            driver.implicitly_wait(60)
            otp=input("Enter the otp")
            #enter the otp
            driver.find_element(By.ID, "otp").send_keys(otp)
            #click on verify button
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
            #check the home_page is displayed or not
            element=driver.find_element(By.XPATH,"//div[text()='Concorde Silicon Valley']").text
            if element=="Concorde Silicon Valley":
                print("login successful")

        except Exception as e:
            print("login failed",str(e))



if __name__ == "__main__":
    login_page= Login("sekhar481@gmail.com", "Jahnavi@16")
    driver = login_page.launch_browser()
    login_page.login(driver)

