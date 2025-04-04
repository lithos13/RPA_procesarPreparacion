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
    
    while general.int_numRetry<= general.int_numRetry:
        # If there is no system exception, the process continues
        if not general.bol_systemException:
            get_transaction()  
        else:       
            end_process()
            break  

        # If there is transaction data, the process continues
        while general.row_transactionItem is not None:
            process()
            if not general.bol_systemException:
                general.int_transactionNumber += 1
                get_transaction() 
            else:
                general.int_numRetry += 1
                # close all
                break
        # end process if there is no transaction data        
        end_process()
        break  
    # end process to finish the process completely    
    end_process()      
    
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
