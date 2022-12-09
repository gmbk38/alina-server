import gspread

conn = gspread.service_account('alina/alina-368013-2b53c4cdae8d.json')

sh = conn.open('alina')

wks = sh.worksheet("Лист1")

# print(wks.row_count, wks.col_count)
# print(wks.acell('A1').value)
# test = None
# print(test != None)
# print(wks.acell('A20').value)
# print(wks.cell(1, 1).value)
# print(wks.get('A1:A9'))
# print(wks.get('A1:A9'))
# print(wks.col_values(1))
# print(wks.find('102').row, wks.find('102').col)

wks.update('A1:C1', [['b4','b5', 'b6']])