import xlwt
import xlrd
import os
from 配置 import *
if not foldermode:
    print('文件夹模式未开启时按班统计功能不可用，请按说明文档放置文件后在\"配置.py\"中修改foldermode为True。')
    input("请按回车键（Enter）继续. . . ")
    os._exit(0)
lj='..\\'+semester+' 课表\\学生\\'
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
for i in range(1,classnum+1):
    file_path=lj+str(i)+'班\\'
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
    wb.save(semester+'\\'+str(i)+'n.xls')
    print('{}班已完成'.format(i))
