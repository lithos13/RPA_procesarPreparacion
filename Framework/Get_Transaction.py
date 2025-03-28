from Functions_and_classes.sys_context import general

def get_transaction():
    if general.df_transactionData.empty:
        print("No transaction data available.")
        general.row_transactionItem = None

    else:
        print(general.df_transactionData)        
        if general.int_transactionNumber<=general.df_transactionData.length:
            general.row_transactionItem = general.df_transactionData.iloc[general.int_transactionNumber]
        else:
            print("No more transaction data available.")
            general.row_transactionItem = None    