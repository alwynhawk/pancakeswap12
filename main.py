from selenium import webdriver
import time
import pyautogui
import pywinauto
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")
options.add_argument(r"user-data-dir=C:\Users\oweno\AppData\Local\Google\Chrome\User Data")
options.add_argument(r"--profile-directory=Profile 2")
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe', options=options)
driver.switch_to.window(driver.window_handles[1])
i = 1
total = 100
def timer():


    while i == 1:


        timer = driver.find_element_by_xpath\
            ("/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div/div[1]/div[3]/div/div[1]/div/div[1]/div[1]")

        def get_sec(time_str):
            """Get Seconds from time."""
            try:
                m, s = time_str.split(':')
            except:
                print("exeption")
                return int(m) * 60 + int(s)


        total = (get_sec(timer.text))
        print(total)


        if total < 1000:

            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)

            upTrend = \
                driver.find_element_by_xpath \
                    ("/html/body/div[2]/div[5]/div/div[1]/div[1]/div[5]/div/div[2]/div[1]/div[4]/div[2]/div[1]/div[2]")

            downTrend = \
                driver.find_element_by_xpath \
                    ("/html/body/div[2]/div[5]/div/div[1]/div[1]/div[5]/div/div[2]/div[1]/div[4]/div[2]/div[2]/div[2]")

            u = False
            d = False

            if (upTrend.text != "n/a"):
                print("up")
                u = True

            if (downTrend.text != "n/a"):
                print("down")
                d = True

            driver.switch_to.window(driver.window_handles[1])


            if (d == True):
                EnterDown = driver.find_elements_by_xpath("//*[contains(text(), 'Enter DOWN')]")[0]
                EnterDown.click()
                time.sleep(1)
                pyautogui.moveTo(x=1273, y=574)

                pyautogui.click()

                pyautogui.write(".001").001

                pyautogui.moveTo(x=1269, y=755)

                pyautogui.click()

            if (u == True):
                EnterUp = driver.find_elements_by_xpath("//*[contains(text(), 'Enter UP')]")[0]
                EnterUp.click()
                time.sleep(1)
                pyautogui.moveTo(x=1273, y=574)

                pyautogui.click()

                pyautogui.write(".001")

                pyautogui.moveTo(x=1269, y=755)

                pyautogui.click()

                pyautogui.moveTo(x=1912, y=562)

                pyautogui.click()

                pyautogui.moveTo(x=1817, y=566)

                pyautogui.click()

if __name__ == '__main__':
    timer()