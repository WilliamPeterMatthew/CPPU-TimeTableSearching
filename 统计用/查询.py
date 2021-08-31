# coding=utf-8
import xlwt
import xlrd
import os
from 配置 import *
if foldermode:
    lj='..\\'+semester+' 课表\\学生\\'
else:
    lj='..\\'+semester+foldersuf+'\\'
dicw={0:'星期一',1:'星期二',2:'星期三',3:'星期四',4:'星期五',5:'星期六',6:'星期日'}
dick={12:0,34:1,56:2,78:3,910:4}
dicl={0:12,1:34,2:56,3:78,4:910}
startdate=datetime.date(startyear,startmonth,startday)
queueyear=int(input("年："))
queuemonth=int(input("月："))
queueday=int(input("日："))
queuedate=datetime.date(queueyear,queuemonth,queueday)
subday=(queuedate-startdate).days
k=dick[int(input("课（12、34、56、78、910）："))]
pd=int(input("有课人员（0）/无课人员（1）："))
w=subday//7
d=subday%7
x=3+7*d+k
y=5+w
def excel_read(file_path,table,x,y):
    data=xlrd.open_workbook(file_path)
    table=data.sheet_by_name(table)
    return table.cell(y,x).value
def listdir(file_path):
    ls=[]
    for file in os.listdir(file_path):
        if not os.path.isdir(file_path+file):
            ls.append(file_path+file)
    return ls
s=[]
if foldermode:
    for i in range(1,classnum+1):
        file_path=lj+str(i)+'班\\'
        ls=listdir(file_path)
        for j in ls:
            if(pd^(len(excel_read(j,"Sheet1",x,y))>0)):
                s.append(j[len(file_path+filepre):-len(filesuf)])
else:
    file_path=lj
    ls=listdir(file_path)
    for j in ls:
        if(pd^(len(excel_read(j,"Sheet1",x,y))>0)):
            s.append(j[len(file_path+filepre):-len(filesuf)])
wj=__file__[:-5]+'结果'+time.strftime("%Y%m%d%H%M%S", time.localtime())+'.txt'
with open(wj,"w") as f:
    f.write(queuedate.strftime('%Y年%m月%d日 ')+dicw[d]+' '+"第{}节课".format(dicl[k])+' ')
    if(pd):
        f.write("{}人无课".format(len(s))+'\n')
    else:
        f.write("{}人有课".format(len(s))+'\n')
    for i in s:
        f.write(i+'\n')
print("查询结果已保存在文件{}中".format(wj))
