import Activities.webActivities as webAct
from Activities.webActivities import open_browser
from decouple import config
from botcity.web import By
from Functions_and_classes.sys_context import general


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
    webbot = open_browser(url_pedidos)
    webbot.driver.maximize_window()
    
    
    # USERNAME
    webAct.find_and_interact(
        selector='__control0-user-inner',
        by=By.ID,
        action="send_keys",
        value=config('USER'),
        error_message="The element 'user' was not found."
    )

    # PASSWORD
    webAct.find_and_interact(
        selector='__control0-pass-inner',
        by=By.ID,
        action="send_keys",
        value=config('PASSWORD'),
        error_message="The element 'password' was not found."
    )

    # LANGUAGE
    webAct.find_and_interact(
        selector='__control0-langdd-inner',
        by=By.ID,
        action="send_keys",
        value=config('LANGUAGE'),
        error_message="The element 'language' was not found."
    )

    # CLICK ON INICIAR SESION BUTTON
    webAct.find_and_interact(
        selector='__control0-logonBtn-BDI-content',
        by=By.ID,
        action="click",
        error_message="The element 'SignIn button' was not found."
    )

    # CLICK ON CONTINUAR BUTTON
    webAct.find_and_interact(
        selector='__control1-continueBtn-inner',
        by=By.ID,
        action="click",
        error_message="The element 'Continuar button' was not found."
    )

    bol_session = True
    return {"bol_session": bol_session, "webbot": webbot, "By":By}

def signOut():
    pass