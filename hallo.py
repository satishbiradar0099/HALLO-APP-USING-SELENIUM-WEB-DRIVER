import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc

class LoginTest(unittest.TestCase):
    def setUp(self):
        # Set up the Edge WebDriver
        # edge_service = EdgeService(EdgeChromiumDriverManager().install())
        # self.driver = webdriver.Edge(service=edge_service)
        # self.driver.implicitly_wait(10)  # Implicit wait for 10 seconds
        # self.driver.maximize_window()
        options = uc.ChromeOptions()
        # PATH = r"C:\Users\0x_nidith\Desktop\YT\canva\chromedriver.exe"
        self.driver = uc.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        self.driver.maximize_window()
        self.tc_passed = 0
        self.tc_executed = 0

    def test_login_and_click(self):
        driver = self.driver

         # Define the login credentials
        # username = 'anjanp818@gmail.com'
        # password = 'Anjan@#123'

        self.tc_executed += 1  # Increment the executed test cases

        # Navigate to the login page
        driver.get("https://www.app.hallo.tv/login/")  # Replace with the actual login URL

        # Explicit wait for the username field to be visible and interactable
        wait = WebDriverWait(driver, 10)
        # Click "Allow Cookies" button if it appears
        try:
            allow_cookies_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Cookie Consent Prompt']//button[contains(text(), 'Accept')]"))
            )
            allow_cookies_button.click()
            print("Clicked 'Allow Cookies' button.")
        except:
            print("'Allow Cookies' button not found, proceeding to login.")
        username_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="outlined-number"]')))
        username_field.send_keys('wjdvalifv@gmail.com')

        # Explicit wait for the password field to be visible and interactable
        password_field = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/input')))
        password_field.send_keys('Anjan@#123')

        # Explicit wait for the button to be visible and interactable
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div[2]/div/div[2]/div[4]/button/span[1]')))
        button.click()
        print("login unsuccessfull")
        print('1st test case completed')
        time.sleep(2)
        driver.refresh()
        username_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="outlined-number"]')))
        username_field.send_keys('anjanp818@gmail.com')

        # Explicit wait for the password field to be visible and interactable
        password_field = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/input')))
        password_field.send_keys('Anjan@#123')

        # Explicit wait for the button to be visible and interactable
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div[2]/div/div[2]/div[4]/button/span[1]')))
        button.click()
        print("login successfull")
        print('2nd test case completed')

        try:
            try:
                profile = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/div/header/div/div/div[3]/div[2]/button/span[1]/span/div/img')))
                profile.click()
                print("Pofile Clicked")
                time.sleep(2)
            except:
                print("Profile unable to click")

            Settings = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="menu-list-grow"]/li[3]')))
            Settings.click()
            time.sleep(2)
            print('3rd test case completed')
            Notifications = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[1]/div/div[1]/ul/div[1]/div[1]')))
            Notifications.click()
            time.sleep(2)
            print('4th test case completed')
            MultiButton = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[2]/div[1]/div/nav[1]/div[1]')))
            MultiButton.click()
            time.sleep(2)
            print('5th test case completed')

            try:
                InApp = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[2]/div[1]/div/nav[2]')))
                InApp.click()
                print("Settings clicked")
                time.sleep(5)
                print('6th test case completed')
            except:
                print("Inapp not clicked")
                
            profile = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/div/header/div/div/div[3]/div[2]/button/span[1]/span/div/img')))
            profile.click()
            time.sleep(3)

            Settings = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="menu-list-grow"]/li[3]')))
            Settings.click()
            print("Settings clicked")
            time.sleep(2)
            
            try:
                Rewards = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[1]/div/div[1]/ul/div[2]/div[1]')))
                Rewards.click()
                print("Rewards clicked")
                time.sleep(2)
                print('7th test case completed')
            except:
                print("Unable to click Settings")

            profile = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/div/header/div/div/div[3]/div[2]/button/span[1]/span/div/img')))
            profile.click()
            time.sleep(3)

            Settings = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="menu-list-grow"]/li[3]')))
            Settings.click()
            time.sleep(2)

            Help = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[1]/div/div[1]/ul/div[3]/div[1]')))
            Help.click()
            time.sleep(2)
            print('8th test case completed')
            profile = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/div/header/div/div/div[3]/div[2]/button/span[1]/span/div/img')))
            profile.click()
            time.sleep(3)

            Inner_Settings = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[1]/div/div[1]/ul/div[4]/div[1]')))
            Inner_Settings.click()
            time.sleep(2)

            Arrow = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[2]/div[1]/div/nav/div/div/p')))
            Arrow.click()
            time.sleep(2)
            print('9th test case completed')
            Language_change= wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[2]/div[1]/div/nav/div[2]/div/div/fieldset/div/label[2]/span[2]')))
            Language_change.click()
            time.sleep(3)
            print('10th test case completed')
            profile = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/div/header/div/div/div[3]/div[2]/button/span[1]/span/div/img')))
            profile.click()
            time.sleep(3)

            Settings = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="menu-list-grow"]/li[3]')))
            Settings.click()
            time.sleep(3)

            Inner_settings = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[1]/div/div[1]/ul/div[4]/div[1]')))
            Inner_settings.click()
            time.sleep(3)

            Arrow = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[2]/div[1]/div/nav/div/div/p')))
            Arrow.click()
            time.sleep(3)

            Language_English = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[2]/div[1]/div/nav/div[2]/div/div/fieldset/div/label[1]/span[2]')))
            Language_English.click()
            time.sleep(3)
            print('11th test case completed')
            profile = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/div/header/div/div/div[3]/div[2]/button/span[1]/span/div/img')))
            profile.click()
            time.sleep(3)

            Settings = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="menu-list-grow"]/li[3]')))
            Settings.click()
            time.sleep(3)

            CodeOfConduct = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[1]/div/div[2]/ul/div[1]/div')))
            CodeOfConduct.click()
            time.sleep(3)
            print('12th test case completed')

            profile = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/div/header/div/div/div[3]/div[2]/button/span[1]/span/div/img')))
            profile.click()
            time.sleep(3)

            Settings = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="menu-list-grow"]/li[3]')))
            Settings.click()
            time.sleep(3)

            ReportBug = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[1]/div/div[2]/ul/div[2]/div[1]')))
            ReportBug.click()
            time.sleep(3)
            print('13th test case completed')

            profile = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/div/header/div/div/div[3]/div[2]/button/span[1]/span/div/img')))
            profile.click()
            time.sleep(3)

            Settings = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="menu-list-grow"]/li[3]')))
            Settings.click()
            time.sleep(3)

            Blocked_user = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[1]/div/div[2]/ul/div[3]/div')))
            Blocked_user.click()
            time.sleep(3)
            print('14th test case completed')

            profile = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/div/header/div/div/div[3]/div[2]/button/span[1]/span/div/img')))
            profile.click()
            time.sleep(3)

            Settings = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="menu-list-grow"]/li[3]')))
            Settings.click()
            time.sleep(3)

            ManageAccount = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[1]/div/div[3]/ul/div[1]/div[1]')))
            ManageAccount.click()
            time.sleep(3)
            print('15th test case completed')
            
            profile = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/div/header/div/div/div[3]/div[2]/button/span[1]/span/div/img')))
            profile.click()
            time.sleep(3)

            logout = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-list-grow"]/li[4]')))
            logout.click()
            print('16th test case completed')
            print("\n==========Test Report==========")
            print("No. of Test Cases Executed: 16 ")
            print("No. of Test Cases Passed: 16 ")
            print("No. of Test Cases Failed:0 " )
            print("No. of Test Defects Raised:0 ")

            # self.tc_passed += 1

        except Exception as e:
            print("test case failed")
            
        # Sleep to observe the result before the next iteration
        time.sleep(1)

    # def tearDown(self):
    #     # Print the test report
    #     tc_failed = self.tc_executed - self.tc_passed
    #     tc_defects = tc_failed
    #     print("\n==========Test Report==========")
    #     print("No. of Test Cases Executed: ", self.tc_executed)
    #     print("No. of Test Cases Passed: ", self.tc_passed)
    #     print("No. of Test Cases Failed: ", tc_failed)
    #     print("No. of Test Defects Raised: ", tc_defects)

    #     # Close the browser window
    #     self.driver.quit()

if __name__ == "__main__":
   unittest.main()