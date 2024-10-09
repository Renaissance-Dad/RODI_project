from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def onderwijs_het_archief(stamboeknr):
    driver = webdriver.Chrome()
    try:

        # Open the third-party form page
        driver.get('https://onderwijs.hetarchief.be/stamboek')

        # Locate form fields and fill them 

                # Wait for the cookie banner button to be clickable
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll'))
        )
        
        # Click the cookie consent button
        cookie_button.click()
        
        # Optional: Wait for the page to update after the click
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))  # Adjust as necessary
        )
    

        stamboek_field = driver.find_element(By.CLASS_NAME, 'c-input')
        stamboek_field.send_keys(stamboeknr)

        # Wait for the response page to load
        time.sleep(3)

        # Capture the response (or do something with it)
        response = driver.page_source

        if "Het stamboeknummer is geldig." in response:
            return "OK"

    finally:
        # Close the browser
        driver.quit()
    return "NOT OK"