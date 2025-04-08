from Functions_and_classes.sys_bussinesException import BusinessException
from Functions_and_classes.sys_context import general

def process():
    try:
        # Your main process logic here
        print("Executing process..."+ general.row_transactionItem["Nombre de proveedor"])
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

