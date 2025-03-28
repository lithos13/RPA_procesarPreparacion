# Import for the Web Bot
from botcity.web import WebBot, Browser, By
# Import webdriver_manager to automatically download the WebDriver binary
from webdriver_manager.chrome import ChromeDriverManager


webbot             = WebBot()
webbot.headless    = False   
webbot.driver_path = ChromeDriverManager().install()

def open_browser(url):
   webbot.browse(url)      
   return webbot