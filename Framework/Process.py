from Functions_and_classes.sys_bussinesException import BusinessException
from Functions_and_classes.sys_context import general
import Activities.webActivities as webAct
from botcity.web import By

def process():
    try:
        # Your main process logic here
        print("Executing process..."+ general.row_transactionItem["Nombre de proveedor"])
        # validating if the ID de pedido de compra is on screen
        

        # Buscar y hacer clic en el ID del pedido
        pedido_id       = general.row_transactionItem["ID de pedido de compra"]
        pedido_selector = f"//a[contains(text(), '{pedido_id}')]"
        foundIDpedido   = wait_and_click(pedido_selector)

        if foundIDpedido:
            webAct.webbot.wait(10000)
            # Click en "Editar"
            editar_selector = "//span[contains(text(), 'Editar')]"
            btnEditar       = wait_and_click(editar_selector)

            # Si se pudo hacer clic en "Editar", buscar "Pedir"
            if btnEditar:
                pedir_selector = "//span[contains(text(), 'Pedir')]"
                wait_and_click(pedir_selector)


        # Example: raise BusinessException("A business error occurred")
        # Example: raise Exception("A system error occurred")
    except BusinessException as be:
        # Handle business exceptions
        print(f"Business exception caught: {be}")
    except Exception as e:
        # Handle system exceptions
        print(f"System exception caught: {e}")
        general.bol_systemException= True
    finally:
        # Cleanup or finalization code
        print("Process finished.")

def wait_and_click(selector, by=By.XPATH, wait_time=2000):
    element = webAct.webbot.find_element(selector=selector, by=by)
    if element:
        webAct.webbot.wait_for_element_visibility(element=element, visible=True, waiting_time=100000)
        webAct.webbot.wait(wait_time)
        element.click()
        return element