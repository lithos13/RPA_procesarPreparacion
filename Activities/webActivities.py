# Import for the Web Bot
from botcity.web import WebBot, Browser, By
# Import webdriver_manager to automatically download the WebDriver binary
from webdriver_manager.chrome import ChromeDriverManager


webbot             = WebBot()

# Configure whether or not to run on headless mode
webbot.headless    = False   
webbot.driver_path = ChromeDriverManager().install()

# Open the browser and navigate to the URL
# This function opens the browser and navigates to the specified URL
def open_browser(url):
   webbot.browse(url)
   # Wait 3 seconds before closing
   webbot.wait(3000)  
   # Finish and clean up the Web Browser
   # You MUST invoke the stop_browser to avoid
   # leaving instances of the webdriver open
   #webbot.stop_browser()    
   return webbot

# Helper function to find and interact with elements
def find_and_interact(selector, by, action, value=None, error_message="Element not found"):
    element = webbot.find_element(selector=selector, by=by)   
    if element:
       webbot.wait_for_element_visibility(element=element, visible=True, waiting_time=100000)
       if action == "send_keys":
          element.send_keys(value)
       elif action == "click":
            element.click()
       else:
           raise Exception(error_message)

     