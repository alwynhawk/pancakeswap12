#imports
from selenium import webdriver
import time
import pyautogui
import pywinauto
from pynput.mouse import Controller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
#options for selenium
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")
options.add_argument(r"user-data-dir=C:\Users\oweno\AppData\Local\Google\Chrome\User Data")
options.add_argument(r"--profile-directory=Profile 2")
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe', options=options)
#infinite while loop
def findtrend():
    i = 1
    while i < 2:
        #switches to supertrend
        driver.switch_to.window(driver.window_handles[0])
        #sleep for 2 seconds
        time.sleep(2)
        # current screen resolution width and height
        pyautogui.size()
        (1920, 1080)
        #decids if graph is going to be up or down
        upTrend = \
            driver.find_element_by_xpath \
                ("/html/body/div[2]/div[5]/div/div[1]/div[1]/div[5]/div/div[2]/div[1]/div[4]/div[2]/div[1]/div[2]")

        downTrend = \
            driver.find_element_by_xpath \
                ("/html/body/div[2]/div[5]/div/div[1]/div[1]/div[5]/div/div[2]/div[1]/div[4]/div[2]/div[2]/div[2]")
        #creates variables to store if its up or down
        u = False
        d = False

        if(upTrend.text != "n/a"):
            print("up")
            u = True




        if(downTrend.text != "n/a"):
            print("down")
            d = True
        #sleeps for a bit
        time.sleep(1)
        #switch to pancakeswap
        driver.switch_to.window(driver.window_handles[1])
        #sleeps for a bit
        time.sleep(1)
        #checks what the timer is at
        timer = driver.find_element_by_xpath\
            ("/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div/div[1]/div[3]/div/div[1]/div/div[1]/div[1]")
        print(timer.text)

        def get_sec(time_str):
            """Get Seconds from time."""
            m, s = time_str.split(':')
            return int(m) * 60 + int(s)


        total = (get_sec(timer.text))

        if(total < 10):
            pyautogui.moveTo(960, 383)
            pyautogui.click()

            if(d == True):

                EnterDown = driver.find_elements_by_xpath("//*[contains(text(), 'Enter DOWN')]")[0]
                EnterDown.click()
                time.sleep(1)
                pyautogui.moveTo(x=1273, y=574)

                pyautogui.click()

                pyautogui.write(".001")

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

                pyautogui.moveTo(x=1912,y=562)

                pyautogui.click()

                pyautogui.moveTo(x=1817, y=566)

                pyautogui.click()
        print(total)






if __name__ == '__main__':
    findtrend()