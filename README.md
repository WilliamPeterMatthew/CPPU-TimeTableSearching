# CPPU-TimeTableSearching
CPPU查询某一节课有多少人上课

## 初始化

clone本项目到本地并打开目录

1. 使用有权限的账号登录本(专)科生教务管理系统
2. 点击排课管理
3. 选择课表管理
4. 进入课表查询
5. 选择学生课表
6. 点击批量生成课表
7. 选择学年学期与学员队，单击确定并等待教务系统生成出所有人的课表

下载zip文件并按照如下文件目录放置文件
```plain
└CPPU-TimeTableSearching
 ├xxxx-xxxx学年 第X学期 课表
 │├教室（*可选）
 ││├XXXXXX_教室课表.xls
 ││├...
 ││└XXXXXX_教室课表.xls
 |├教学班（*可选）
 ||├常规班级
 |||├常规班级_xxXXx队1班（XX）_X...X(X...X)_班级课表.xls
 |||├常规班级_xxXXx队2班（XX）_X...X(X...X)_班级课表.xls
 |||├...
 |||└常规班级_xxXXx队x班（XX）_X...X(X...X)_班级课表.xls
 ||├分级班
 |||├分级班_xxXXxxx班（X...X）(X...X)_班级课表.xls
 |||├...
 |||└分级班_xxXXxxx班（X...X）(X...X)_班级课表.xls
 ||├糅合（需要自己制作如下内容）
 |||├糅合_xxXXx队1班（XX）,xxXXx队2班（XX）_X...X(X...X)_班级课表.xls
 |||├糅合_xxXXx队3班（XX）,xxXXx队4班（XX）_X...X(X...X)_班级课表.xls
 |||├...
 |||└糅合_xxXXx队x班（XX）,xxXXx队x班（XX）_X...X(X...X)_班级课表.xls
 ||└综合（需要自己制作如下内容）
 || ├综合_xxXXx队1班（XX）_X...X(X...X)_班级课表.xls
 || ├综合_xxXXx队2班（XX）_X...X(X...X)_班级课表.xls
 || ├...
 || └综合_xxXXx队x班（XX）_X...X(X...X)_班级课表.xls
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
  ├xxxx-xxxx学年 第X学期
  ├txt
  ├班.py
  ├查询.py
  ├成队.py
  └合班.py
```

接着你需要统计各班的文件并汇总，你可以在命令行使用如下命令处理出一份文件
```bash
dir > x.txt
```

你会得到文件x.txt，其内容例如
```plain
 驱动器 x 中的卷是 T...T
 卷的序列号是 FFFF-FFFF

X:\...\CPPU-TimeTableSearching\xxxx-xxxx学年 第X学期 课表\学生\x班 的目录

xxxx/xx/xx  xx:xx    <DIR>          .
xxxx/xx/xx  xx:xx    <DIR>          ..
xxxx/xx/xx  xx:xx                 0 x.txt
xxxx/xx/xx  xx:xx            xx,xxx xxXXx队x班（XX）_xxxxxxxxxx_X..X_学员课表.xls
...
xxxx/xx/xx  xx:xx            xx,xxx xxXXx队x班（XX）_xxxxxxxxxx_X..X_学员课表.xls
              xx 个文件      x,xxx,xxx 字节
               2 个目录 xx,xxx,xxx,xxx 可用字节
```

你可以通过如下步骤获得一份名单文件
1. 删除前8行和后2行
2. 在支持Alt键选择的文本编辑器中，将文件前的日期和大小信息删除（推荐软件：[notepad++](https://notepad-plus-plus.org/download/)）

你应该制作出如下内容的文件
```plain
xx,xxx xxXXx队x班（XX）_xxxxxxxxxx_X..X_学员课表.xls
...
xx,xxx xxXXx队x班（XX）_xxxxxxxxxx_X..X_学员课表.xls
```

现在将目录更新为如下内容
```plain
└CPPU-TimeTableSearching
 ├xxxx-xxxx学年 第X学期 课表
 │├教室（*可选）
 ││├XXXXXX_教室课表.xls
 ││├...
 ││└XXXXXX_教室课表.xls
 |├教学班（*可选）
 ||├常规班级
 |||├常规班级_xxXXx队1班（XX）_X...X(X...X)_班级课表.xls
 |||├常规班级_xxXXx队2班（XX）_X...X(X...X)_班级课表.xls
 |||├...
 |||└常规班级_xxXXx队x班（XX）_X...X(X...X)_班级课表.xls
 ||├分级班
 |||├分级班_xxXXxxx班（X...X）(X...X)_班级课表.xls
 |||├...
 |||└分级班_xxXXxxx班（X...X）(X...X)_班级课表.xls
 ||├糅合（需要自己制作如下内容）
 |||├糅合_xxXXx队1班（XX）,xxXXx队2班（XX）_X...X(X...X)_班级课表.xls
 |||├糅合_xxXXx队3班（XX）,xxXXx队4班（XX）_X...X(X...X)_班级课表.xls
 |||├...
 |||└糅合_xxXXx队x班（XX）,xxXXx队x班（XX）_X...X(X...X)_班级课表.xls
 ||└综合（需要自己制作如下内容）
 || ├综合_xxXXx队1班（XX）_X...X(X...X)_班级课表.xls
 || ├综合_xxXXx队2班（XX）_X...X(X...X)_班级课表.xls
 || ├...
 || └综合_xxXXx队x班（XX）_X...X(X...X)_班级课表.xls
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
  ├xxxx-xxxx学年 第X学期
  ├txt
  |├1.txt
  |├2.txt
  |├...
  |└x.txt
  ├班.py
  ├查询.py
  ├成队.py
  └合班.py
```

现在你可以进行统计了。

## 快速统计队内每时刻上课人数
首先，你需要进入目录`统计用`，接着，你应该按如下步骤执行脚本  
```bash
python 班.py
python 合班.py
python 成队.py
```
这样可以生成一份课表统计列表，文件放在xxxx-xxxx学年 第X学期中，方便安排队内事务。  

对于xxxx-xxxx学年 第X学期中的文件说明如下

你会看到如下列表的文件
```plain
└xxxx-xxxx学年 第X学期
 ├0n.xls
 ├1n.xls
 ├2n.xls
 ├...
 ├xn.xls
 ├xn.xls
 ├12n.xls
 ├34n.xls
 ├...
 └xxn.xls
```
所有xls文件与CPPU课表格式相同。
- 0n.xls中包含的信息是全队的上课人数。
- xn.xls中包含的信息是综合后的单个教学班的上课人数。
- xxn.xls中包含的信息是糅合后的两个教学班的上课人数。

## 查询某节课有多少人有课/无课以及对应的名单

你应该执行以下命令查询某一天某一节课的人员情况。  
```bash
python 查询.py
```

你会在执行中收到如下询问
```
月：
日：
课（12、34、56、78、910）：
有课人员（0）/无课人员（1）：
```

你应该给出回答，例如
```
月：3
日：3
课（12、34、56、78、910）：78
有课人员（0）/无课人员（1）：0
```

你会看到如下提示
```
查询结果已保存在文件X:\...\CPPU-TimeTableSearching\统计用\结果xxxxxxxxxxxxxx.txt中
```

你可以在当前目录下找到结果xxxxxxxxxxxxxx.txt，打开即可查看到查询结果，根据示例中的回答，文件内容如下
```
3月3日 星期三 第78节课 xx人有课
XXX
XX
XXX
XX
XX
XXX
XX
XX
XXX
XXX
XXX
XXX
XXX
XX
XX
XX
XXX
XX
XXX
```
