import openpyxl
wb=openpyxl.load_workbook('example.xlsx')
print(wb.sheetnames)  #printing all sheet names within the workbook
sheet=wb['Sheet3']   # trying to get one specific sheet from that workbook
print(sheet)  # each sheet is represented by a worksheet object
print(type(sheet))  #it shows that it is a worksheet object
print(sheet.title)  # getting the title of that sheet
anotherSheet=wb.active #to get the active sheet which is currently open
print(anotherSheet)

