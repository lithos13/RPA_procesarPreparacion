from Functions_and_classes.sys_bussinesException import BusinessException
from Functions_and_classes.sys_context import general
import Activities.webActivities as webAct
from botcity.web import By

def process():
    str_typException =""
    try:
        # Your main process logic here
        print("Executing process..."+ general.row_transactionItem["Nombre de proveedor"] + " - " + str(general.row_transactionItem["ID de proveedor"]))

        #looking supplier ID in the COD Proveedores sheet-----------------------------------
        df_rowProveedorConfig = general.df_dataConfig[general.df_dataConfig['ID SAP'] == str(general.row_transactionItem["ID de proveedor"])]
        if not df_rowProveedorConfig.empty:
            str_tipoProveedor = df_rowProveedorConfig['PREVISIÓN'].iloc[0]
        else:
            general.str_messageError = "Proveedor no encontrado en la configuración de proveedores"
            raise BusinessException(general.str_messageError)
        #-------------------------------------------------------------------------------------

        # when the supplier is IMPORTADOS, let's check if the current day is a purchase day---------
        if str_tipoProveedor == "IMPORTADOS":
            arr_purchaseDays = list(map(str, df_rowProveedorConfig['DÍAS DE COMPRA'].iloc[0].split('-')))
            bol_purchaseDay  = general.str_currentDay in arr_purchaseDays
           # Check if the current day is a purchase day for the supplier
            if bol_purchaseDay:
                    # Proceed with the order
                pass
            else:
                    #log no es el dia de compra para el proveedor
                return
        else:
            # when the supplier is NACIONAL, let's proceed to the order
            pass       
        #---------------------------------------------------------------------------------------------

        # obtein the "ID de pedido de compra" from the transaction item
        pedido_id       = str(general.row_transactionItem["ID de pedido de compra"])
         
         # searching the "ID de pedido de compra" in the screen table
        input_search    = wait_and_sendKeys(selector='__pane1-searchField-I', by=By.ID, value=pedido_id)              
       
        # if the input field is found, send the ID de pedido de compra to it
        if input_search:           
            webAct.webbot.enter()
            webAct.webbot.wait(2000) 
        else:
            general.str_messageError = "el campo de busqueda para buscar el pedido en la tabla no fue encontrado."
            raise Exception(general.str_messageError)           
            

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
            general.str_messageError    = "El ID pedido de compra: "+pedido_id+" no se encontró en la tabla."
            raise Exception(general.str_messageError)  
        
        # if editing is successful, click on "Pedir"
        if btnEditar:
            pedir_selector = "//span[contains(text(), 'Pedir')]"                  
            btnPedir = wait_and_click(pedir_selector, by=By.XPATH)
        else:
            general.str_messageError    = "El botón editar no fue encontrado."
            raise Exception(general.str_messageError)  
        
         # if pedir is successful, click on "Pedir"
        if btnPedir:
            print("Pedido realizado con éxito.")
            pass
        else:
            general.str_messageError    = "El botón pedir no fue encontrado."
            raise Exception(general.str_messageError)  
        
        # if the process is successful, click on "Cerrar" pedido
        cerrar_selector = "//span[contains(text(), 'Cerrar')]"
        btnCerrar = wait_and_click(cerrar_selector, by=By.XPATH)       

    # Type of exception handling
    except BusinessException as be:
        # Handle business exceptions
        print(f"Business exception caught: {be}")
        general.bol_bussinessException= True
        str_typException = "BusinessException"
    except Exception as e:
        # Handle system exceptions
        print(f"System exception caught: {e}")
        general.bol_systemException= True
        str_typException = "SystemException"
    finally:
        # Cleanup or finalization code
        print("Process finished.")
        return str_typException

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