from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


try:
    print("=============scraping-started============")
    options = Options()
    options.add_argument("--headless")  # Headless mode
    options.add_argument("--disable-gpu")  # Good practice
    options.add_argument("--no-sandbox")  # Required for some Linux distros
    options.add_argument("--window-size=1920,1080")  # Ensure full content renders
    service = Service("/usr/bin/chromedriver")  # Point to the correct chromedriver
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://forms.gle/WT68aV5UnPajeoSc8")
    time.sleep(2)  # Wait for page to load
    name = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name.send_keys("John Doe")

    contact_no = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    contact_no.send_keys("1234567890")

    email = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    email.send_keys("john.doe@example.com")

    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
    address.send_keys("123 Main St, Anytown, USA")

    pin_code = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    pin_code.send_keys("12345")

    date = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    date.send_keys("01/01/2000")

    gender = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    gender.send_keys("Male")

    captcha = driver.find_element(By.XPATH, '//*[@id="i37"]/span[1]/b')  # Replace with actual XPath
    captcha_value = captcha.text.strip()

    captcha_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')  
    captcha_input.send_keys(captcha_value)
    
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()
    time.sleep(2)  # Wait for submission to process
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]')
    element.screenshot("submission_confirmation.png")
    print("=============scraping-completed============")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
