from Functions_and_classes.sys_context import general
from Framework.closeApplications import closeApp
import Functions_and_classes.sap_signIn_singOut as sap_auth
import pandas as pd

def init():
    str_message = ""
    try:
        if general.int_numRetry == 0:
           print("first run")
           # load variables
           closeApp()

           #Init applications--------------------------------------------------
           print("Initializing applications...")
           # Sign in on SAP Business ByDesign    
           bol_session = sap_auth.signIn()
           print(f"Session: {bol_session}")
           if bol_session:
               print("Session started successfully..")
               general.bol_systemException = False
           else:
               raise Exception("Session not started.")  
           #---------------------------------------------------------------------
         
                 
        
    except Exception as e:
        print(f"An error occurred: {e}")        
        general.bol_systemException= True
    
        
    