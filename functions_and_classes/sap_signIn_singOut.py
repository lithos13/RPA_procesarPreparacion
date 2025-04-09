import Activities.webActivities as webAct
from decouple import config
from botcity.web import By
from Functions_and_classes.sys_context import general

# Sign in on SAP Business ByDesign>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def signIn():
    bol_session = False
    print("Sign in on SAP Business ByDesign")

    # Get the URL from the environment variable
    url_pedidos = config('URL_PEDIDOS')

    # Check if the URL is None or empty
    if not url_pedidos:
        general.str_messageError = "The environment variable 'URL_PEDIDOS' is not set."
        raise Exception(general.str_messageError)

    # Open the browser and maximize the window
    webbot = webAct.open_browser(url_pedidos)
    webbot.driver.maximize_window()
    
    
    # USERNAME
    username = webAct.webbot.find_element(selector="__control0-user-inner", by=By.ID)
    if username is not None:
        webAct.webbot.wait_for_element_visibility(element=username, visible=True, waiting_time=100000)
        webAct.webbot.wait(2000)
        webAct.webbot.find_element(selector="__control0-user-inner", by=By.ID)
        print(f"Username: {config('USER')}")
        username.send_keys(config('USER'))
    else:
        ## Check if the "Pedidos de compra" element is loaded
        ## This is a workaround to check if the session is already started
        pedidosLoaded = webAct.webbot.find_element(selector="//span[contains(text(), 'Pedidos de compra')]", by=By.XPATH)  
        if pedidosLoaded is not None:
            webAct.webbot.wait_for_element_visibility(element=pedidosLoaded, visible=True, waiting_time=100000)
            webAct.webbot.wait(2000)
            bol_session = True    
            return {"bol_session": bol_session, "webbot": webbot, "By":By}        
        

    # PASSWORD
    password = webAct.webbot.find_element(selector="__control0-pass-inner", by=By.ID)
    if password is not None:   
        webAct.webbot.wait_for_element_visibility(element=password, visible=True, waiting_time=100000)
        webAct.webbot.wait(2000)
        webAct.webbot.find_element(selector="__control0-pass-inner", by=By.ID)
        password.send_keys(config('PASSWORD'))
    

    # LANGUAGE
    language = webAct.webbot.find_element(selector="__control0-langdd-inner", by=By.ID)
    if language is not None:
        webAct.webbot.wait_for_element_visibility(element=language, visible=True, waiting_time=100000)
        webAct.webbot.wait(2000)
        webAct.webbot.find_element(selector="__control0-langdd-inner", by=By.ID)
        language.send_keys(config('LANGUAGE'))
    

    # CLICK ON INICIAR SESION BUTTON
    btnIniciarSesion = webAct.webbot.find_element(selector='__control0-logonBtn-BDI-content', by=By.ID)
    if btnIniciarSesion is not None:    
        webAct.webbot.wait_for_element_visibility(element=btnIniciarSesion, visible=True, waiting_time=100000)
        webAct.webbot.wait(2000)
        webAct.webbot.find_element(selector='__control0-logonBtn-BDI-content', by=By.ID)
        btnIniciarSesion.click()
   

    # CLICK ON CONTINUAR BUTTON
    continuar = webAct.webbot.find_element(selector='__control1-continueBtn-inner', by=By.ID)
    if continuar is not None:    
        webAct.webbot.wait_for_element_visibility(element=continuar, visible=True, waiting_time=100000)
        webAct.webbot.wait(2000)
        webAct.webbot.find_element(selector='__control1-continueBtn-inner', by=By.ID)
        continuar.click()    
        webAct.webbot.wait(10000)

    ## Check if the "Pedidos de compra" element is loaded
    ## This is a workaround to check if the session is already started
    pedidosLoaded = webAct.webbot.find_element(selector="//span[contains(text(), 'Pedidos de compra')]", by=By.XPATH)  
    if pedidosLoaded is not None:
        webAct.webbot.wait_for_element_visibility(element=pedidosLoaded, visible=True, waiting_time=100000)
        webAct.webbot.wait(2000)
        bol_session = True    
        return {"bol_session": bol_session, "webbot": webbot, "By":By}
    else:  
        bol_session = False              
        return {"bol_session": bol_session, "webbot": webbot, "By":By}
       
    
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    

# Sign out of SAP Business ByDesign>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def signOut():
    print("Sign out of SAP Business ByDesign")

    # CLICK ON AVATAR BUTTON    
    avatar = webAct.webbot.find_element(selector='sapBUiRoundButtonIconImg', by=By.CLASS_NAME)
    if avatar is not None:
        webAct.webbot.wait_for_element_visibility(element=avatar,visible=True, waiting_time=8000)    
        webAct.webbot.wait(2000)
        webAct.webbot.find_element(selector='sapBUiRoundButtonIconImg', by=By.CLASS_NAME)
        avatar.click()    
    
    
    # CLICK ON SALIR DEL SISTEMA OPTION        
    opcionSalir = webAct.webbot.find_element(selector="//div[contains(text(), 'Salir del sistema')]", by=By.XPATH)
    if opcionSalir is not None:
        webAct.webbot.wait_for_element_visibility(element=opcionSalir,visible=True, waiting_time=8000)    
        webAct.webbot.wait(2000)
        webAct.webbot.find_element(selector="//div[contains(text(), 'Salir del sistema')]", by=By.XPATH)
        opcionSalir.click()    
    
    
    # CLICK ON Confirmar Confirmar cierre sesión
    confirm= webAct.webbot.find_element(selector="//bdi[contains(text(), 'OK')]", by=By.XPATH)
    if confirm is not None:
        webAct.webbot.wait_for_element_visibility(element=confirm,visible=True, waiting_time=8000)    
        webAct.webbot.wait(2000)
        webAct.webbot.find_element(selector="//bdi[contains(text(), 'OK')]", by=By.XPATH)
        confirm.click()
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Finish and clean up the Web Browser
      
    