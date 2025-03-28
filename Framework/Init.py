from Functions_and_classes.sys_context import general
from Framework.closeApplications import closeApp
from Framework.InitApplications import initApp
import pandas as pd

def init():
    str_message = ""
    try:
        if general.int_numRetry == 0:
           print("first run")
           # load variables
           closeApp()
           initApp()          
           general.bol_systemException= False
        
    except Exception as e:
        print(f"An error occurred: {e}")        
        general.bol_systemException= True
    
        
    