import Functions_and_classes.google_connect as gc
from decouple import config
import pandas as pd
#import send_email as sendE


def get_sheet(id):
    try:       
        sheet           = gc.client.open_by_key(id)
        sheet_instance  = sheet.get_worksheet(0)
        records         = sheet_instance.get_all_records()
        return records
    except gc.gspread.exceptions.APIError as e:
           error_json   = e.response.json()
           error_status = error_json.get("error", {}).get("status") 
           if error_status == 'PERMISSION_DENIED':
                    msj_error="The Service Account does not have permission to read or write on the spreadsheet document. Have you shared the spreadsheet with %s?" % gc.client_email
                    print(msj_error)
                    
           elif error_status == 'NOT_FOUND':
                    msj_error="Trying to open non-existent spreadsheet document. Verify the document id exists (%s)." % config('ID_SHEET_CONFIG')
                    print(msj_error)
                    
           else:       
                msj_error="The Google API returned an error: %s" % e
                print(msj_error)
                

    #sendE.send_Mail(config('HEAD_SUBJECT')+' '+error_status, config('EMAIL_OWNER'),msj_error, config('EMAIL_OWNER'))
    return []

def get_google_sheet_as_dataframe(sheet_id, sheet_name):
    """
    Retrieves all data from a specific Google Sheet and saves it into a pandas DataFrame.

    :param sheet_id: The ID of the Google Sheet (found in the URL of the sheet).
    :param sheet_name: The name of the sheet (e.g., 'Sheet1').
    :return: A pandas DataFrame containing the sheet data.
    """
    # Authorize Google Sheets
    sheets_service =gc.authorize_google_sheets()

    # Use the Sheets API to get all data from the specified sheet
    result = sheets_service.spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range=sheet_name  # Specify only the sheet name to get all data
    ).execute()

    # Extract the data
    rows = result.get('values', [])

    # Convert the data to a pandas DataFrame
    if rows:
        df = pd.DataFrame(rows[1:], columns=rows[0])  # Use the first row as column headers
    else:
        df = pd.DataFrame()  # Return an empty DataFrame if no data is found

    return df