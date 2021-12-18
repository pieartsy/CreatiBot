# import gspread
#from oauth2client.service_account import ServiceAccountCredentials
#import google.oauth2.credentials
#import google_auth_oauthlib.flow
#import random
#import json
#import os

#scope = ['https://spreadsheets.google.com/feeds',
 #   'https://www.googleapis.com/auth/drive'
#]
# Use the client_secret.json file to identify the application requesting
# authorization. The client ID (from that file) and access scopes are required.
#credentials = google_auth_oauthlib.flow.Flow.from_client_config(json.loads(os.environ.get("GOOGLE_API_CREDS")), scope)

#gc = gspread.authorize(credentials)
#gc.login()
#wks = gc.open_by_key("1q7W_S13YCDtw8_2VoLdJ683kmkNRiDIv6KD6cGhi7d4").sheet1

#def saveprompt(arg):
 #   row = [arg]
  #  index = 1
   # wks.insert_row(row, index)

#def getprompt():
 #   randomuserprompt = ""
  #  counter = 0
   # while counter < wks.row_count:
    #    if randomuserprompt == "" and wks.col_values(1):
     #       randomuserprompt = random.choice(wks.col_values(1))
      #      counter +=1
       # if not wks.col_values(1):
        #    return "Your prompts list is empty!"
        #else:
#            break
 #   return randomuserprompt