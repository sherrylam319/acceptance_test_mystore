from __future__ import print_function
from google.oauth2 import service_account
import googleapiclient.discovery
from tests.acceptance.utils.path import *


class GsheetData:
    def __init__(self, spreadsheet_id, val_range_name, key_range_name):
        self.spreadsheet_id = spreadsheet_id
        self.val_range_name = val_range_name
        self.key_range_name = key_range_name


    def get_gsheet_data(self):

        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = path_param_1() / "the/full/path/of/your/service_account.json"


        credentials = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        gsheetadmin = googleapiclient.discovery.build('sheets', 'v4', credentials=credentials)

        gsheet = gsheetadmin.spreadsheets()
        result_val = gsheet.values().get(spreadsheetId=self.spreadsheet_id,
                                        range=self.val_range_name).execute()
        values_val = result_val.get('values')

        result_key = gsheet.values().get(spreadsheetId=self.spreadsheet_id,
                                        range=self.key_range_name).execute()
        values_key = result_key.get('values')

        user_info = dict(zip(values_key[0], values_val[0]))
        return user_info



