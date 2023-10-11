from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Navigate to Pave
driver.get("https://pave-web-lilac.vercel.app/")
driver.maximize_window()
time.sleep(2)
# Smooth scroll to the bottom of the page
driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });")

# Wait for a few seconds to observe the scrolling (optional)
time.sleep(2)

# Smooth scroll back to the top of the page
driver.execute_script("window.scrollTo({ top: 0, behavior: 'smooth' });")
time.sleep(2)

# Login

# Locate the button using the find_element method and By.CSS_SELECTOR
button = driver.find_element(By.CSS_SELECTOR, '.btn.normal-case.text-md.btn-primary')

# Click the button
button.click()
time.sleep(3)

#Select and click the new quiz button
button = driver.find_element(By.CSS_SELECTOR, "a.btn-primary[href='/dashboard/quiz']")
button.click()


time.sleep(3)
#Select and click the form wizard quiz
button = driver.find_element(By.CSS_SELECTOR, "a[href='./quiz/wizard']")
button.click()

time.sleep(3)
button = driver.find_element(By.CSS_SELECTOR, "button.block.w-full.rounded.p-2.text-left.transition-all.duration-300.hover\\:bg-gray-100")
# Click the button
button.click()

time.sleep(5)
# Locate the "start-time" input element using its id attribute and set a date and time value


file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
file_path = "C:\\Users\\Admin\\Downloads\\Chapter2&3.pdf"
file_input.send_keys(file_path)


#  locate and click textarea
textarea = driver.find_element(By.CSS_SELECTOR, "textarea.textarea")
textarea.click()
time.sleep(1)
textarea.send_keys("Focus on Software testing Question")
time.sleep(2)
# locate and click button by xpath
button = driver.find_element(By.XPATH, "//button[contains(text(),'Generate Quiz')]")
button.click()
driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });")
time.sleep(30)

# driver.quit()