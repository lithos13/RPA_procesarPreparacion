from Functions_and_classes.sys_context import general

def get_transaction():
    try:
        if general.df_transactionData.empty:
            print("No transaction data available.")
            general.row_transactionItem = None

        else:        
            if general.int_transactionNumber<len(general.df_transactionData):
                print(f"Transaction number: {general.int_transactionNumber}")
                general.row_transactionItem = general.df_transactionData.iloc[general.int_transactionNumber]                
            else:
                print("No more transaction data available.")
                general.row_transactionItem = None    
    except  IndexError as e:
        print(f"get_transaction: Index error occurred: {e}")
        general.str_messageError = f"Index error occurred: {e}"    
        general.bol_systemException = True        