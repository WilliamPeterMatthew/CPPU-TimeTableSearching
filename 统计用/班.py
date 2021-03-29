import xlwt
import xlrd
ml=__file__[:-5]
xg=ml[-1]
kz='2020-2021学年 第二学期'+xg
lj=ml[:-4]+kz[:-1]+' 课表'+xg+'学生'+xg
def excel_read(file_path, table, x, y):
    data = xlrd.open_workbook(file_path)
    table = data.sheet_by_name(table)
    return table.cell(y, x).value
for i in range(1,7):
    wb=xlwt.Workbook()
    ws=wb.add_sheet('Sheet1')
    for x in range(3,51):
        if(x%7==2):
            continue
        for y in range(5,25):
            with open(ml+'txt'+xg+str(i)+'.txt', "r") as f:
                lb= f.readlines()
            s=0
            for j in lb:
                j = j.strip('\n') 
                if(len(excel_read(lj+str(i)+'班'+xg+j,"Sheet1",x,y))>0):
                    s+=1
            ws.write(y,x,str(s))
    wb.save(ml+kz+str(i)+'n.xls')
    print('{}班已完成'.format(i))
