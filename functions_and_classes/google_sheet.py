import Functions_and_classes.google_connect as gc
import pandas as pd
#import send_email as sendE



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