import xlwt
import xlrd
import os
from 配置 import *
if foldermode:
    print('文件夹模式开启时直接成队功能不可用，请先运行\"班.py\"进行按班统计，然后运行\"成队.py\"进行全队统计。')
    input("请按回车键（Enter）继续. . . ")
    os._exit(0)
lj='..\\'+semester+foldersuf+'\\'
def excel_gen(file_path,table):
    data=xlrd.open_workbook(file_path)
    table=data.sheet_by_name(table)
    s=[[0 for si in range(totalweeks+5)] for si in range(51)]
    for x in range(3,51):
        if(x%7==2):
            continue
        for y in range(5,totalweeks+5):
            if(len(table.cell(y,x).value)>0):
                s[x][y]=1
    return s
def listdir(file_path):
    ls=[]
    for file in os.listdir(file_path):
        if not os.path.isdir(file_path+file):
            ls.append(file_path+file)
    return ls
if not os.path.exists(semester):
    os.makedirs(semester)
file_path=lj
ls=listdir(file_path)
s=[[0 for si in range(totalweeks+5)] for si in range(51)]
for j in ls:
    ts=excel_gen(j,"Sheet1")
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
wb.save(semester+'\\''0n.xls')
print('已完成')
