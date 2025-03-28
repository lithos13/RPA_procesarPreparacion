# Import for the Web Bot
from botcity.web import WebBot, Browser, By
# Import webdriver_manager to automatically download the WebDriver binary
from webdriver_manager.chrome import ChromeDriverManager


def initApp():
    webbot             = WebBot()    
    webbot.headless    = False   
    webbot.driver_path = ChromeDriverManager().install()
    webbot.browse("https://my360131.sapbydesign.com/sap/public/ap/ui/repository/SAP_UI/HTMLOBERON5/client.html?app.component=/SAP_UI_CT/Main/root.uiccwoc&rootWindow=X&redirectUrl=/sap/public/byd/runtime#n=eyJpblBvcnQiOiIiLCJ0YXJnZXQiOiIvU0FQX0JZRF9BUFBMSUNBVElPTl9VSS9zcm0vcHJvL1BST19QdXJjaGFzZVJlcXVlc3RfV0NWaWV3LldDVklFVy51aXdvY3ZpZXciLCJwYXJhbXMiOnt9LCJsaXN0cyI6e30sIndjQ29udGV4dCI6eyJ3b2NJZCI6Ii9TQVBfQllEX0FQUExJQ0FUSU9OX1VJL3NybS9wcm8vUFJPX1NSTV9XQ0YuV0NGLnVpd29jIiwidmlld0lkIjoiL1NBUF9CWURfQVBQTElDQVRJT05fVUkvc3JtL3Byby9QUk9fUHVyY2hhc2VSZXF1ZXN0X1dDVmlldy5XQ1ZJRVcudWl3b2N2aWV3IiwiaXNPdnAiOmZhbHNlLCJpc05hdk5vZGUiOnRydWUsIm5hdk5vZGVUZXh0IjoiU29saWNpdHVkZXMlMjBkZSUyMGNvbXByYSUyMHklMjBwZWRpZG9zJTIwLSUyMFNvbGljaXR1ZGVzJTIwZGUlMjBjb21wcmEifX0%3D")
    print("Initializing applications...")
    