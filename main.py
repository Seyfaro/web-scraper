from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get('https://www.fife.gov.uk/services/bin-calendar')

# Wait for the input box and button to load
input_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'dform_widget_ps_45M3LET8_txt_postcode')))
search_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'dform_widget_ps_3SHSN93_searchbutton')))

# Clear the input box to make sure it's empty
input_box.clear()

# Input 'KY15 5NA' into the input box
input_box.send_keys('KY15 5NA')

# Press Enter to submit the form, or click the search button
search_button.click()

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.title_contains('Search Results'))

# Perform actions on the search results page
# ...

# Close the browser window
driver.quit()
