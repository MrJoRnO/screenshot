import sys
import os
from selenium import webdriver
from pyvirtualdisplay import Display

# Get website URL from command line argument
website_url = sys.argv[1]

# Start virtual display
display = Display(visible=0, size=(1920, 1080))
display.start()

# Take screenshot using headless Chrome
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=options)
driver.get(website_url)
driver.save_screenshot('screenshot.png')

# Stop virtual display
display.stop()

# Move screenshot outside container
os.rename('/app/screenshot.png', 'screenshot.png')
print("0") 
