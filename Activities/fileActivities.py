import os
import pandas as pd
import xlwings as xw
from Functions_and_classes.sys_context import general


def read_ExcelFile(str_ruta):
    
    # app allow  to open the file in background 
    app = xw.App(visible=False)  
    
    try:
        # Check if the file exists
        if not os.path.exists(str_ruta):
            raise FileNotFoundError(f"File {str_ruta} does not exist.")
        
        # Open the Excel file using xlwings
        # This will open the file in the background
        wb = app.books.open(str_ruta)
        # lets save and close the file, this solves a problem with the original file generates by SAP
        wb.save()
        wb.close()
        # the data stars on row 5 and column B to I
        df = pd.read_excel(str_ruta, skiprows=4, usecols="B:I", engine='openpyxl')               
        # Remove the file after reading
        os.remove(str_ruta)
        return df       

    except Exception as e:
          general.str_messageError    = f"An error occurred while reading the Excel file: {e}"          
          raise Exception(general.str_messageError)          
    finally:
        app.quit()


# Clean up the path of the file before downloding the new one
def cleanPath(str_ruta):
    if  os.path.exists(str_ruta):
        os.remove(str_ruta)
