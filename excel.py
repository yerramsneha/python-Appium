import xlsxwriter

book = xlsxwriter.Workbook('Example1.xlsx')
sheet = book.add_worksheet()

row = 0
column = 0

content = ["Parker", " Smith", "John"]

for item in content:
    sheet.write(row,column,item)
    row+=1

book.close()
