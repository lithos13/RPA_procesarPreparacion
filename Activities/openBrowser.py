# Import for the Web Bot
from botcity.web import WebBot, Browser, By
# Import webdriver_manager to automatically download the WebDriver binary
from webdriver_manager.chrome import ChromeDriverManager


webbot             = WebBot()

# Configure whether or not to run on headless mode
webbot.headless    = False   
webbot.driver_path = ChromeDriverManager().install()

def open_browser(url):
   webbot.browse(url)
   # Wait 3 seconds before closing
   webbot.wait(3000)  
   # Finish and clean up the Web Browser
   # You MUST invoke the stop_browser to avoid
   # leaving instances of the webdriver open
   #webbot.stop_browser()    
   return webbot