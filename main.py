
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from tabulate import tabulate
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
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


# Wait for the dropdown menu to load
time.sleep(4)
# Wait for the dropdown menu to load
dropdown_menu = driver.find_element('id', 'dform_widget_ps_3SHSN93_id')
time.sleep(4)


# Select an option from the dropdown menu

select = Select(dropdown_menu)
select.select_by_visible_text('18 MAIN STREET, CERES, FIFE, KY15 5NA')



# Extract!

time.sleep(4)

div_elements = driver.find_elements(By.CSS_SELECTOR, "div.dform_td[data-name='type']")


type_list = []

for div_element in div_elements:
    text = div_element.text
    type_list.append(text)

print(type_list)

div_dates = driver.find_elements(By.CSS_SELECTOR, "div.dform_td[data-name='date']")


date_list = []

for div_date in div_dates:
    text = div_date.text
    date_list.append(text)

print(date_list)

ThisWeek = [[date_list[i], type_list[i]] for i in range(len(date_list))]

print(ThisWeek)


# Print the 2D array as a table
print(tabulate(ThisWeek, headers=['Collection Date', 'Bin Type'], tablefmt='orgtbl'))

#export
array_str = '\n'.join(['~'.join([str(elem) for elem in row]) for row in ThisWeek])

# Write the string representation to a file
with open('ThisWeek.txt', 'w') as f:
    f.write(array_str)