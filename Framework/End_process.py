from Functions_and_classes.sys_context import general
import Activities.webActivities as webAct
import Functions_and_classes.sap_signIn_singOut as sap_auth

def end_process():
    if general.bol_systemException:
        print("System exception occurred. Process stopped.")
        sap_auth.signOut()
        webAct.webbot.stop_browser()
    else:   
        print("Process finished.")
        sap_auth.signOut()
        webAct.webbot.stop_browser()  
    