from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_options.add_argument("user-data-dir=/Users/sagar/Sagar/Work/work3/ww/chromium_user_data")
chrome_options.add_argument("profile-directory=Profile 2")  # Use the correct profile

# Set up WebDriver service
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for the user to log in manually
time.sleep(15)

# Function to scroll an element into view
def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

# Function to hover over an element
def hover_over_element(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

try:
    # Specify the group name
    group_name = "https://chat.whatsapp.com/Bgg1l5tTcJl3NpOuXfqdSp"  # Replace this with your group's name

    # Locate the search box, type the group name, and select the group
    print("Locating the search box and typing the group name...")
    search_box_xpath = "//div[@role='textbox']"  # XPath for the search box
    search_box = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, search_box_xpath)))
    search_box.click()
    search_box.send_keys(group_name)
    print("Group name typed")

    # Click on the group from the search results
    print("Locating and clicking on the group...")
    group_xpath = f"//span[@title='{group_name}']"  # XPath to find the group
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, group_xpath))).click()
    print("Group clicked")

    # Click on the Group Info button
    print("Locating and clicking Group Info...")
    group_info_xpath = "/html/body/div[1]/div/div/div[2]/div[4]/div/header/div[2]/div[1]/div/span"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, group_info_xpath))).click()
    print("Group Info clicked")

    # Locate and scroll to the member list
    print("Locating and scrolling to the member list...")
    div_xpath = "/html/body/div[1]/div/div/div[2]/div[5]/span/div/span/div/div/div/section/div[7]"
    div_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, div_xpath)))
    scroll_to_element(driver, div_element)
    print("Scrolled to member list")

    # Loop through members and remove each one
    while True:
        try:
            # Find and hover over the first visible member
            print("Locating and hovering over the member...")
            member_xpath = "/html/body/div[1]/div/div/div[2]/div[5]/span/div/span/div/div/div/section/div[7]/div[2]/div[3]/div/div/div/div[10]"
            member_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, member_xpath)))
            hover_over_element(driver, member_element)
            print("Hovered over the member")

            # Click the down arrow to open the menu
            print("Locating and clicking the down arrow...")
            down_arrow_xpath = "/html/body/div[1]/div/div/div[2]/div[5]/span/div/span/div/div/div/section/div[7]/div[2]/div[3]/div/div/div/div[10]/div/div/div[2]/div[2]/div[2]"
            down_arrow_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, down_arrow_xpath)))
            down_arrow_element.click()
            print("Down arrow clicked")

            # Click the Remove option
            print("Locating and clicking the Remove option...")
            remove_xpath = "/html/body/div[1]/div/div/span[5]/div/ul/div/li[2]/div"
            remove_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, remove_xpath)))
            remove_element.click()
            print("Remove option clicked")

            # Confirm removal
            print("Locating and clicking the final Remove button...")
            final_remove_xpath = "/html/body/div[1]/div/div/span[2]/div/div/div/div/div/div/div[2]/div/button[2]"
            final_remove_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, final_remove_xpath)))
            final_remove_element.click()
            print("Final Remove button clicked")

            # Wait for the page to update
            time.sleep(2)  # Adjust if necessary

        except Exception as e:
            print("No more members to remove or an error occurred:", str(e))
            break

finally:
    # Close the browser
    time.sleep(50)  # Allow some time to see results
    driver.quit()
