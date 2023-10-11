from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_Quizz_creation():

    driver = webdriver.Chrome()

    # Navigate to Pave
    driver.get("https://pave-web-lilac.vercel.app/")
    driver.maximize_window()
    print("can navigate to Pave")
    time.sleep(3)
    # Smooth scroll to the bottom of the page
    driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });")
    print("Can scroll to the bottom of the page")

    # Wait for a few seconds to observe the scrolling (optional)
    time.sleep(3)

    # Smooth scroll back to the top of the page
    driver.execute_script("window.scrollTo({ top: 0, behavior: 'smooth' });")
    time.sleep(4)

    # Login

    # Locate the button using the find_element method and By.CSS_SELECTOR
    button = driver.find_element(By.CSS_SELECTOR, '.btn.normal-case.text-md.btn-primary')

    # Click the button
    button.click()
    print("Can click the login button and be redirected to homepage")
    time.sleep(5)

    #Select and click the new quiz button
    button = driver.find_element(By.CSS_SELECTOR, "a.btn-primary[href='/dashboard/quiz']")
    button.click()
    print("Can click the new quiz button and be redirected to new quiz page")

    time.sleep(4)
    #Select and click the form wizard quiz
    button = driver.find_element(By.CSS_SELECTOR, "a[href='./quiz/wizard']")
    button.click()
    print("Can click the form wizard quiz button and be redirected to form wizard quiz page")
    time.sleep(3)
    button = driver.find_element(By.CSS_SELECTOR, "button.block.w-full.rounded.p-2.text-left.transition-all.duration-300.hover\\:bg-gray-100")
    # Click the button
    button.click()

    time.sleep(5)


    
    file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    file_path = "C:\\Users\\Admin\\Downloads\\Chapter2&3.pdf"
    file_input.send_keys(file_path)
    print("Can upload file")

    #  locate and click textarea
    textarea = driver.find_element(By.CSS_SELECTOR, "textarea.textarea")
    textarea.click()
    time.sleep(2)
    textarea.send_keys("Focus on Software testing Question")
    print("can click on text area and enter a question")
    time.sleep(3)
    # locate and click button by xpath
    button = driver.find_element(By.XPATH, "//button[contains(text(),'Generate Quiz')]")
    button.click()
    print("can click on generate quiz button")
    driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });")
    time.sleep(30)
    print("All tests passed")

    # driver.quit()


test_Quizz_creation()
