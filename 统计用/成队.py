import xlwt
import xlrd
import os
from 配置 import *
if not foldermode:
    print('文件夹模式未开启时按班统计后合队功能不可用，请运行\"队.py\"进行全队统计，或按说明文档放置文件后在\"配置.py\"中修改foldermode为True。')
    input("请按回车键（Enter）继续. . . ")
    os._exit(0)
def excel_gen(file_path,table):
    data=xlrd.open_workbook(file_path)
    table=data.sheet_by_name(table)
    s=[[0 for si in range(totalweeks+5)] for si in range(51)]
    for x in range(3,51):
        if(x%7==2):
            continue
        for y in range(5,totalweeks+5):
            s[x][y]=int(table.cell(y,x).value)
    return s
s=[[0 for si in range(totalweeks+5)] for si in range(51)]
for i in range(1,classnum+1):
    file=semester+'\\'+str(i)+'n.xls'
    ts=excel_gen(file,"Sheet1")
    for x in range(3,51):
        if(x%7==2):
            continue
        for y in range(5,totalweeks+5):
            s[x][y]+=ts[x][y]
wb=xlwt.Workbook()
ws=wb.add_sheet('Sheet1')
for x in range(3,51):
    if(x%7==2):
        continue
    for y in range(5,totalweeks+5):
        ws.write(y,x,str(s[x][y]))
wb.save(semester+'\\'+'0n.xls')
print('已完成')
