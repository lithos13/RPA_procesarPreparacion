from Functions_and_classes.sys_bussinesException import BusinessException
from Functions_and_classes.sys_context import general
import Activities.webActivities as webAct
from botcity.web import By

def process():
    try:
        # Your main process logic here
        print("Executing process..."+ general.row_transactionItem["Nombre de proveedor"])
        # validating if the ID de pedido de compra is on screen        

        # obtein the "ID de pedido de compra" from the transaction item
        pedido_id       = str(general.row_transactionItem["ID de pedido de compra"])
         
         # searching the "ID de pedido de compra" in the screen table
        input_search    = wait_and_sendKeys(selector='__pane1-searchField-I', by=By.ID, value=pedido_id)              
       
        # if the input field is found, send the ID de pedido de compra to it
        if input_search:           
            webAct.webbot.enter()
            webAct.webbot.wait(2000) 
        else:
            general.str_messageError = "The input field for searching the ID de pedido de compra was not found."
            general.bol_systemException = True
            return        

        # Once the ID de pedido de compra is on screen, click on it
        pedido_selector = f"//a[contains(text(), '{pedido_id}')]"
        foundIDpedido   = wait_and_click(pedido_selector, by=By.XPATH)

        # inside of the ID de pedido de compra, click on "Editar"
        if foundIDpedido:
            webAct.webbot.wait(2000)
            # Click on "Editar"
            editar_selector = "//span[contains(text(), 'Editar')]"
            btnEditar       = wait_and_click(editar_selector, by=By.XPATH)          
        else:
            general.str_messageError    = "The ID de pedido de compra "+pedido_id+" was not found in the table."
            general.bol_systemException = True
            return
        
        # if editing is successful, click on "Pedir"
        if btnEditar:
            pedir_selector = "//span[contains(text(), 'Pedir')]"                  
            btnPedir = wait_and_click(pedir_selector, by=By.XPATH)
        else:
            general.str_messageError    = "The Edit button was not found."
            general.bol_systemException = True
            return
        
         # if pedir is successful, click on "Pedir"
        if btnPedir:
            pass
        else:
            general.str_messageError    = "The Pedir button was not found."
            general.bol_systemException = True
            return
        
        # if the process is successful, click on "Cerrar" pedido
        cerrar_selector = "//span[contains(text(), 'Cerrar')]"
        btnCerrar = wait_and_click(cerrar_selector, by=By.XPATH)
       
        ## Getting text property, you can access other properties through the WebElement object
        # print(element.text)
        
        

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

def wait_and_click(selector, by, wait_time=2000):
    element = webAct.webbot.find_element(selector=selector, by=by)
    if element:
        webAct.webbot.wait_for_element_visibility(element=element, visible=True, waiting_time=100000)
        webAct.webbot.wait(wait_time)
        element.click()
        return element

def wait_and_sendKeys(selector, by, wait_time=2000, value=None):
    element = webAct.webbot.find_element(selector=selector, by=by)
    if element:
        webAct.webbot.wait_for_element_visibility(element=element, visible=True, waiting_time=100000)
        webAct.webbot.wait(wait_time)
        element.clear()    
        element.send_keys(value)
        return element        