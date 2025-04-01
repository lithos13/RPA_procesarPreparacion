from Functions_and_classes.sys_context import general
from Activities.openBrowser import open_browser
from decouple import config
# Import for the Web Bot
from botcity.web import By



#     # Sign in on SAP Business ByDesign
def signIn(): 
    str_messageError = ""
    bol_session      = False
    print("Sign in on SAP Business ByDesign")
    # Get the URL from the environment variable    
    url_pedidos = config('URL_PEDIDOS')

    # Check if the URL is None or empty
    if url_pedidos is None:   
        str_messageError = "The environment variable 'URL_PEDIDOS' is not set."  
        raise Exception(str_messageError)           
    else:    
        webbot= open_browser(url_pedidos)
        # Maximize the browser window
        webbot.driver.maximize_window()

        #USERNAME"
        user = webbot.find_element(selector='__control0-user-inner', by=By.ID)
        # Wait for the page to load
        if user is not None:            
            webbot.wait_for_element_visibility(element=user, visible=True, waiting_time=10000)
            user.send_keys(config('USER'))            
        else:   
            str_messageError = "The element 'user' was not found."
            raise Exception(str_messageError)   
       
        #PASSWORD"
        password = webbot.find_element(selector='__control0-pass-inner', by=By.ID)
        # Wait for the page to load
        if password is not None:            
            webbot.wait_for_element_visibility(element=password, visible=True, waiting_time=10000)
            password.send_keys(config('PASSWORD'))            
        else:   
            str_messageError = "The element 'password' was not found."
            raise Exception(str_messageError)   
        
    
        #LANGUAGE"
        languaje = webbot.find_element(selector='__control0-langdd-inner', by=By.ID)
        ## Insert text content in the element
        if languaje is not None:            
            webbot.wait_for_element_visibility(element=languaje, visible=True, waiting_time=10000)     
            languaje.send_keys("")       
            languaje.send_keys(config('LANGUAGE'))            
        else:   
            str_messageError = "The element 'languaje' was not found."
            raise Exception(str_messageError)   
       
        #CLICK ON INICIAR SESION IN BUTTON"
        signInBTN = webbot.find_element(selector='__control0-logonBtn-BDI-content', by=By.ID)
        if signInBTN is not None:
            # Waiting until it is visible on the page.
            webbot.wait_for_element_visibility(element=signInBTN, visible=True, waiting_time=10000)
            signInBTN.click()
        else:
            str_messageError            = "The element 'SignIn button' was not found."
            raise Exception(str_messageError)   
        
         # Finding an element.
        continuar = webbot.find_element(selector='__control1-continueBtn-inner', by=By.ID)
        if continuar is not None:
            # Waiting until it is visible on the page.
            print("Button 'Continuar' found")
            webbot.wait_for_element_visibility(element=continuar, visible=True, waiting_time=10000)            
            continuar.click()     
        
        bol_session = True
    return bol_session