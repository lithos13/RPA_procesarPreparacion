"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/desktop/
"""
# Import for the Desktop Bot
from botcity.core import DesktopBot
# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Import Init module
from Framework.Init import init
from Framework.Get_Transaction import get_transaction
from Framework.Process import process
from Framework.End_process import end_process
from Functions_and_classes.sys_context import general


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    desktop_bot = DesktopBot()

    # Implement here your logic...----------------------------------------------------------------------------------------------------------------------------------------
    
    # Initialize the process returns TRUE or FALSE. TRUE means that a system exception occurred and the process should be stopped.FALSE means that the process should continue.
    init()
    if general.bol_systemException:
        end_process()
        return
    
    while general.int_numRetry<= general.int_totalRetry:
        # Reset the variables for each retry iteration
        general.str_messageError    =""
        general.bol_systemException = False
        
        # Get transaction data from the DataFrame
        get_transaction()         

        # If there is transaction data, the process continues
        while general.row_transactionItem is not None:
            str_typeException = process()

            match str_typeException:
                case "BusinessException":
                    general.int_transactionNumber += 1
                    general.bol_bussinessException = False
                    general.str_messageError       = ""
                    get_transaction() 
                case "SystemException":
                    general.int_numRetry += 1
                    print(f"Retry number: {general.int_numRetry}")
                    # close all
                    break   
                case "":
                    general.int_transactionNumber += 1
                    get_transaction()# If the process is successful, get the next transaction           
            
        # end process if there is no transaction data
        if general.row_transactionItem is None:
            print("No transaction data available.")
            # close all
            end_process()
            break 

    if general.bol_systemException:
        end_process()
                      
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   

    # Uncomment to mark this task as finished on BotMaestro
    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
         message="Task Finished OK."
     )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
