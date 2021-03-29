import xlwt
import xlrd
ml=__file__[:-5]
xg=ml[-1]
ml+='2020-2021学年 第二学期'+xg
def excel_read(file_path, table, x, y):
    data = xlrd.open_workbook(file_path)
    table = data.sheet_by_name(table)
    return table.cell(y, x).value
for i in range(1,7,2):
    wb=xlwt.Workbook()
    ws=wb.add_sheet('Sheet1')
    for x in range(3,51):
        if(x%7==2):
            continue
        for y in range(5,25):
            s=0
            for j in range(i,i+2):
                s+=eval(excel_read(ml+str(j)+'n.xls',"Sheet1",x,y))
            ws.write(y,x,str(s))
    wb.save(ml+str(i)+str(i+1)+'n.xls')
