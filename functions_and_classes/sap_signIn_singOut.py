from Activities.openBrowser import open_browser
from decouple import config
from botcity.web import By


def signIn():
    str_messageError = ""
    bol_session = False
    print("Sign in on SAP Business ByDesign")

    # Get the URL from the environment variable
    url_pedidos = config('URL_PEDIDOS')

    # Check if the URL is None or empty
    if not url_pedidos:
        raise Exception("The environment variable 'URL_PEDIDOS' is not set.")

    # Open the browser and maximize the window
    webbot = open_browser(url_pedidos)
    webbot.driver.maximize_window()

    # Helper function to find and interact with elements
    def find_and_interact(selector, by, action, value=None, error_message="Element not found"):
        element = webbot.find_element(selector=selector, by=by)
        if element:
            webbot.wait_for_element_visibility(element=element, visible=True, waiting_time=10000)
            if action == "send_keys":
                element.send_keys(value)
            elif action == "click":
                element.click()
        else:
            raise Exception(error_message)

    # USERNAME
    find_and_interact(
        selector='__control0-user-inner',
        by=By.ID,
        action="send_keys",
        value=config('USER'),
        error_message="The element 'user' was not found."
    )

    # PASSWORD
    find_and_interact(
        selector='__control0-pass-inner1',
        by=By.ID,
        action="send_keys",
        value=config('PASSWORD'),
        error_message="The element 'password' was not found."
    )

    # LANGUAGE
    find_and_interact(
        selector='__control0-langdd-inner',
        by=By.ID,
        action="send_keys",
        value=config('LANGUAGE'),
        error_message="The element 'language' was not found."
    )

    # CLICK ON INICIAR SESION BUTTON
    find_and_interact(
        selector='__control0-logonBtn-BDI-content',
        by=By.ID,
        action="click",
        error_message="The element 'SignIn button' was not found."
    )

    # CLICK ON CONTINUAR BUTTON
    find_and_interact(
        selector='__control1-continueBtn-inner',
        by=By.ID,
        action="click",
        error_message="The element 'Continuar button' was not found."
    )

    bol_session = True
    return bol_session