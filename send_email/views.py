# myapp/views.py
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.conf import settings
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def screenshot(url):
    # from selenium import webdriver
    # from selenium.webdriver.chrome.service import Service
    # from webdriver_manager.chrome import ChromeDriverManager
    # from selenium.webdriver.chrome.options import Options
    # from selenium.webdriver.common.by import By
    # from selenium.webdriver.common.keys import Keys
    # import time
    


    # Setup Chrome options
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Ensure GUI is off
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")

    # # Choose Chrome Browser and set up the driver with webdriver_manager
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # URL of the Google form
    driver = webdriver.Chrome()

    driver.get(url)

    time.sleep(2)

        # Fill out the form
    full_name_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    full_name_input.send_keys("Harshit Garg")

    phone_number = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    phone_number.send_keys("--------")

    email_address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    email_address.send_keys("mail@gmail.com")

    home_address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
    home_address.send_keys("------------------------")

    pin_number = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    pin_number.send_keys("-----")

    date_of_birth = driver.find_element(By.XPATH, '//input[@type="date"]')
    date_of_birth.send_keys("---")
    date_of_birth.send_keys(Keys.RETURN)

    gender = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    gender.send_keys("Male")

    verification = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    verification.send_keys("-----")

        # Submit the form (uncomment the lines below to actually submit)
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

        # Give some time to ensure the form submission and redirection (if submission is enabled)
    time.sleep(2)

        # Capture a screenshot of the confirmation page or filled form
    screenshot_path = 'form_submission_screenshot.png'
    driver.save_screenshot(screenshot_path)

    driver.quit()
    return screenshot_path




def add_attachment(screenshot_path):
    subject = 'Python (Selenium) Assignment - Harshit Garg'
    message = ("Message"
               "\n\n\n For Source code:\n github repo : https://github.com/Harshit-880/scrap_sendmail")

    recipients = ['----emailid']
    cc_recipients = ['----emailid']

    email = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        recipients,
        cc=cc_recipients
    )

    resume_path = r"path"
    documentation_path = r"path"
    
    with open(screenshot_path, 'rb') as f:
        email.attach('screenshot.png', f.read(), 'image/png')

    # Attach the resume
    with open(resume_path, 'rb') as f:
        email.attach('resume.pdf', f.read(), 'application/pdf')

    # Attach Documentation file
    with open(documentation_path, 'rb') as f:
        email.attach('documentation.txt', f.read(), 'text/pdf/md')

        # Send email
    # email.send()

def send_email(request):
    screanshot=screenshot(url)
    add_attachment(screanshot)
    
    os.remove(screanshot)

url = "form url"
send_email(url)