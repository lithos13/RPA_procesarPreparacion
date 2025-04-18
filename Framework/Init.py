from Functions_and_classes.sys_context import general
import Functions_and_classes.google_workspace_activities as gs
from Framework.closeApplications import closeApp
import Functions_and_classes.sap_signIn_singOut as sap_auth
import Activities.fileActivities as fileAct
from decouple import config
import pandas as pd
from datetime import datetime

def init():
    str_message = ""
    try:
        if general.int_numRetry == 0:
           print("first run")
           # load variables
           closeApp()

        #Init applications>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        print("Initializing applications...")
        # Sign in on SAP Business ByDesign    
        arr_session = sap_auth.signIn()          
        print(f"Session: {arr_session['bol_session']}")
        if arr_session['bol_session']:
            print("Session started successfully..")
            general.bol_systemException = False
        else:
            general.str_messageError = "Session not started."            
            raise Exception(general.str_messageError)  
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        #obtein the current date and time>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # Get the current date and time
        general.date_current = datetime.now()

        # Extract the current day as a string
        general.str_currentDay = general.date_current.strftime("%d")
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        #Obtein configuration data from config file>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
        sheet_name = 'COD Proveedores'
        dataConfig = gs.get_google_sheet_as_dataframe(config('ID_SHEET_CONFIG'), sheet_name)
        if len(dataConfig)>0:
            general.df_dataConfig = pd.DataFrame(dataConfig)                  
        else:
            general.str_messageError = "El sheet de configuración 'COD Proveedores' no fue encontrado."
            raise Exception(general.str_messageError)        
        
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        #Get transaction data "En preparacion">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>      
        # Select the dropdown list
        select = arr_session['webbot'].find_element(selector='__pane1-defaultSetDDLB-arrow', by=arr_session['By'].ID)
        if select is not None:            
            #click on the dropdown list arrow
            arr_session['webbot'].wait_for_element_visibility(element=select,visible=True, waiting_time=8000)            
            arr_session['webbot'].wait(2000)            
            select = arr_session['webbot'].find_element(selector='__pane1-defaultSetDDLB-arrow', by=arr_session['By'].ID)        
            select.click()
            # click on the option "Pedidos de compra en preparación"
            arr_session['webbot'].wait(2000)            
            element = arr_session['webbot'].find_element(selector="//li[contains(text(), 'Pedidos de compra en preparación')]", by=arr_session['By'].XPATH)            
            element.click()          
        else:
            general.str_messageError    = "La lista seleccionable 'lista de estados de pedidos' no fue encontrada."
            raise Exception(general.str_messageError)        
       
        arr_session['webbot'].wait(2000)

        # click on Exportar button        
        btn_exportar = arr_session['webbot'].find_element(selector="//span[contains(text(), 'Exportar')]", by=arr_session['By'].XPATH)            
        btn_exportar.click()  
        arr_session['webbot'].wait(1000)

        # click on Exportar a Excel button
        btn_excel = arr_session['webbot'].find_element(selector="//div[contains(text(), 'A Microsoft Excel')]", by=arr_session['By'].XPATH)            
        btn_excel.click()  
        
        # read the excel file
        arr_session['webbot'].wait(10000)
        str_ruta = config('PATH_TEMP') + "Listadepedidos__ES.xlsx"
        df_excel = fileAct.read_ExcelFile(str_ruta, 4, "B:J")                
        if df_excel.empty:
            general.str_messageError = "El archivo de Excel (lista pedidos en preparación) está vacio o no se han recuperado datos."
            raise Exception(general.str_messageError)
        else:
            print("Data successfully retrieved from the Excel file.")       
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        general.df_transactionData = df_excel    
        arr_session['webbot'].wait(11000)

        
    except Exception as e:
        print(f"An error occurred: {e} - {general.str_messageError}")        
        general.bol_systemException= True
    
        
    