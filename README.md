# CPPU-TimeTableSearching
CPPU查询某一节课有多少人上课

使用方法如下：

clone本项目到本地并打开目录

1. 使用有权限的账号登录本(专)科生教务管理系统
2. 点击排课管理
3. 选择课表管理
4. 进入课表查询
5. 选择学生课表
6. 点击批量生成课表
7. 选择学年学期与学员队，单击确定并等待教务系统生成出所有人的课表

下载zip文件并按照如下文件目录放置文件
```
└CPPU-TimeTableSearching
 ├xxxx-xxxx学年 第X学期 课表
 │├教室（*可选）
 ││├XXXXXX_教室课表.xls
 ││├...
 ││└XXXXXX_教室课表.xls
 |├教学班（*可选）
 ||
 ||
 |└学生
 | ├1班
 | |├xxXXx队1班（XX）_xxxxxxxxxx_X..X_学员课表.xls
 | |├...
 | |└xxXXx队1班（XX）_xxxxxxxxxx_X..X_学员课表.xls
 | ├2班
 | |├xxXXx队2班（XX）_xxxxxxxxxx_X..X_学员课表.xls
 | |├...
 | |└xxXXx队2班（XX）_xxxxxxxxxx_X..X_学员课表.xls
 | ├...
 | └x班
 |  ├xxXXx队x班（XX）_xxxxxxxxxx_X..X_学员课表.xls
 |  ├...
 |  └xxXXx队x班（XX）_xxxxxxxxxx_X..X_学员课表.xls
 └统计用
  ├2020-2021学年 第二学期
  ├txt
  ├班.py
  ├查询.py
  ├成队.py
  └合班.py
