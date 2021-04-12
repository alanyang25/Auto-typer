from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()

url = 'https://10fastfingers.com/typing-test/english'

def open_website():
    """Open 10fastfingers website"""
    driver.get(url)
    sleep(3)
    allow_btn = driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
    allow_btn.click()

def start_type():
    """Run typing hack"""
    open_website()
    input_field = driver.find_element(By.ID, 'inputfield')
    try:
        i = 1
        while True:
            word = driver.find_element(By.XPATH, '//*[@id="row1"]/span['+str(i)+']')
            input_field.send_keys(word.text)
            sleep(0.005) # set the interval(sec)
            input_field.send_keys(" ") # Press space to type the next word
            i += 1
    except:
        print(f"Finished! You typed {i} words.")

def main():
    start_type()

if __name__ == '__main__':
    main()
