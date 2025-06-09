import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from login_page import Login


class Complaints:
    def __init__(self,subject,house_no,content):
        self.subject=subject
        self.house_no=house_no
        self.content=content

    def complaints(self,driver):

        wait = WebDriverWait(driver, 40)
        try:
            # click on the help desk button
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Help Desk']"))).click()
            # click on the complaints link
            wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Complaints']"))).click()

            # click on the raise new button
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Click to raise a new ticket']"))).click()

            # enter the subject
            wait.until(EC.presence_of_element_located(
                (By.XPATH, "//input[@class='MuiInputBase-input MuiOutlinedInput-input']"))).send_keys(self.subject)

            # send the data to the house_no drop down
            house_no = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                              "(//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiAutocomplete-input MuiAutocomplete-inputFocused MuiInputBase-inputAdornedEnd MuiOutlinedInput-inputAdornedEnd'])[3]")))
            house_no.send_keys(self.house_no)
            house_no.send_keys(Keys.ARROW_DOWN)
            house_no.send_keys(Keys.ENTER)

            # locate the category drop down
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "(//div[@class='MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input'])[6]"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-value='1459']"))).click()

            # locate the type drop down
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "(//div[@class='MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input'])[8]"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-value='personal']"))).click()

            # locate the department drop down
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "(//div[@class='MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input'])[9]"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-value='1424']"))).click()

            # enter the data to the context field
            wait.until(EC.presence_of_element_located((By.XPATH,
                                                       "//textarea[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputMultiline MuiOutlinedInput-inputMultiline']"))).send_keys(
                self.content)

            # click on calendar icon
            wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[@alt='date'])[3]"))).click()
            # click on the preferred date
            date=input("Enter the preferred date to resolve the issue")
            wait.until(EC.element_to_be_clickable((By.XPATH, f"//p[text()='{date}']"))).click()

            # click on ok button
            wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='OK']"))).click()

            # locate the prefered timming
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   "(//div[@class='MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input'])[10]"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@data-value='5958']"))).click()
            time.sleep(10)

            # select the "Is it Urgent" check box
            checkbox = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                  "//label[@class='MuiFormControlLabel-root getInput_checkbox_option']//span[contains(@class,'MuiButtonBase-root')]")))
            checkbox.click()

            # Upload file
            file = wait.until(EC.presence_of_element_located((By.ID, "uploadBtn")))
            file.send_keys("C:\\Users\\91630\\OneDrive\\Desktop\\Nikhitha_Resume.pdf")
            time.sleep(10)

            print("successfully raised a complaint")

        except Exception:
            print(False)







if __name__ == "__main__":

    login_page= Login("sekhar481@gmail.com", "Jahnavi@16")
    driver = login_page.launch_browser()
    login_page.login(driver)

    complaints=Complaints("complaint","i-122-ff","it's is very nice")
    complaints.complaints(driver)














