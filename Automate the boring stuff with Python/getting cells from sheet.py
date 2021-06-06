import openpyxl
wb=openpyxl.load_workbook('example.xlsx')
sheet=wb['Sheet1']
print(sheet['A1'])
print(sheet['A1'].value)
c=sheet['B1']
print(c.value)
print('Row %s,Column %s is %s'%(c.row,c.column,c.value))
print('Cell %s is %s' %(c.coordinate,c.value))
print(sheet['C1'].value)


