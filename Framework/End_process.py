from Functions_and_classes.sys_context import general
from Framework.closeApplications import closeApp

def end_process():
    if general.bol_systemException:
        print("System exception occurred. Process stopped.")
    else:   
        print("Process finished.")
    