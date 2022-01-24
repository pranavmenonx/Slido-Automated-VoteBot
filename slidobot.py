# Pranav Menon, Dhruv Peechara, Rohith Gowrisankar, Syam Angalakuditi
from selenium import webdriver
import time
import sys
import getopt

class SlidoBot:
    def __init__(self, hash=None, xpath=None, driver=None):
        if hash == None or xpath == None or driver == None:
            raise("Invalid arg")
        self.hash = hash
        self.xpath = xpath
        self.driver = driver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        if "chrome" in self.driver:
            self.driver = webdriver.Chrome(self.driver, chrome_options=chrome_options)
        else:
            self.driver = webdriver.Firefox(executable_path=self.driver)
    def closeBrowser(self):
        self.driver.close()

    def vote(self):
        self.driver.get("https://app.sli.do/event/"+self.hash+"/embed/polls/e96f8488-1a52-48c5-8651-1e8a55b8f462")
        time.sleep(1)
        click_elem = self.driver.find_element_by_xpath("//span[text()='insert the text of the desired choice']")
        click_elem.click()
        btn_elem = self.driver.find_element_by_xpath("//button")
        btn_elem.click()

# hash # xpath # times
def main():

    try:
        options, args = getopt.getopt(
            sys.argv[1:], "h:x:d:v:",
            ["hash=", "xpath=", "driver=", "votes="])
        for name, value in options:
            if name in ('-h', '--hash'):
                HASH = value
            if name in ('-x', '--xpath'):
                XPATH = value
            if name in ('-d', '--driver'):
                DRIVER = value
            if name in ('-v', '--votes'):
                VOTES = value

    except getopt.GetoptError as err:
        print(str(err))
        print("Please Retry Arguments")
        sys.exit(1)

    for i in range(1, int(VOTES)+1):
        BOT = SlidoBot(HASH, XPATH, DRIVER)
        BOT.vote()
        BOT.closeBrowser()
        print("Votes: " + str(i))
if __name__ == "__main__":
    print("Voting...")
    main()
