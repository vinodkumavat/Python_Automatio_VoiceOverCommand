import gspread
from oauth2client import client
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Contact_Details").sheet1

#Fetching data
data = sheet.get_all_records()
#getting row data
row = sheet.row_values(3)
#getting coloum data
coloum = sheet.col_values(2)
#getting cell data
#cells = sheet.cell(i, j).value

for i in range(1, len(coloum)+1):
    for j in range(1, len(row)+1):
        print(sheet.cell(i, j).value)


print(len(data))

#Insert data

#data entry of one person
insertRow = ["Vinod", "8830313146", "vinodkumawat9167@gmail.com"]
sheet.insert_row(insertRow, len(sheet.get_all_records())+2)

print(len(sheet.get_all_records()))