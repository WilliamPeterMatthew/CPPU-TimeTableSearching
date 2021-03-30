如根目录下的说明文件所述，你应该按如下步骤执行脚本  
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

------

如根目录下的说明文件所述，你应该执行以下命令查询某一天某一节课的人员情况。  
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
