        arr_session['webbot'].wait(2000)           
        tables = arr_session['webbot'].find_elements(selector='sapBUiListTab', by=arr_session['By'].CLASS_NAME)
        print(f"Tables: {tables.__len__()}")
        if tables.__len__() > 0:
            # Get the first table
            table         = tables[0]    
            rows          = table.find_elements(value='sapBUiListRow', by=arr_session['By'].CLASS_NAME) 
            print(f"Rows: {len(rows)}")
            table_html    = table.get_attribute('outerHTML')   
            table_html_io = io.StringIO(table_html)
            df            = pd.read_html(table_html_io)[0]
            print(len(df))
            # Get the rows of the table
            #rows = table.find_elements(selector='sapBUiListRow', by=arr_session['By'].CLASS_NAME)